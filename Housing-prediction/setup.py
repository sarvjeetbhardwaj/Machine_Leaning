from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open('./requirements.txt') as f:
        return f.readlines()


setup(
name = 'housing-predictor',
version = '0.1',
author = 'sarvjeet_bhardwaj',
description = 'This is house prediction project regression problem',
packages = find_packages(), #### will refer to folders containing __init__.py adn install the packages apart from the ones mentioned in requirements.txt
install_requires = get_requirements_list()

)