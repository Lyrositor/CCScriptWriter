#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="CCScriptWriter",
    version="1.2",
    description="Extracts the dialogue from EarthBound and outputs it into a CCScript file.",
    url="https://github.com/Lyrositor/CCScriptWriter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ccscriptwriter = CCScriptWriter.CCScriptWriter:main"
        ]
    }
)