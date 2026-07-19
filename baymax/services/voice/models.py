from dataclasses import dataclass
@dataclass(slots=True)
class VoiceRequest:
    text:str
@dataclass(slots=True)
class VoiceResponse:
    intent:str
    response:str
