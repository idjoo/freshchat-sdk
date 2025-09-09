from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CallbackPart")


@_attrs_define
class CallbackPart:
    """callback part

    Attributes:
        label (str): label Example: 👍 upvote.
        payload (str): payload Example: {"id":"483b0c7a-583e-4d5f-a486-9028cdc39e24", "vote":"1"}.
    """

    label: str
    payload: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        payload = d.pop("payload")

        callback_part = cls(
            label=label,
            payload=payload,
        )

        callback_part.additional_properties = d
        return callback_part

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
