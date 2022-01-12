#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


setup(
    name="simulation",
    version="0.1.0",
    license="BSD-2-Clause",
    description="An Evolution Simulatior - Including an agent based simulation and a learning algorithm.",
    author="Tomer Goren",
    url="https://https://github.com/gegiti/Simulation",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    python_requires=">3.9.6",
    install_requires=[
        "numpy",
        "opencv-python",
        "pytest",
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "simulation = simulation.__main__:main",
        ]
    },
)
