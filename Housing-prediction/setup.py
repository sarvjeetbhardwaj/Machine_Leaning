from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    with open('./requirements.txt') as f:
        return f.readlines()


setup(
name = 'housing-predictor',
version = '0.1',
author = 'sarvjeet_bhardwaj',
description = 'This is house prediction project regression problem',
packages = ['housing'],
install_requires = get_requirements_list()

)