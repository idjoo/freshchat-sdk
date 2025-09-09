from enum import Enum


class ErrorStatus(str, Enum):
    AGENT_NOT_FOUND = "AGENT_NOT_FOUND"
    WRONG_PAGE = "WRONG_PAGE"

    def __str__(self) -> str:
        return str(self.value)
