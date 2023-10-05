from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/project-jiogamesnow-nonprod-394d3b1e638e.json'

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print(f"Blob {blob_name} deleted.")

# Replace 'my-bucket' and 'my-file.txt' with your bucket name and file name
delete_blob('jio-events', 'jpeg/wedding-image1.jpg')
