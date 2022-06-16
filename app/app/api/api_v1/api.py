from fastapi import APIRouter

from app.api.api_v1.endpoints import lookup, remove, export

api_router = APIRouter()
api_router.include_router(lookup.router, prefix="/lookup", tags=["lookup"])
api_router.include_router(remove.router, prefix="/remove", tags=["remove"])
api_router.include_router(export.router, prefix="/export", tags=["export"])