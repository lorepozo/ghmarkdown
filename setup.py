#!/usr/bin/env python

from setuptools import setup, find_packages


version = '1.0.1'

setup(
    name='ghmarkdown',
    version=version,
    description='ghmarkdown is the complete command-line tool for GitHub-flavored markdown',
    long_description=open('README.rst').read(),
    author='Lucas Morales',
    author_email='lucasem@mit.edu',
    license='GNU GPL v2.0',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Communications',
            'Topic :: Software Development',
            'Topic :: Software Development :: Documentation',
            'Topic :: Text Processing :: Markup',
            'Topic :: Text Processing :: Markup :: HTML',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ],
    keywords="markdown live html github command command-line cli",
    url='http://github.com/lukedmor/ghmarkdown',
    packages=find_packages(),
    package_data={
        'ghmarkdown': ['ceiling.dat', 'floor.dat']
    },
    install_requires = ['requests'],
    entry_points={
        'console_scripts': [
            'ghmarkdown=ghmarkdown.ghmarkdown:main'
        ],
    }
)
