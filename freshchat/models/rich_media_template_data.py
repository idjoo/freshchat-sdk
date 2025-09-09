from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body import Body
    from ..models.header import Header


T = TypeVar("T", bound="RichMediaTemplateData")


@_attrs_define
class RichMediaTemplateData:
    """for rich media contents

    Attributes:
        body (Union[Unset, Body]): body for components
        header (Union[Unset, Header]): header for components
    """

    body: Union[Unset, "Body"] = UNSET
    header: Union[Unset, "Header"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        header: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.body import Body
        from ..models.header import Header

        d = src_dict.copy()
        _body = d.pop("body", UNSET)
        body: Union[Unset, Body]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = Body.from_dict(_body)

        _header = d.pop("header", UNSET)
        header: Union[Unset, Header]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = Header.from_dict(_header)

        rich_media_template_data = cls(
            body=body,
            header=header,
        )

        rich_media_template_data.additional_properties = d
        return rich_media_template_data

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
