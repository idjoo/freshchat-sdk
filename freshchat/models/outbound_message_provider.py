from enum import Enum


class OutboundMessageProvider(str, Enum):
    WHATSAPP = "whatsapp"

    def __str__(self) -> str:
        return str(self.value)
