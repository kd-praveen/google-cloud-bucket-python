from google.cloud import storage
import requests
import zipfile
import os
from urllib.parse import urlparse
from datetime import timedelta

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/praveenkd/Documents/Docs/Project Documents/Jio-events/project-jiogamesnow-nonprod-394d3b1e638e.json'




# define function that downloads a file from the bucket
def download_zip_folder(bucket_name): 
        
    # Create a client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Get all user image URLs from database by user ID
    image_urls =  [
            {
                "id": 2,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/e252b2efc156482cbae56a45ee006f48_IMG_20220725_121107108.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/e252b2efc156482cbae56a45ee006f48_IMG_20220725_121107108_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 6,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/0ce1561d0f574c6bbd7d8188951247a6_Spider-ManIntoTheSpider-Verse1-01.jpeg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/0ce1561d0f574c6bbd7d8188951247a6_Spider-ManIntoTheSpider-Verse1-01_reduced.jpeg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 7,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/3f2ae57dff664765a75a0b18c33c7a70_Spider-ManIntoTheSpider-Verse7.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/3f2ae57dff664765a75a0b18c33c7a70_Spider-ManIntoTheSpider-Verse7_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 8,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/fd4257a4090e4bab9fc442af53cd5e20_Spider-ManIntoTheSpider-Verse1.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/fd4257a4090e4bab9fc442af53cd5e20_Spider-ManIntoTheSpider-Verse1_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 12,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/a6277532474d4a53b05306491b11414e_Spider-ManIntoTheSpider-Verse1.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/a6277532474d4a53b05306491b11414e_Spider-ManIntoTheSpider-Verse1_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 13,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/ffbcbdd63527424a9a31c1adac6419a9_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/ffbcbdd63527424a9a31c1adac6419a9_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 14,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/4cdecb12065d4151b549c0d2c17f203d_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/4cdecb12065d4151b549c0d2c17f203d_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 15,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/19f352b9ee7746db87917a275123789b_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/19f352b9ee7746db87917a275123789b_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 16,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/85b9a80186684ba6a61f79ebf181c1ea_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/85b9a80186684ba6a61f79ebf181c1ea_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 17,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/7fe27d0db91a4868ac753f466e3adf1b_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/7fe27d0db91a4868ac753f466e3adf1b_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 18,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/88293fa3fa334061ac2e1999a2d82d81_PXL_20221014_072945846.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/88293fa3fa334061ac2e1999a2d82d81_PXL_20221014_072945846_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            },
            {
                "id": 19,
                "original_image_public_path": "https://storage.googleapis.com/jio-events/event-1/8be07d656df049dda9edcb44e02b18fd_pexels-kammeran-gonzalezkeola-9638689.jpg",
                "image_path": "https://storage.googleapis.com/jio-events/event-1/8be07d656df049dda9edcb44e02b18fd_pexels-kammeran-gonzalezkeola-9638689_reduced.jpg",
                "is_public": "False",
                "role": "Guest"
            }
        ]
   
    # Create a ZipFile object
    with zipfile.ZipFile('photos.zip', 'w') as zipf:
        # Generate signed URL for each image and download it
        for image_url in image_urls:
            # Parse the URL to get the blob name
            parsed_url = urlparse(image_url["image_path"])
            blob_name = parsed_url.path.lstrip('/')
            blob_name = blob_name.split('/', 1)[1]

            
            # Generate a local file name
            local_file_name = os.path.basename(blob_name)
            
            # Get the blob and generate a signed URL
            blob = bucket.blob(blob_name)
            signed_url = blob.generate_signed_url(expiration=timedelta(minutes=15))
            # Download the image to a local file
            response = requests.get(signed_url)
            with open(local_file_name, 'wb') as f:
                f.write(response.content)
            
            # Add the local file to the zip archive
            zipf.write(local_file_name)
            
            # Delete the local file after adding it to the zip archive
            os.remove(local_file_name)


download_zip_folder('jio-events')