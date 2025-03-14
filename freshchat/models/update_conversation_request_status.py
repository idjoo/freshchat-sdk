from enum import Enum


class UpdateConversationRequestStatus(str, Enum):
    ASSIGNED = "assigned"
    NEW = "new"
    REOPENED = "reopened"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
