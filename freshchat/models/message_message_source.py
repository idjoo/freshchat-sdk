from enum import Enum


class MessageMessageSource(str, Enum):
    API = "API"
    FB_MESSENGER = "FB_MESSENGER"
    FB_NATIVE = "FB_NATIVE"
    FRESHDESK = "FRESHDESK"
    INVALID = "INVALID"
    MOBILE = "MOBILE"
    SMOOCH = "SMOOCH"
    SYSTEM = "SYSTEM"
    WEB = "WEB"
    ZENDESK = "ZENDESK"

    def __str__(self) -> str:
        return str(self.value)
