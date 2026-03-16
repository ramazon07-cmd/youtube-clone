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
    
def _get_watermark_transformation(username: str) -> str:
    return (
        "l-text,"
        f"i-{username},"
        "lfo-bottom_left,"
        "lx-10,ly-10," 
        "fs-16,"
        "co-FFFFFF,"
        "bg-00000060,"
        "pa-4_8,"
        "l-end"       
    )
    
def get_optimized_video_url(base_url:str) -> str:
    if "?" in base_url:
        return f"{base_url}&tr=q-50,f-auto"
    return f"{base_url}&tr=q-50,f-auto"
    
def get_streaming_url(base_url:str)->str:
    return f"{base_url}/ik-master.m3u8?tr=sr-480_720_1080"
    
def get_thumbnail_url(base_url:str, width:int=480, height:int=270, username:str=None)->str:
    transformations = "".join(_get_watermark_transformation(username))
    return f"{base_url}/ik-thumbnail.jpg?tr={transformations}"
  
def add_image_watermark(base_url:str, username:str=None)->str:
    transformations = "".join(_get_watermark_transformation(username))
    return f"{base_url}?tr={transformations}"  


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
    
def delete_video(file_id: str, thumbnail_file_id: str = None) -> bool:
    client = get_imagekit_client()
    try:
        client.delete_file(file_id=file_id)
        if thumbnail_file_id: 
            client.delete_file(file_id=thumbnail_file_id)
        return True
    except Exception as e:
        print(f"Delete failed: {e}")
        return False
    
    
    
    
    
    