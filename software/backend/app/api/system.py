from fastapi import APIRouter
from app.services.system_service import SystemService
router=APIRouter(tags=["System"])
@router.get("/api/v1/health")
def health(): return {"status":"ok"}
@router.get("/api/v1/system")
def system_status(): return SystemService.status()
@router.get("/api/v1/system/info")
def system_info(): return SystemService.info()
