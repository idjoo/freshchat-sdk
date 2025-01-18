from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.conversations_properties import ConversationsProperties
    from ..models.conversations_users_item import ConversationsUsersItem


T = TypeVar("T", bound="Conversations")


@_attrs_define
class Conversations:
    """
    Attributes:
        channel_id (Union[Unset, str]): Identifier of the topic under which the conversation is to be created.
        messages (Union[Unset, list[File]]): Details of the messages that constitute the conversation.
        properties (Union[Unset, ConversationsProperties]): Details of the conversation properties configured for the
            Freshchat account.
        users (Union[Unset, list['ConversationsUsersItem']]): Details of the user who initiated the conversation.
    """

    channel_id: Union[Unset, str] = UNSET
    messages: Union[Unset, list[File]] = UNSET
    properties: Union[Unset, "ConversationsProperties"] = UNSET
    users: Union[Unset, list["ConversationsUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        messages: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_tuple()

                messages.append(messages_item)

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if properties is not UNSET:
            field_dict["properties"] = properties
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.conversations_properties import ConversationsProperties
        from ..models.conversations_users_item import ConversationsUsersItem

        d = src_dict.copy()
        channel_id = d.pop("channel_id", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = File(payload=BytesIO(messages_item_data))

            messages.append(messages_item)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ConversationsProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ConversationsProperties.from_dict(_properties)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ConversationsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        conversations = cls(
            channel_id=channel_id,
            messages=messages,
            properties=properties,
            users=users,
        )

        conversations.additional_properties = d
        return conversations

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
