# -*- coding: utf-8 -*-

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='cli',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    entry_points={
        'console_scripts': [
            'cli=cli.__main__:main',
        ],
    },
)
