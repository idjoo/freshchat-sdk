from enum import Enum


class MessageMessageType(str, Enum):
    NORMAL = "normal"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
