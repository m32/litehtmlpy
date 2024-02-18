#
# cmake -DCMAKE_BUILD_TYPE=Debug .
# cmake -DCMAKE_BUILD_TYPE=Release .
#
cmake_minimum_required(VERSION 3.4...3.18)
project(litehtmlpy)

# https://stackoverflow.com/questions/38296756/what-is-the-idiomatic-way-in-cmake-to-add-the-fpic-compiler-option
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

option(LITEHTMLPY_BUILD_TESTING "enable testing for litehtmlpy" OFF)

find_package(Git)

if(NOT EXISTS ${CMAKE_SOURCE_DIR}/litehtml)
    execute_process(COMMAND "${GIT_EXECUTABLE}" clone --depth 1 https://github.com/m32/litehtml -b master
        WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}")
endif()
if(NOT EXISTS ${CMAKE_SOURCE_DIR}/pybind11)
    if(CMAKE_CROSSCOMPILING)
        execute_process(COMMAND "${GIT_EXECUTABLE}" clone --depth 1 https://github.com/pybind/pybind11.git -b v2.9
            WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}")
    else()
        execute_process(COMMAND "${GIT_EXECUTABLE}" clone --depth 1 https://github.com/pybind/pybind11.git -b v2.11
            WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}")
    endif()
endif()

add_subdirectory(litehtml)

if(CMAKE_CROSSCOMPILING)
    # Tell pybind11 where the target python installation is
    set(PYTHON_INCLUDE_DIR ${MY_TARGET_PYTHON_INCLUDE_DIRS} CACHE INTERNAL "Cross python include path")
    set(PYTHON_INCLUDE_DIRS ${MY_TARGET_PYTHON_INCLUDE_DIRS} CACHE INTERNAL "Cross python include path")
    set(PYTHON_MODULE_EXTENSION ".pyd" CACHE INTERNAL "Cross python lib extension")

    # Disable pybind11 python search mechanism
    set(PYTHONLIBS_FOUND TRUE CACHE INTERNAL "")

    target_compile_definitions(litehtml PRIVATE
        -DLITEHTML_NO_THREADS
    )
endif()

add_subdirectory(pybind11)

pybind11_add_module(
    litehtmlpy
    src/litehtmlpy.cpp
)

if(LITEHTMLPY_BUILD_TESTING)
    set_target_properties(litehtmlpy PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/src/litehtmlpy")
endif()

#if(NOT CMAKE_CROSSCOMPILING)
#    find_package(PythonLibs 3.6)
#    #find_package(PythonLibs 3.8 REQUIRED)
#    #find_package(PythonLibs 3.11.2 EXACT REQUIRED)
#endif()

set_target_properties(litehtmlpy PROPERTIES
    CXX_STANDARD 11
    C_STANDARD 99
)

target_compile_definitions(litehtmlpy PRIVATE
    #-DUNICODE
)

target_include_directories(litehtmlpy PRIVATE
#    ${PYTHON_INCLUDE_DIRS}
    litehtml/include
#    ${PYBIND11_INCLUDE_DIR}
)

target_link_libraries(litehtmlpy PRIVATE
    litehtml
    gumbo
#    ${PYTHON_LIBRARIES}
)

if(CMAKE_CROSSCOMPILING)
target_compile_definitions(litehtmlpy PRIVATE
    -DMS_WIN64
)
target_compile_options(litehtmlpy PRIVATE
    -Wa,-mbig-obj
)
target_link_options(litehtmlpy PRIVATE
    -static
    -static-libgcc
    -static-libstdc++
)
endif()
