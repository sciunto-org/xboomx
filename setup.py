# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages


def read_version(name):
    with open(os.path.join(os.path.dirname(__file__), name, '__init__.py')) as f:
        for line in f:
            match = re.match(r"^__version__ = ['\"]([^'\"]*)['\"]", line)
            if match:
                return match.group(1)
        raise RuntimeError("Unable to find version string.")


def parse_requirements(filename):
	with open(filename, 'r') as file:
		return file.read().splitlines()


setup(
    name='xboomx',
    version=read_version('xboomx'),
    packages=['xboomx'],
    scripts=['xboomx/bin/xboomx_sort.py',
             'xboomx/bin/xboomx_update.py',
             'xboomx/bin/xboomx',
             ],
    license='GPL-2.0',
    long_description='A wrapper for most common occurrences in dmenu',
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True,
    author="Francois Boulogne",
    author_email="devel@sciunto.org",
    url="https://github.com/sciunto/xboomx",
)
