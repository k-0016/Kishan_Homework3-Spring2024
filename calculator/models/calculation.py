from dataclasses import dataclass  # Consider using dataclasses 

@dataclass
class Calculation:
    operation: str
    operands: tuple
    result: float

    def __repr__(self):
        return f"Calculation(operation={self.operation}, operands={self.operands}, result={self.result})"
