#user-defined modules
from PoultryDiseaseClassifier import logger
from PoultryDiseaseClassifier.config.configuration import ConfigurationManager
from PoultryDiseaseClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self,):...
    def main(self,):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config, )
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

    

if __name__=="__main__":
    try:
        logger.info(msg=f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(msg=f">>>>>> {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    