#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'TencentYoutuyun',
    version = '1.0.0',
    keywords = ('TencentYoutuyun', 'qcloud'),
    description = 'python sdk for open.youtu.qq.com',
    license = 'MIT License',
    install_requires=['requests'],
    packages = find_packages(),
    platforms = 'any',
)