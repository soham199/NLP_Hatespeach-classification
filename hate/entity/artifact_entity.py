from dataclasses import dataclass
from hate.constants import *
import os

@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str