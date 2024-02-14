from typing import List, Optional
from calculator.models.calculation import Calculation
from dataclasses import dataclass

@dataclass
class CalculationHistoryEntry:  # Nest a data class
   calculation: Calculation 

class CalculationHistory:
    _history: List[CalculationHistoryEntry] = [] 

    @classmethod
    def add_calculation(cls, operation: str, operands: tuple, result: float) -> None:
        calculation = Calculation(operation, operands, result)
        entry = CalculationHistoryEntry(calculation)
        cls._history.append(entry)

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        if cls._history:
            return cls._history[-1].calculation  # Access calculation within entry
        return None

    @classmethod
    def clear_history(cls) -> None:
        cls._history.clear()

    @classmethod
    def get_all(cls) -> List[Calculation]:  # Add method to get full history
       return [entry.calculation for entry in cls._history]
