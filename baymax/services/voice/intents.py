from enum import Enum
class Intent(str,Enum):
    GREETING="greeting"
    VEHICLE_COOLANT="vehicle.coolant"
    VEHICLE_RPM="vehicle.rpm"
    VEHICLE_SPEED="vehicle.speed"
    AUDIO_VOLUME="audio.volume"
    AI="ai"
