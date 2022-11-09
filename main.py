# from sensor.exception import SensorException
# import sys,os
# from sensor.logger import logging


# def test_exception():
#     try:
#         logging.info("We are trying to divide by 0")
#         x=1/0
#     except Exception as e:
#         raise SensorException(e,sys)


# if __name__ == '__main__':
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)


# from sensor.configuration.mongo_db_connection import MongoDBClient

# if __name__ == '__main__':

#     mongodb=MongoDBClient()
#     print(mongodb)
#     print("collection name",mongodb.database.list_collection_names())

    
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig  


if __name__ == "__main__":

    training_pipeline_config=TrainingPipelineConfig()
    data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingestion_config.__dict__)

