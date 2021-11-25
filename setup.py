from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages= find_packages(exclude=['tests*']),
    license= 'MIT',
    description= 'Lekes EDSA example on python packages',
    long_description= open('README.md').read(),
    install_requires= ["numpy"],
    url='',
    author='Oluwaleke Oni',
    author_email='oluwalekeoni@gmail.com'
)
