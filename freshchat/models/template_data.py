from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateData")


@_attrs_define
class TemplateData:
    """template data

    Attributes:
        data (str): data Example: Arya Stark.
        instance (Union[Unset, TemplateData]): template data
    """

    data: str
    instance: Union[Unset, "TemplateData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data")

        _instance = d.pop("instance", UNSET)
        instance: Union[Unset, TemplateData]
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = TemplateData.from_dict(_instance)

        template_data = cls(
            data=data,
            instance=instance,
        )

        template_data.additional_properties = d
        return template_data

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
