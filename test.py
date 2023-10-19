from src.PoultryDiseaseClassifier.utils.general_utils import read_yaml
from pathlib import Path



yaml_file_path = "E:\projects\poultry_disease_classification\Poultry-Disease-Classification\config\config.yaml"\

yaml_file_path = Path(yaml_file_path)

data = read_yaml(yaml_file_path=yaml_file_path)
print(data)