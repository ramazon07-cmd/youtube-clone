import os
from imagekitio import ImageKit

def get_imagekit_client():
    return ImageKit()

def upload_video(file_data:bytes, file_name:str, folder:str='videos/') -> dict:
    public_key = os.getenv('IMAGEKIT_PUBLIC_KEY')

    client = get_imagekit_client()

    response = client.files.upload(
        file=file_data,
        file_name=file_name,
        folder=folder,
        options={
            "useUniqueFileName": True,
            "responseFields": ["url", "fileId"]
        }
    )
    
    return {
        "file_id": response.fileId,
        "url": response.url
    }


def upload_thumbnail(file_data:bytes, file_name:str, folder:str='thumbnails/') -> dict:
    import base64
    public_key = os.getenv('IMAGEKIT_PUBLIC_KEY')

    if file_data.startswith('data:'):
        header, file_data = file_data.split(',', 1)
        file_data = base64.b64decode(file_data)
    else:
        file_data = file_data.encode()

    client = get_imagekit_client()

    response = client.files.upload(
        file=file_data,
        file_name=file_name,
        folder=folder,
        options={
            "useUniqueFileName": True,
            "responseFields": ["url", "fileId"]
        }
    )

    return {
        "file_id": response.fileId,
        "url": response.url
    }














