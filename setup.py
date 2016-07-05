from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development",
]

setup(
    author="David Whale",
    name='energenie',
    version="1",
    description='A python interface to the Energenie line of products',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/whaleygeek/pyenergenie',
    packages=find_packages(exclude=['*.pyc']),
    package_data={'': ['drv/*']},
    include_package_data=True,
    zip_safe = False,
    license='MIT License',
    platforms=['Raspberry Pi'],
    classifiers=CLASSIFIERS,
    install_requires=[],
)
