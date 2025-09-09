from enum import Enum


class HistoricalMetricsInterval(str, Enum):
    VALUE_0 = "1m"
    VALUE_1 = "5m"
    VALUE_2 = "15m"
    VALUE_3 = "30m"
    VALUE_4 = "1h"
    VALUE_5 = "1d"
    VALUE_6 = "1W"
    VALUE_7 = "1M"

    def __str__(self) -> str:
        return str(self.value)
