#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'TencentYoutuyun',
    version = '1.0.2',
    keywords = ('TencentYoutuyun', 'qcloud'),
    description = 'python sdk for app.qcloud.com',
    license = 'MIT License',
    install_requires=['requests'],

    author = 'jayli',
    author_email = 'jayli@tencent.com',
    
    packages = find_packages(),
    platforms = 'any',
)