from fastapi import FastAPI
import socket
import platform
import psutil

app = FastAPI(title="Baymax API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "🚗 Baymax API is running"}

@app.get("/api/v1/health")
def health():
    return {
        "status": "healthy",
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "boot_time": psutil.boot_time()
    }
