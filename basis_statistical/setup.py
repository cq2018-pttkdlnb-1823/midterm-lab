from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='basis-statistical',
    version='0.1.0',
    description='asic Statistical',
    long_description=readme,
    author='DNNs',
    author_email='lenam.fithcmus@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)