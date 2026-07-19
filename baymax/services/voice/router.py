from __future__ import annotations
class IntentRouter:
    async def route(self,text:str):
        t=text.lower().strip()
        if any(x in t for x in ("hello","hi","hey")):
            return {"intent":"greeting","response":"Hey Chandra. 😏"}
        if "coolant" in t:
            return {"intent":"vehicle.coolant","response":None}
        if "rpm" in t:
            return {"intent":"vehicle.rpm","response":"Engine is idling at 850 RPM (mock)."}
        if "speed" in t:
            return {"intent":"vehicle.speed","response":"Current speed is 0 km/h (mock)."}
        if "volume" in t:
            return {"intent":"audio.volume","response":"Volume adjusted (mock)."}
        return {"intent":"ai","response":"I don't know that one yet. I'll ask my brain later."}
