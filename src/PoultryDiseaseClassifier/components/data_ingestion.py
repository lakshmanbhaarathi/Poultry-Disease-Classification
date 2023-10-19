import os
import zipfile
import requests
from io import BytesIO
from pathlib import Path
import urllib.request as request

# user-defined modules
from PoultryDiseaseClassifier import logger
from PoultryDiseaseClassifier.utils.general_utils import get_size
from PoultryDiseaseClassifier.entity.config_entity import DataIngestionConfig






"""
# Replace the following variables with your GitHub information
github_username = "lakshmanbhaarathi"
repository_name = "Poultry-Disease-Classification"
branch_name = "main"
file_path = "data.zip"

# Construct the URL
url = f"https://github.com/{github_username}/{repository_name}/raw/{branch_name}/{file_path}
# Make a request to download the file
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Unzip the downloaded content
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        # Specify the directory where you want to extract the contents
        extract_path = "path/to/extract"
        z.extractall(extract_path)
        
    print("File downloaded and extracted successfully!")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
"""

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_file(self,):

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url
                , filename=self.config.local_data_file
            )
            logger.info(msg=f"File {filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(msg=f"File already exists of size: {get_size(self.config.local_data_file)}") 
            
    
    def extract_zip_file(self,):
        unzip_path = self.config.unzip_dir
        os.makedirs(name=unzip_path, exist_ok=True)
        with zipfile.ZipFile(file=self.config.local_data_file, mode="r") as zip_ref:
            zip_ref.extractall(path=unzip_path)

            