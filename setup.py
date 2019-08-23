from setuptools import setup, find_packages
from mporm import __version__


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="mporm",
    version=__version__,
    author="Leonard Mivinci XJJ",
    author_email="1366723936@qq.com",
    description="MySQL ORM in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mivinci/mporm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
