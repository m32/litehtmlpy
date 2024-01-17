#
# cmake -DCMAKE_BUILD_TYPE=Debug .
#
cmake_minimum_required(VERSION 3.4...3.18)
project(litehtmlpy)

# https://stackoverflow.com/questions/38296756/what-is-the-idiomatic-way-in-cmake-to-add-the-fpic-compiler-option
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_TESTING NO)

add_subdirectory(litehtml)
add_subdirectory(pybind11)

pybind11_add_module(
    litehtmlpy
    src/litehtmlpy.cpp
)

#find_package(PythonLibs 3.0)
#find_package(PythonLibs 3.8 REQUIRED)
find_package(PythonLibs 3.11.2 EXACT REQUIRED)

set_target_properties(litehtmlpy PROPERTIES
    CXX_STANDARD 11
    C_STANDARD 99
)

target_compile_definitions(litehtmlpy PRIVATE
    #-DUNICODE
)

target_include_directories(litehtmlpy PRIVATE
    ${PYTHON_INCLUDE_DIRS}
    litehtml/include
    ${PYBIND11_INCLUDE_DIR}
)

target_link_libraries(litehtmlpy PRIVATE
    litehtml
    gumbo
    ${Python_LIBRARIES}
)
