from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in suncycle/__init__.py
from suncycle import __version__ as version

setup(
	name="suncycle",
	version=version,
	description="Translation Of Item",
	author="Akhilaminc",
	author_email="vivekthakor1690@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
