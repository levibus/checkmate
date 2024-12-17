import logging
from io import BytesIO
from PIL import Image
import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="chess",
                               connection="chessimages_STORAGE") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

    # Read the blob's content as bytes
    blob_data = myblob.read()

    # Use BytesIO to treat the blob data as a file-like object
    image_bytes = BytesIO(blob_data)

    # Open the image using PIL
    image = Image.open(image_bytes)

    # Save the image as a JPEG file locally
    image.save('output_image.jpg', 'JPEG')
    logging.info(f"Image saved as 'output_image.jpg'")