import os
import yaml
import json
import joblib
import base64
from typing import Any,List
from pathlib import Path
from box import ConfigBox     # helps converting dict object to config box
from ensure import ensure_annotations
from box.exceptions import BoxValueError

# user-defined modules
from PoultryDiseaseClassifier import logger


@ensure_annotations
def read_yaml(yaml_file_path:Path)->ConfigBox:
    """
    Description: 
        Reads yaml file
    Args:
        yaml_file_path(str): Path like input

    Raises:
        ValueError: If yaml file is empty
        e: Empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(file=yaml_file_path) as yaml_file:
            content = yaml.safe_load(stream=yaml_file)
            logger.info(msg=f"Yaml file: {yaml_file_path} read succesfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty!")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:List, verbose=True):
    """
    Description:
        Create directories from the list.

    Args:
        path_to_directories: List of paths to directories.
        verbose: default=True, ignore if multiple directories to be created.
    """

    for path in path_to_directories:
        os.makedirs(name=path, exist_ok=True)
        if verbose:
            logger.info(msg=f"Created directory at: {path}")


@ensure_annotations
def save_json(file_path:Path, data:dict):
    """
    Description:
        Saves json data to the given path
    Args:
        file_path (Path): Path to json file
        data (dict): JSON data to be saved in file
    """
    with open(file=file_path, mode="w") as f:
        json.dump(obj=data, fp=f, indent=4)
    logger.info(msg=f"JSON file saved succesfully at: {path}")


@ensure_annotations
def load_json(file_path:Path) ->ConfigBox:
    """
    Description: 
        Loads JSON files from the path
    Args:
        file_path (Path): Path to JSON file
    Returns:
        ConfigBox: Data as class attributes instead of dictionary.

    """
    with open(file=file_path) as f:
        data = json.load(fp=f)
    
    logger.info(msg=f"JSON data loaded succesfully from file: {path}")

    return ConfigBox(data)

@ensure_annotations
def save_binary(data:Any, file_path:Path):
    """
    Description:
        Save data as binary file
    Args:
        data (Any): Data to be saved as binary
        file_path (Path): Path to binary file
    """
    joblib.dump(value=data, filename=file_path)

    logger.info(msg=f"Data saved successfully as binary file at: {file_path}")


@ensure_annotations
def load_binary(file_path:Path)->Any:
    """
    Description:
        Load binary data from the given file path
    
    Args:
        path (Path): Path to binary file
    
    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(filename=file_path)
    logger.info(msg=f"Binary file loaded successfully from: {file_path}")

    return(data)

@ensure_annotations
def get_size(file_path:Path) ->str:
    """
    Description:
         Get file size in mb.
    Args:
        file_path (Path): File path
    
        Returns:
            str: Size in mb
    """
    file_size = round(os.path.getsize(filename=file_path)/1024)

    return(f"File size ~ {file_size}")

@ensure_annotations
def decode_image(imgstring:str, file_path:Path):
    """
    Description: Decode image from the image string to the given file path.
    Args:
        imgstring (str): Image string to be decoded
        file_path (Path): File path to save the image.
    """
    imgdata = base64.b64decode(s=imgstring)
    with open(file=file_path, mode="wb") as f:
        f.write(__buffer=imgdata)
        f.close()
    logger.info(msg=f"The image {imgstring} has been succesfully decoded into file: {file_path}")

@ensure_annotations
def enceode_image(img_path:Path):
    with open(file=img_path, mode="rb") as f:
        return base64.b64encode(f.read())
    
