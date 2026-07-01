from fastapi import APIRouter
from app.services.system_service import SystemService

router = APIRouter(prefix="/api/v1/system", tags=["System"])


@router.get("")
def system_status():
    return SystemService.status()
