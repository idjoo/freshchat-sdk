from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConversations")


@_attrs_define
class UpdateConversations:
    """
    Attributes:
        channel_id (Union[Unset, str]): Identifier of the topic under which the conversation is created, auto-generated
            when a topic is created in the Freshchat system.
        conversation_id (Union[Unset, str]): Identifier of the conversation object, auto-generated when a conversation
            record is created in the Freshchat system.
        status (Union[Unset, str]): Status of the conversation.
    """

    channel_id: Union[Unset, str] = UNSET
    conversation_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        conversation_id = self.conversation_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        status = d.pop("status", UNSET)

        update_conversations = cls(
            channel_id=channel_id,
            conversation_id=conversation_id,
            status=status,
        )

        update_conversations.additional_properties = d
        return update_conversations

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
