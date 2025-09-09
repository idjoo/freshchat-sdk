from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Thumbnail")


@_attrs_define
class Thumbnail:
    """thumbnail model

    Attributes:
        content_type (Union[Unset, str]):  Example: image/png.
        height (Union[Unset, int]):  Example: 100.
        url (Union[Unset, str]):  Example: https://chat.s3.amazonaws.com/f_marketingpicFull/u_8ace8de9b2545716308776dc1d
            f471f347f1057db625ce8ee57b713146b8023a/img_1602510533617.png.
        width (Union[Unset, int]):  Example: 200.
    """

    content_type: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        height = self.height

        url = self.url

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = d.pop("content_type", UNSET)

        height = d.pop("height", UNSET)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        thumbnail = cls(
            content_type=content_type,
            height=height,
            url=url,
            width=width,
        )

        thumbnail.additional_properties = d
        return thumbnail

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
