import os
from zipfile import ZipFile
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync
from hate.entity.config_entity import dataingestionconfig
from hate.entity.artifact_entity import DataIngestionArtifacts
import sys


class DataIngestion:
    def __init__(self, data_ingestion_config: dataingestionconfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud=GCloudSync()
        
        
    def get_def_data_from_gcloud(self) ->None:
        try:
            logging.info("Entered the get_def_data_from_gcloud method ")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACT_DIR, exist_ok=True)
            
            self.gcloud.sync_folder_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
                                                self.data_ingestion_config.ZIP_FILE_NAME,
                                                self.data_ingestion_config.DATA_INGESTION_ARTIFACT_DIR,
                                                )
            
            logging.info("Exited the data ingestion class")
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def unzip_and_clean(self):
        logging.info("Entered the unzip method")                
            
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)
                
                return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
            
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
    def initiate_data_ingestion(self)->DataIngestionArtifacts:
        logging.info("Data ingestion started")
        
        try:
            self.get_def_data_from_gcloud()
            imbalance_data_file_path,raw_data_file_path=self.unzip_and_clean()
            
            data_ingestion_artifact=DataIngestionArtifacts(
                imbalance_data_file_path=imbalance_data_file_path,
                raw_data_file_path=raw_data_file_path)
            
            
            return data_ingestion_artifact
            
            
        
        except Exception as e:
            raise CustomException(e,sys) from e
                        
            
