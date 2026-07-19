class WakeWordDetector:
    def detect(self,text:str)->bool:
        t=text.lower()
        return "hey tinker" in t or "tinker" in t
