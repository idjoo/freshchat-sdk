from enum import Enum


class TemplateContentType(str, Enum):
    CAROUSEL = "carousel"
    CAROUSEL_CARD_DEFAULT = "carousel_card_default"
    QUICK_REPLY_DROPDOWN = "quick_reply_dropdown"

    def __str__(self) -> str:
        return str(self.value)
