#!/bin/bash
set -e -u -x
cd /io

#[ -n "$WHEELHOUSE" ] || 
WHEELHOUSE=wheelhouse
#[ -z "$PYTHON_BUILD_VERSION" ] && 
PYTHON_BUILD_VERSION="cp311-cp311"

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" -w /io/wheelhouse/
    fi
}


# Install a system package required by our library
# yum install -y pybind11

# Compile wheels
for PYBIN in /opt/python/${PYTHON_BUILD_VERSION}/bin; do
    #"${PYBIN}/pip" install -r /io/dev-requirements.txt
    "${PYBIN}/pip" wheel /io/ --no-deps -w /io/${WHEELHOUSE} || exit 1
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
for PYBIN in /opt/python/${PYTHON_BUILD_VERSION}/bin; do
    "${PYBIN}/pip" install litehtmlpy --no-index -f /io/${WHEELHOUSE}
    "${PYBIN}/python" litehtmld.py
done
