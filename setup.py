#!/usr/bin/env python

"""The setup script."""
import time
from setuptools import setup, find_packages

version = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().split('\n')

setup(
    author="nlpzoo",
    author_email='yuanjie@example.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Create a Python package.",
    entry_points={
        'console_scripts': [
            'nlpzoo=nlpzoo.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nlpzoo',
    name='nlpzoo',
    packages=find_packages(include=['nlpzoo', 'nlpzoo.*']),

    test_suite='tests',
    url='https://github.com/Jie-Yuan/nlpzoo',
    version=version, # '0.0.0',
    zip_safe=False,
)
