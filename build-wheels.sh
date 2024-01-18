#!/bin/bash
set -e -u -x
cd /io
PLAT=$AUDITWHEEL_PLAT

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /io/wheelhouse/
    fi
}


# Install a system package required by our library
# yum install -y pybind11

# Compile wheels
for PYBIN in /opt/python/cp311-cp311/bin; do
    #"${PYBIN}/pip" install -r /io/dev-requirements.txt
    "${PYBIN}/pip" wheel /io/ --no-deps -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
for PYBIN in /opt/python/cp311-cp311/bin; do
    "${PYBIN}/pip" install litehtmlpy --no-index -f /io/wheelhouse
    "${PYBIN}/python" litehtmld.py
done
