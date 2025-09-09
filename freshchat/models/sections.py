from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message_part import MessagePart


T = TypeVar("T", bound="Sections")


@_attrs_define
class Sections:
    """template fragment sections

    Attributes:
        name (str):  Example: title.
        parts (list['MessagePart']):
    """

    name: str
    parts: list["MessagePart"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parts": parts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.message_part import MessagePart

        d = src_dict.copy()
        name = d.pop("name")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = MessagePart.from_dict(parts_item_data)

            parts.append(parts_item)

        sections = cls(
            name=name,
            parts=parts,
        )

        sections.additional_properties = d
        return sections

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
