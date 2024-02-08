from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wip_forms/__init__.py
from wip_forms import __version__ as version

setup(
	name="wip_forms",
	version=version,
	description="Tasks assigned by Gupteshwer Sir",
	author="Dharmaraj",
	author_email="dharmaraj.b@indictranstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
