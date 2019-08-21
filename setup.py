import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="mporm",
    version="1.0.0",
    author="Leonard Mivinci XJJ",
    author_email="1366723936@qq.com",
    description="MySQL ORM in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mivinci/mporm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
