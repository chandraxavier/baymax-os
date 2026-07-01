from fastapi import FastAPI

from app.api.system import router as system_router
from app.core.config import ConfigLoader

config = ConfigLoader.load("system.yaml")

app = FastAPI(
    title=config["application"]["name"],
    version=config["application"]["version"]
)

app.include_router(system_router)


@app.get("/")
def root():
    return {
        "application": config["application"]["name"],
        "version": config["application"]["version"]
    }
