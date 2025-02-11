# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='xboomx',
    version='2025.02.11',
    packages=['xboomx'],
    scripts=['xboomx/bin/xboomx_path.py',
             'xboomx/bin/xboomx_sort.py',
             'xboomx/bin/xboomx_update.py',
             'xboomx/bin/xboomx',
    license='GPL-2.0',
    long_description='A wrapper for most common occurrences in dmenu',
    install_requires=[],
    include_package_data=True,
    package_data={'shared': ["etc/config"]},
    author="Francois Boulogne",
    author_email="devel@sciunto.org",
    url="https://github.com/sciunto/xboomx",
)
