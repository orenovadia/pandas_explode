#!/usr/bin/env bash
set -ex
python setup.py clean ; rm -r dist
python setup.py build sdist
twine upload dist/*