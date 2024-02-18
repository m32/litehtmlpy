#!/bin/bash
set -e -x

install_manylinux_build_deps() {
  yum install -y epel-release;
  yum -y install autoconf automake cmake gcc gcc-c++ git make pkgconfig ninja-build 
}

install_ubuntu_build_deps() {
  sudo apt-get update
  sudo apt-get -y install build-essential git make pkg-config cmake ninja-build
}

upload_artifacts_to_pypi() {
  python3 -m pip install twine
  twine upload dist/*
}
