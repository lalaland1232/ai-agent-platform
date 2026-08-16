from abc import ABC, abstractmethod
class AI(ABC):
    @abstractmethod
    def generate_response(self, prompt: str, input_data: dict) -> str:
        pass
