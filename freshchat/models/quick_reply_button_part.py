from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickReplyButtonPart")


@_attrs_define
class QuickReplyButtonPart:
    """quick reply button part

    Attributes:
        label (str): label Example: string.
        custom_reply_text (Union[Unset, str]): customReplyText Example: string.
        payload (Union[Unset, str]): payload Example: string.
    """

    label: str
    custom_reply_text: Union[Unset, str] = UNSET
    payload: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        custom_reply_text = self.custom_reply_text

        payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if custom_reply_text is not UNSET:
            field_dict["custom_reply_text"] = custom_reply_text
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        custom_reply_text = d.pop("custom_reply_text", UNSET)

        payload = d.pop("payload", UNSET)

        quick_reply_button_part = cls(
            label=label,
            custom_reply_text=custom_reply_text,
            payload=payload,
        )

        quick_reply_button_part.additional_properties = d
        return quick_reply_button_part

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
