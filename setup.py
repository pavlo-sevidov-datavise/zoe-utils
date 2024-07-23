from setuptools import setup, find_packages

setup(
    name='zoe-utils',
    version='0.1.0',
    author='Pavlo Sevidov',
    author_email='pavlo.sevidov@datavise.ai',
    description='A Zeo utility library for working with Prefect',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pavlo-sevidov-datavise/zoe-utils',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)