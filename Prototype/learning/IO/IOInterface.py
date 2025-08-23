from abc import ABC, abstractmethod

class IOInteface(ABC):
    
    @abstractmethod
    def output(self, msg: str) -> None:
        pass
    
    @abstractmethod
    def input(self, prompt: str) -> None:
        pass
        
