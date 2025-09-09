from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instant_value import InstantValue
    from ..models.key_value_pair import KeyValuePair


T = TypeVar("T", bound="InstantValuesPerGrouping")


@_attrs_define
class InstantValuesPerGrouping:
    """Values at the current instant for a metric per grouping

    Attributes:
        groupings (Union[Unset, list['KeyValuePair']]):
        values (Union[Unset, list['InstantValue']]):
    """

    groupings: Union[Unset, list["KeyValuePair"]] = UNSET
    values: Union[Unset, list["InstantValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groupings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groupings, Unset):
            groupings = []
            for groupings_item_data in self.groupings:
                groupings_item = groupings_item_data.to_dict()
                groupings.append(groupings_item)

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groupings is not UNSET:
            field_dict["groupings"] = groupings
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.instant_value import InstantValue
        from ..models.key_value_pair import KeyValuePair

        d = src_dict.copy()
        groupings = []
        _groupings = d.pop("groupings", UNSET)
        for groupings_item_data in _groupings or []:
            groupings_item = KeyValuePair.from_dict(groupings_item_data)

            groupings.append(groupings_item)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = InstantValue.from_dict(values_item_data)

            values.append(values_item)

        instant_values_per_grouping = cls(
            groupings=groupings,
            values=values,
        )

        instant_values_per_grouping.additional_properties = d
        return instant_values_per_grouping

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
