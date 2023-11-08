from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/project-jiogamesnow-nonprod-394d3b1e638e.json'


def check_folder_size(bucket_name, prefix):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    
    folder_size = 0
    for blob in blobs:
        folder_size += blob.size  # size in bytes
    
    folder_size_gb = folder_size / (1024 ** 3)  # size in GB
    return folder_size_gb

# usage
bucket_name = 'jio-events'
event_id = '2'
folder_size_gb = check_folder_size(bucket_name, f'event-{event_id}/')

print(f'The size of the folder events-{event_id} is {folder_size_gb} GB.')
