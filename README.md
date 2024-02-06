# python-litehtml
LiteHtmlPy is a solution that helps python developers to create printouts and previews of html5/css3 pages without using a web browser.

## Links
  * [litehtml library](https://github.com/litehtml/litehtml)
  * [pybind11](https://github.com/pybind/pybind11)

## Cleanup repository
./x-cleanup

## Linux configure
./x-build-cmake -DCMAKE_BUILD_TYPE=Debug
./x-build-cmake -DCMAKE_BUILD_TYPE=Release

## Cross Mingw configure for python 2.7
./x-build-cmake-mingw

## Build for manylinux inside docker
./x-build-docker

## Just setup.py build
./x-build-python
