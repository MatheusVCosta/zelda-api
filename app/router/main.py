from fastapi import FastAPI

from app.controllers.core import health_router

app = FastAPI(
    title="Balance Manager Integration",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

app.include_router(health_router)
