from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resources import Resources


T = TypeVar("T", bound="InstantValue")


@_attrs_define
class InstantValue:
    """Values for a given metric, will include count and reference to the resources based on the request

    Attributes:
        count (Union[Unset, int]):  Example: 23.
        key (Union[Unset, str]):  Example: team_member.online.
        resources (Union[Unset, list['Resources']]):
    """

    count: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    resources: Union[Unset, list["Resources"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        key = self.key

        resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if key is not UNSET:
            field_dict["key"] = key
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.resources import Resources

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        key = d.pop("key", UNSET)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resources.from_dict(resources_item_data)

            resources.append(resources_item)

        instant_value = cls(
            count=count,
            key=key,
            resources=resources,
        )

        instant_value.additional_properties = d
        return instant_value

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
