from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reply_conversation_request_message_parts_item import ReplyConversationRequestMessagePartsItem
    from ..models.reply_conversation_request_reply_parts_item import ReplyConversationRequestReplyPartsItem


T = TypeVar("T", bound="ReplyConversationRequest")


@_attrs_define
class ReplyConversationRequest:
    """
    Attributes:
        actor_id (Union[Unset, str]):
        actor_type (Union[Unset, str]):
        message_parts (Union[Unset, list['ReplyConversationRequestMessagePartsItem']]):
        message_type (Union[Unset, str]):
        reply_parts (Union[Unset, list['ReplyConversationRequestReplyPartsItem']]):
        user_id (Union[Unset, str]):
    """

    actor_id: Union[Unset, str] = UNSET
    actor_type: Union[Unset, str] = UNSET
    message_parts: Union[Unset, list["ReplyConversationRequestMessagePartsItem"]] = UNSET
    message_type: Union[Unset, str] = UNSET
    reply_parts: Union[Unset, list["ReplyConversationRequestReplyPartsItem"]] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_id = self.actor_id

        actor_type = self.actor_type

        message_parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.message_parts, Unset):
            message_parts = []
            for message_parts_item_data in self.message_parts:
                message_parts_item = message_parts_item_data.to_dict()
                message_parts.append(message_parts_item)

        message_type = self.message_type

        reply_parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reply_parts, Unset):
            reply_parts = []
            for reply_parts_item_data in self.reply_parts:
                reply_parts_item = reply_parts_item_data.to_dict()
                reply_parts.append(reply_parts_item)

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if actor_type is not UNSET:
            field_dict["actor_type"] = actor_type
        if message_parts is not UNSET:
            field_dict["message_parts"] = message_parts
        if message_type is not UNSET:
            field_dict["message_type"] = message_type
        if reply_parts is not UNSET:
            field_dict["reply_parts"] = reply_parts
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.reply_conversation_request_message_parts_item import ReplyConversationRequestMessagePartsItem
        from ..models.reply_conversation_request_reply_parts_item import ReplyConversationRequestReplyPartsItem

        d = src_dict.copy()
        actor_id = d.pop("actor_id", UNSET)

        actor_type = d.pop("actor_type", UNSET)

        message_parts = []
        _message_parts = d.pop("message_parts", UNSET)
        for message_parts_item_data in _message_parts or []:
            message_parts_item = ReplyConversationRequestMessagePartsItem.from_dict(message_parts_item_data)

            message_parts.append(message_parts_item)

        message_type = d.pop("message_type", UNSET)

        reply_parts = []
        _reply_parts = d.pop("reply_parts", UNSET)
        for reply_parts_item_data in _reply_parts or []:
            reply_parts_item = ReplyConversationRequestReplyPartsItem.from_dict(reply_parts_item_data)

            reply_parts.append(reply_parts_item)

        user_id = d.pop("user_id", UNSET)

        reply_conversation_request = cls(
            actor_id=actor_id,
            actor_type=actor_type,
            message_parts=message_parts,
            message_type=message_type,
            reply_parts=reply_parts,
            user_id=user_id,
        )

        reply_conversation_request.additional_properties = d
        return reply_conversation_request

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
