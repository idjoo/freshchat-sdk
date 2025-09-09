from enum import Enum


class ReportsApiRequestAggregator(str, Enum):
    AVG = "avg"
    MEDIAN = "median"
    P90 = "p90"

    def __str__(self) -> str:
        return str(self.value)
