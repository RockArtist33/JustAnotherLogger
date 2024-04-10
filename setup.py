from setuptools import find_packages, setup

setup(
    name='simplelogger',
    packages=find_packages(include=['simplelogger']),
    version='0.0.2',
    description='My first Python library',
    author='RockArtist33',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.1.1'],
    test_suite='testsuite'
)