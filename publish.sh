#!/usr/bin/env bash
set -ex
python setup.py clean ; rm -rf dist || true
python setup.py build sdist
twine upload --verbose dist/*
