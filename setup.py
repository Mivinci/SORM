from setuptools import setup


with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='TSORM',
    version='0.1.0',
    author='Leonard Mivinci',
    author_email='1366723936@qq.com',
    description='Provide simple ORM APIs for Python project',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Mivinci/SORM',
    install_requires=[
        'PyMySQL==0.9.2',
    ],
    packages=['SORM'],
    license='MIT',
)
