from enum import Enum


class UrlButtonPartTarget(str, Enum):
    VALUE_0 = "_self"
    VALUE_1 = "_blank"

    def __str__(self) -> str:
        return str(self.value)
