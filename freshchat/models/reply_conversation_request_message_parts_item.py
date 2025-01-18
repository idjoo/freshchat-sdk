from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reply_conversation_request_message_parts_item_text import ReplyConversationRequestMessagePartsItemText


T = TypeVar("T", bound="ReplyConversationRequestMessagePartsItem")


@_attrs_define
class ReplyConversationRequestMessagePartsItem:
    """
    Attributes:
        text (Union[Unset, ReplyConversationRequestMessagePartsItemText]):
    """

    text: Union[Unset, "ReplyConversationRequestMessagePartsItemText"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.reply_conversation_request_message_parts_item_text import (
            ReplyConversationRequestMessagePartsItemText,
        )

        d = src_dict.copy()
        _text = d.pop("text", UNSET)
        text: Union[Unset, ReplyConversationRequestMessagePartsItemText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = ReplyConversationRequestMessagePartsItemText.from_dict(_text)

        reply_conversation_request_message_parts_item = cls(
            text=text,
        )

        reply_conversation_request_message_parts_item.additional_properties = d
        return reply_conversation_request_message_parts_item

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
