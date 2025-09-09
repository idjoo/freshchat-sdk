from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value_pair import KeyValuePair


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """Filters applied to obtain result

    Attributes:
        metric_filters (Union[Unset, list['KeyValuePair']]):
    """

    metric_filters: Union[Unset, list["KeyValuePair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metric_filters, Unset):
            metric_filters = []
            for metric_filters_item_data in self.metric_filters:
                metric_filters_item = metric_filters_item_data.to_dict()
                metric_filters.append(metric_filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric_filters is not UNSET:
            field_dict["metric_filters"] = metric_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.key_value_pair import KeyValuePair

        d = src_dict.copy()
        metric_filters = []
        _metric_filters = d.pop("metric_filters", UNSET)
        for metric_filters_item_data in _metric_filters or []:
            metric_filters_item = KeyValuePair.from_dict(metric_filters_item_data)

            metric_filters.append(metric_filters_item)

        filter_ = cls(
            metric_filters=metric_filters,
        )

        filter_.additional_properties = d
        return filter_

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
