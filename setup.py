from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Binance Exchange python wrapper'
LONG_DESCRIPTION = 'Various scripts that can be used to easily interact with the Binance exchange.'

setup(
    name="Binance",
    version=VERSION,
    author="ageorge95",
    author_email="arteni.george.daniel@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"],
    extras_require={},
    keywords=['python', 'pyBinance', 'Binance']
)