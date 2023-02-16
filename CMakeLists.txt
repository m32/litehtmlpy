cmake_minimum_required(VERSION 3.4...3.18)
project(litehtmlpy)

# https://stackoverflow.com/questions/38296756/what-is-the-idiomatic-way-in-cmake-to-add-the-fpic-compiler-option
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_subdirectory(litehtml)

set(SOURCES
    src/py_container.cpp
)

find_package(PythonLibs 3.0)

add_library (litehtmlpy MODULE ${SOURCES})

set_target_properties(litehtmlpy PROPERTIES
    CXX_STANDARD 11
    C_STANDARD 99
)

target_compile_definitions(litehtmlpy PRIVATE
    #-DUNICODE
)

target_include_directories(litehtmlpy PRIVATE
    .
)
target_include_directories(litehtmlpy PRIVATE
    ${PYTHON_INCLUDE_DIRS}
    litehtml/include
)

target_link_libraries(litehtmlpy ${PYTHON_LIBRARIES} litehtml gumbo)
