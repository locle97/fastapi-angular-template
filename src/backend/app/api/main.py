from fastapi import APIRouter

from app.api.routes import items, images

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(images.router, prefix="/images", tags=["images"])
