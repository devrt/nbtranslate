#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def main():
    setup(
        name='nbtranslate',
        version='0.0.1',
        author='Yosuke Matsusaka',
        author_email='yosuke.matsusaka@gmail.com',
        url='http://github.com/devrt/nbtranslate',
        license='BSD',
        packages=['nbtranslate'],
        install_requires=[
            'nbformat',
            'polib'
        ],
        entry_points={
            'console_scripts': ['nbtranslate = nbtranslate.nbtranslate:main']
        }
    )


if __name__ == '__main__':
    main()
