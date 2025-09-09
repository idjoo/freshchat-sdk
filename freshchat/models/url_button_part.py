from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.url_button_part_target import UrlButtonPartTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlButtonPart")


@_attrs_define
class UrlButtonPart:
    """url button part

    Attributes:
        label (str): label Example: string.
        url (str): url Example: string.
        target (Union[Unset, UrlButtonPartTarget]): target Example: _self.
    """

    label: str
    url: str
    target: Union[Unset, UrlButtonPartTarget] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        url = self.url

        target: Union[Unset, str] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "url": url,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        url = d.pop("url")

        _target = d.pop("target", UNSET)
        target: Union[Unset, UrlButtonPartTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = UrlButtonPartTarget(_target)

        url_button_part = cls(
            label=label,
            url=url,
            target=target,
        )

        url_button_part.additional_properties = d
        return url_button_part

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
