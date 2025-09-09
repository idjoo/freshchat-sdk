from enum import Enum


class ErrorMessage(str, Enum):
    THE_PAGE_DOES_NOT_EXIST_IN_THE_SEARCH_RESULT = "The page does not exist in the search result"
    THIS_AGENT_DOES_NOT_EXIST = "This agent does not exist"

    def __str__(self) -> str:
        return str(self.value)
