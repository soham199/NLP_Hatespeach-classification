from hate.logger import logging
from hate.configuration.gcloud_syncer import GCloudSync

obj=GCloudSync()

obj.sync_folder_from_gcloud("hate-speech-classigication-2024","dataset.zip","download/dataset.zip")



