from enum import Enum


class ReportsApiRequestName(str, Enum):
    HELPDESK = "helpdesk"
    TEAM_PERFORMANCE = "team_performance"

    def __str__(self) -> str:
        return str(self.value)
