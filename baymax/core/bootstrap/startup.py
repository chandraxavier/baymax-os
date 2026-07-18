from baymax.core.voice.session import VoiceSession

def startup():
    voice = VoiceSession()
    voice.startup()
    return voice

if __name__ == "__main__":
    startup()
