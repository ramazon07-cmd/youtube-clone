from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
import os
import base64

_client = None

def get_imagekit_client():
    global _client
    if _client is None:
        _client = ImageKit(
            public_key=os.environ.get("IMAGEKIT_PUBLIC_KEY"),
            private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
            url_endpoint=os.environ.get("IMAGEKIT_URL_ENDPOINT")
        )

    
    return _client

def upload_video(file_data: bytes, file_name: str, folder: str = "/videos/") -> dict:
    client = get_imagekit_client()
    encoded = base64.b64encode(file_data).decode("utf-8")
    response = client.upload_file(
        file=encoded,
        file_name=file_name,
        options=UploadFileRequestOptions(folder=folder)
    )
    return {"file_id": response.file_id, "url": response.url}


def upload_thumbnail(file_data: str | bytes, file_name: str, folder: str = "/thumbnails/") -> dict:
    if isinstance(file_data, str) and file_data.startswith("data:"):
        encoded = file_data.split(",", 1)[1]
    else:
        encoded = base64.b64encode(file_data).decode("utf-8")

    client = get_imagekit_client()
    response = client.upload_file(
        file=encoded,
        file_name=file_name,
        options=UploadFileRequestOptions(folder=folder)
    )
    return {"file_id": response.file_id, "url": response.url}