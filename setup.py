from setuptools import setup, find_packages

VERSION = "0.0.1"

classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 3 - Alpha"
]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pycongress',
    version=VERSION,
    packages=find_packages(),
    description="Python client for Congress.gov's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="harrison kirk",
    author_email="harrison@hawkirk.com",
    url="https://github.com/hawkirk/PyCongress",
    license='MIT',
    classifiers=classifiers
)
