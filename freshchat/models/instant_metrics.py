from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.instant_values_per_grouping import InstantValuesPerGrouping


T = TypeVar("T", bound="InstantMetrics")


@_attrs_define
class InstantMetrics:
    """Instant metrics API response

    Attributes:
        data (Union[Unset, list['InstantValuesPerGrouping']]):
        filters (Union[Unset, Filter]): Filters applied to obtain result
        metric (Union[Unset, str]):  Example: team_presence.online.
    """

    data: Union[Unset, list["InstantValuesPerGrouping"]] = UNSET
    filters: Union[Unset, "Filter"] = UNSET
    metric: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        metric = self.metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if filters is not UNSET:
            field_dict["filters"] = filters
        if metric is not UNSET:
            field_dict["metric"] = metric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.instant_values_per_grouping import InstantValuesPerGrouping

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = InstantValuesPerGrouping.from_dict(data_item_data)

            data.append(data_item)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, Filter]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = Filter.from_dict(_filters)

        metric = d.pop("metric", UNSET)

        instant_metrics = cls(
            data=data,
            filters=filters,
            metric=metric,
        )

        instant_metrics.additional_properties = d
        return instant_metrics

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
