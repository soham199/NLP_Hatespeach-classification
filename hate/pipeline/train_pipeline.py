import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.components.data_ingestion import DataIngestion
from hate.entity.config_entity import (dataingestionconfig)
from hate.entity.artifact_entity import (DataIngestionArtifacts)

class TrainPipeline:
    
    def __init__(self):
        self.data_ingestion_config=dataingestionconfig()
        
        
    def start_data_ingestion(self)->DataIngestionArtifacts:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def run_pipeline(self):
        logging.info("Pipeline Strted")
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        
        
        except Exception as e:
            raise CustomException(e,sys) from e
        
        

  
    
    


