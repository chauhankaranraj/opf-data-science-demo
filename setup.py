"""Package manifest for this template repo."""

from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="src",
    packages=find_packages(),
    version=__version__,
    description="Demo project to show how to easily and automatically containerize a GitHub repo and share it on JupyterHub using Thoth tools",
    author="chauhankaranraj",
    license="MIT",
)
