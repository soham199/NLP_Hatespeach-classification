import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="hate"

list_of_files=[
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",    
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",    
    f"{project_name}/constants/__init__.py",    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",    
    f"{project_name}/pipeline/prediction_pipeline.py", 
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",  
    "app.py"
    "demo.py"
    "requirements.txt" ,
    "Dockerfile",
    "setup.py",
    ".dockerignore"   
    
    
]

for i in list_of_files:
    i=Path(i)
    
    filedir,filename=os.path.split(i)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating dictonaty; {filedir} for the file {filename}")
        
    if(not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open(i,"w") as f:
            pass
            logging.info(f"Creating Empty files:{i}")
            
    else:
        logging.info(f"{filename} is already exisst")
        
        
        
        