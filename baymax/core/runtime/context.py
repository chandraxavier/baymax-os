from baymax.core.voice.session import VoiceSession
from baymax.core.events.bus import EventBus

class RuntimeContext:
    def __init__(self):
        self.bus = EventBus()
        self.voice = VoiceSession()
