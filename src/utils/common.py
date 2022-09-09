from importlib.resources import contents
import os
import yaml
import logging
import time
import pandas as pd
import json



def read_yaml(path_to_yaml:str)->dict:
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
    logging.info(f"yaml_file:{path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directoris:list)->None:
    for path in path_to_directoris:
        os.makedirs(path,exist_ok=True)
        logging.info(f"created directory at :{path}")


def save_json(path:str,data:dict)->None:
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logging.info(f"json file saved at:{path}")




















