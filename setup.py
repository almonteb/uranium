#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    "docopt==0.6.2",
    "pip==7.1.2",
    "requests==2.9.1",
    "setuptools==18.2",
    "virtualenv==13.1.2"
]

tests_require = [
    'httpretty',
]

setup(name='uranium',
      version='0.2.31b',
      description='a build system for python',
      long_description=open('README.rst').read(),
      author='Yusuke Tsutsumi',
      author_email='yusuke@tsutsumi.io',
      url='http://uranium.readthedocs.org',
      packages=find_packages(),
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Topic :: System :: Software Distribution',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ],
      entry_points={
          'console_scripts': [
              'uranium=uranium.scripts.main:main'
          ],
      },
      tests_require=tests_require
)
