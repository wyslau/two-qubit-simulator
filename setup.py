"""

Setup script for the two_qubit_simulator module

"""

from __future__ import print_function

from setuptools import setup, find_packages

def main():
    setup(
        name='two_qubit_simulator',
        version='0.0',
        packages=find_packages(),
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        install_requires=['numpy', 'pytest', 'pylint'],
        author='Python@EQUS',
        author_email='python@equs.org',
        description='A simple module to simulate one and two qubit circuits',
        keywords='quantum'
    )

if __name__ == '__main__':
    main()