# import packages
from google.cloud import storage
import os, datetime

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/project-jiogamesnow-nonprod-394d3b1e638e.json'

# define function that uploads a file from the bucket
def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    url = blob.generate_signed_url(
        # This URL will be valid for 1 hour
        expiration=datetime.timedelta(hours=1),
        # Allow GET requests using this URL
        method='GET'
    )

    return url

print(upload_cs_file('jio-events', '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/pexels-emma-bauso-3585798.jpg', 'jpeg/wedding-image1.jpg'))