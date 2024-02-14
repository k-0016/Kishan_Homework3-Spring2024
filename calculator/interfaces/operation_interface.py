from abc import ABC, abstractmethod

class OperationInterface(ABC):
    @abstractmethod
    def perform(self, a: float, b: float) -> float:
        pass
