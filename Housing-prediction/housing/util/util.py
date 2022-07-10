from housing.exception import HousingException
import yaml 
import os,sys

def read_yaml_file(file_path:str)->dict:

    try:
        with open(file_path,'rb') as yaml_file:
            return yaml_file.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e

