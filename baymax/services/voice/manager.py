from __future__ import annotations
from baymax.services.voice.router import IntentRouter
from baymax.services.personality.tinker import TinkerPersonality
class VoiceManager:
    def __init__(self, context):
        self.context=context
        self.router=IntentRouter()
        self.personality=TinkerPersonality()
        self.running=False
    async def start(self):
        self.running=True
    async def stop(self):
        self.running=False
    async def health(self):
        return {"status":"healthy" if self.running else "stopped"}
    async def process(self,text:str):
        result=await self.router.route(text)
        if result["intent"].startswith("vehicle."):
            vehicle=self.context.service_manager.registry.get("vehicle")
            result["vehicle_status"]=await vehicle.status()
            if result["intent"]=="vehicle.coolant":
                temp=result["vehicle_status"]["telemetry"].coolant_temperature
                result["response"]=f"Coolant temperature is {temp}°C." if temp is not None else "I can not see the coolant temperature yet, Chandra. The vehicle link is offline."
        return self.personality.respond(result)
