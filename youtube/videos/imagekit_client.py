from imagekitio import ImageKit
import os
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions


def get_imagekit_client():
    return ImageKit(
        public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
        private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
        url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT")
    )    

def upload_video(file_data, file_name, folder="videos/"):
    client = get_imagekit_client()
    response = client.upload_file(
        file=file_data.read(),
        file_name=file_name,
        options=UploadFileRequestOptions(
            folder=folder,
            use_unique_file_name=True,
        )
    )
    return {
        "file_id": response.file_id,
        "url": response.response_metadata.raw["url"]
    }

def upload_thumbnail(file_data, file_name, folder="thumbnails/"):
    import base64
    if isinstance(file_data, str) and file_data.startswith("data:"):
        _, file_data = file_data.split(",", 1)
        file_data = base64.b64decode(file_data)
    
    client = get_imagekit_client()
    
    response = client.upload_file(
        file=file_data,
        file_name=file_name,
        options=UploadFileRequestOptions(
            folder=folder,
            use_unique_file_name=True,
        )
    )
    return {
        "file_id": response.file_id,
        "url": response.response_metadata.raw["url"]
    }





