from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.historical_metrics_aggregator import HistoricalMetricsAggregator
from ..models.historical_metrics_interval import HistoricalMetricsInterval
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.historic_values_per_grouping import HistoricValuesPerGrouping


T = TypeVar("T", bound="HistoricalMetrics")


@_attrs_define
class HistoricalMetrics:
    """Response for historical dashboard metrics API

    Attributes:
        aggregator (Union[Unset, HistoricalMetricsAggregator]):  Example: median.
        data (Union[Unset, list['HistoricValuesPerGrouping']]):
        end (Union[Unset, str]):  Example: 2019-05-31T15:30:00.000+05:30.
        filters (Union[Unset, Filter]): Filters applied to obtain result
        interval (Union[Unset, HistoricalMetricsInterval]):  Example: 1h.
        metric (Union[Unset, list[str]]):  Example: team_performance.first_response_time.
        start (Union[Unset, str]):  Example: 2019-01-01T15:30:00.000+05:30.
    """

    aggregator: Union[Unset, HistoricalMetricsAggregator] = UNSET
    data: Union[Unset, list["HistoricValuesPerGrouping"]] = UNSET
    end: Union[Unset, str] = UNSET
    filters: Union[Unset, "Filter"] = UNSET
    interval: Union[Unset, HistoricalMetricsInterval] = UNSET
    metric: Union[Unset, list[str]] = UNSET
    start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregator: Union[Unset, str] = UNSET
        if not isinstance(self.aggregator, Unset):
            aggregator = self.aggregator.value

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        end = self.end

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        interval: Union[Unset, str] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.value

        metric: Union[Unset, list[str]] = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregator is not UNSET:
            field_dict["aggregator"] = aggregator
        if data is not UNSET:
            field_dict["data"] = data
        if end is not UNSET:
            field_dict["end"] = end
        if filters is not UNSET:
            field_dict["filters"] = filters
        if interval is not UNSET:
            field_dict["interval"] = interval
        if metric is not UNSET:
            field_dict["metric"] = metric
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.historic_values_per_grouping import HistoricValuesPerGrouping

        d = src_dict.copy()
        _aggregator = d.pop("aggregator", UNSET)
        aggregator: Union[Unset, HistoricalMetricsAggregator]
        if isinstance(_aggregator, Unset):
            aggregator = UNSET
        else:
            aggregator = HistoricalMetricsAggregator(_aggregator)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = HistoricValuesPerGrouping.from_dict(data_item_data)

            data.append(data_item)

        end = d.pop("end", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, Filter]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = Filter.from_dict(_filters)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, HistoricalMetricsInterval]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = HistoricalMetricsInterval(_interval)

        metric = cast(list[str], d.pop("metric", UNSET))

        start = d.pop("start", UNSET)

        historical_metrics = cls(
            aggregator=aggregator,
            data=data,
            end=end,
            filters=filters,
            interval=interval,
            metric=metric,
            start=start,
        )

        historical_metrics.additional_properties = d
        return historical_metrics

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
