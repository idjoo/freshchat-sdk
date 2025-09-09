from enum import Enum


class ReportsResponseV2Status(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
