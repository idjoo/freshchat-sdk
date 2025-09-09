from enum import Enum


class ReportsLinkStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
