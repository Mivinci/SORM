from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='tsorm',
    version='0.2.3',
    author='Leonard Mivinci',
    author_email='1366723936@qq.com',
    description='Provide simple ORM APIs for Python project',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Mivinci/tsorm',
    install_requires=[
        'PyMySQL==0.9.2',
    ],
    packages=find_packages(),
    license='MIT',
)
