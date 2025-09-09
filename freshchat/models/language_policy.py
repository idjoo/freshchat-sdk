from enum import Enum


class LanguagePolicy(str, Enum):
    DETERMINISTIC = "deterministic"

    def __str__(self) -> str:
        return str(self.value)
