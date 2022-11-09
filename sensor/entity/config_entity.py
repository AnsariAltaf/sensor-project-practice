from datetime import datetime
from sensor.constant import training_pipeline
import os 

'''
We are noting the time beacuse whenevr the code will be run
,a folder by the name of current timestamp will be created under Artifacts directory
and this folder will contain data ingestion and data validation.
this will help in maintaining the vresions of our pipeline.
Again if wew run the pipeline then again one more folder will be created of the current timestamp 
and it will contain data ingestion and data validation.
'''
class TrainingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_dir=os.path.join(training_pipeline.ARTIFACT_DIR,timestamp)
        self.timestamp=timestamp


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)
        self.training_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.testing_file_path=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME



