from PoultryDiseaseClassifier import logger
from PoultryDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(msg=f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(msg=f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    #logger.info(e)
    raise e
