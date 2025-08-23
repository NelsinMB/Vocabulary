import Prototype.learning.IO.IOInterface as IOInterface

class ConsoleIO(IOInterface):
    def output(self, msg: str) -> None:
        print(msg)
        
    def input(self, prompt: str) -> str:
        return input(prompt)