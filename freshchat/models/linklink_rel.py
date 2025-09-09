from enum import Enum


class LinklinkRel(str, Enum):
    AGENT = "agent"
    GROUP = "group"
    MESSAGE = "message"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
