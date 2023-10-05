from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/project-jiogamesnow-nonprod-394d3b1e638e.json'

def delete_folder(bucket_name, folder_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    
    # List all objects in the folder
    blobs = bucket.list_blobs(prefix=folder_name)
    
    print(blobs)
    
    # Delete each object in the folder
    for blob in blobs:
        blob.delete()

    print(f"Folder {folder_name} deleted.")
    
delete_folder('jio-events', 'events-1')
