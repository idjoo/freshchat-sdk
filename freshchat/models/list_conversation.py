from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.list_conversation_properties import ListConversationProperties
    from ..models.list_conversation_users_item import ListConversationUsersItem


T = TypeVar("T", bound="ListConversation")


@_attrs_define
class ListConversation:
    """
    Attributes:
        messages (Union[Unset, list[File]]): Details of the messages that constitute the conversation.
        properties (Union[Unset, ListConversationProperties]): Details of the conversation properties configured for the
            Freshchat account.
        users (Union[Unset, list['ListConversationUsersItem']]): Details of the user who initiated the conversation.
    """

    messages: Union[Unset, list[File]] = UNSET
    properties: Union[Unset, "ListConversationProperties"] = UNSET
    users: Union[Unset, list["ListConversationUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        if messages is not UNSET:
            field_dict["messages"] = messages
        if properties is not UNSET:
            field_dict["properties"] = properties
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_conversation_properties import ListConversationProperties
        from ..models.list_conversation_users_item import ListConversationUsersItem

        d = src_dict.copy()
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = File(payload=BytesIO(messages_item_data))

            messages.append(messages_item)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ListConversationProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ListConversationProperties.from_dict(_properties)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ListConversationUsersItem.from_dict(users_item_data)

            users.append(users_item)

        list_conversation = cls(
            messages=messages,
            properties=properties,
            users=users,
        )

        list_conversation.additional_properties = d
        return list_conversation

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
