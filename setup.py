from setuptools import setup

setup(
        name='hill-cipher',
        version='0.1',
        packages=['hillcipher'],
        test_suite='nose.collector',
        tests_require=['nose'],
)
