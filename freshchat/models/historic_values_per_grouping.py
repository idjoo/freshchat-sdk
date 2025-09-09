from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value_pair import KeyValuePair
    from ..models.values_across_time_periods import ValuesAcrossTimePeriods


T = TypeVar("T", bound="HistoricValuesPerGrouping")


@_attrs_define
class HistoricValuesPerGrouping:
    """Values for the metric over the time period requested, per grouping.

    Attributes:
        groupings (Union[Unset, list['KeyValuePair']]):
        series (Union[Unset, list['ValuesAcrossTimePeriods']]):
    """

    groupings: Union[Unset, list["KeyValuePair"]] = UNSET
    series: Union[Unset, list["ValuesAcrossTimePeriods"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groupings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groupings, Unset):
            groupings = []
            for groupings_item_data in self.groupings:
                groupings_item = groupings_item_data.to_dict()
                groupings.append(groupings_item)

        series: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.key_value_pair import KeyValuePair
        from ..models.values_across_time_periods import ValuesAcrossTimePeriods

        d = src_dict.copy()
        groupings = []
        _groupings = d.pop("groupings", UNSET)
        for groupings_item_data in _groupings or []:
            groupings_item = KeyValuePair.from_dict(groupings_item_data)

            groupings.append(groupings_item)

        series = []
        _series = d.pop("series", UNSET)
        for series_item_data in _series or []:
            series_item = ValuesAcrossTimePeriods.from_dict(series_item_data)

            series.append(series_item)

        historic_values_per_grouping = cls(
            groupings=groupings,
            series=series,
        )

        historic_values_per_grouping.additional_properties = d
        return historic_values_per_grouping

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
