from azure.storage.blob import BlobServiceClient

# Replace these values with your storage account information
CONTAINER_NAME = "chess"
BLOB_NAME = "new_blob.jpeg"
IMAGE_PATH = "pookie.jpeg"

def upload_image_to_blob():
    try:
        # Initialize the BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string("chessimages_STORAGE")

        # Get a BlobClient to interact with the blob
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        # Open the image file in binary mode and upload it
        with open(IMAGE_PATH, "rb") as image_file:
            blob_client.upload_blob(image_file, overwrite=True)
        
        print(f"Image successfully uploaded to Blob Storage at: {blob_client.url}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
upload_image_to_blob()
