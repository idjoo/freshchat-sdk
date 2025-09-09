from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message_part import MessagePart


T = TypeVar("T", bound="CollectionPart")


@_attrs_define
class CollectionPart:
    """collection part

    Attributes:
        sub_parts (list['MessagePart']):
    """

    sub_parts: list["MessagePart"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_parts = []
        for sub_parts_item_data in self.sub_parts:
            sub_parts_item = sub_parts_item_data.to_dict()
            sub_parts.append(sub_parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sub_parts": sub_parts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.message_part import MessagePart

        d = src_dict.copy()
        sub_parts = []
        _sub_parts = d.pop("sub_parts")
        for sub_parts_item_data in _sub_parts:
            sub_parts_item = MessagePart.from_dict(sub_parts_item_data)

            sub_parts.append(sub_parts_item)

        collection_part = cls(
            sub_parts=sub_parts,
        )

        collection_part.additional_properties = d
        return collection_part

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
