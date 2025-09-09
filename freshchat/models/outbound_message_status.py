from enum import Enum


class OutboundMessageStatus(str, Enum):
    ACCEPTED = "Accepted"
    DELIVERED = "Delivered"
    FAILED = "Failed"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
