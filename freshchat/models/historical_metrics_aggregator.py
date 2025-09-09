from enum import Enum


class HistoricalMetricsAggregator(str, Enum):
    AVG = "avg"
    MAX = "max"
    MEDIAN = "median"
    MIN = "min"
    VALUE_4 = "90th_percentile"

    def __str__(self) -> str:
        return str(self.value)
