from setuptools import setup, find_packages

setup(
    name='interface-mysql',
    packages=find_packages(include=['interface_mysql']),
    version='0.0.1',
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[],
)
