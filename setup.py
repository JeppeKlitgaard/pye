#!/usr/bin/env python

from setuptools import setup
from pye import VERSION

setup(
    name="pye",
    version=".".join(str(i) for i in VERSION),
    description="A series of useful tools. Extends Python.",
    #TODO Add long_description
    author="Jeppe Klitgaard",
    author_email="jeppe@dapj.dk",
    url="https://github.com/dkkline/pye",
    packages=["pye",
              "pye.math"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"]
)
