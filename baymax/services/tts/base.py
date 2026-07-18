from abc import ABC, abstractmethod

class BaseTTSEngine(ABC):
    @abstractmethod
    def speak(self, text: str):
        pass
