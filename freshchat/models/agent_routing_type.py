from enum import Enum


class AgentRoutingType(str, Enum):
    DISABLED = "DISABLED"
    INTELLIASSIGN = "INTELLIASSIGN"
    OCR = "OCR"

    def __str__(self) -> str:
        return str(self.value)
