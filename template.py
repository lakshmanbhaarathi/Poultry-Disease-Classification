import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format=f'[%(asctime)s] --%(message)s')


project_name = "PoultryDiseaseClassifier"

file_paths = [
    "__init__.py"
    , ".github/workflows/.gitkeep"
    , f"src/{project_name}/__init__.py"
    , f"src/{project_name}/components/__init__.py"
    , f"src/{project_name}/utils/__init__.py"
    , f"src/{project_name}/config/__init__.py"
    , f"src/{project_name}/config/configuration.py"
    , f"src/{project_name}/pipeline/__init__.py"
    , f"src/{project_name}/entity/__init__.py"
    , f"src/{project_name}/entity/config_entity.py"
    , f"src/{project_name}/entity/artifact_entity.py"
    , f"src/{project_name}/constants/__init__.py"
    , "config/config.yaml"
    , "dvc.yaml"
    , "params.yaml"
    , "requirements.txt"
    , "setup.py"
    , "research/trials.ipynb"
    , "templates/index.html"
]

for file_path in file_paths:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if not os.path.exists(file_path):              # check if the file exists
        if file_dir:                               # if there is no directory the Path will be ""
            os.makedirs(file_dir, exist_ok=True)   # create folder
            logging.info(f"Creating directory: {file_dir} for file: {file_name}")

        with open(file=file_path, mode="w") as f:    # create an empty file              
            logging.info(f"Creating empty file: {file_name}")

    else:
        logging.info(f"{file_name} already exists!")