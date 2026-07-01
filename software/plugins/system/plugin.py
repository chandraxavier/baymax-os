import socket
import time
import psutil


class SystemPlugin:

    @staticmethod
    def get_status():
        return {
            "hostname": socket.gethostname(),
            "cpu": psutil.cpu_percent(interval=0.2),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent,
            "boot_time": int(psutil.boot_time()),
            "uptime_seconds": int(time.time() - psutil.boot_time())
        }
