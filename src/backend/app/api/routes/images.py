from pathlib import Path

from fastapi.responses import FileResponse
from fastapi import APIRouter

from app.core.config import settings

ASSETS_DIR = settings.ASSETS_DIR

router = APIRouter()


@router.get("")
async def get_sample_image():
    image_url = ASSETS_DIR + "sample.jpg"
    image_path = Path(image_url)

    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
