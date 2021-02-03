#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Tr4PrFnPredLib',
      version='0.0.2',
      description='Library for protein function prediction models',
      author='Tr4FnPr',
      author_email='derekshao@cmail.carleton.ca',
      packages=find_packages(),
      install_requires=[
            'tensorflow-gpu',
            'torch',
            'pandas',
            'aiofiles',
            'redis'
      ]
    )
