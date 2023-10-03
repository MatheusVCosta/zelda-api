from fastapi import APIRouter

from app.config.config import get_settings

router = APIRouter(
    prefix="/health",
    tags=["core"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def health():
    settings = get_settings()
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.version,
        "env": settings.app_env,
    }
