from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateConversationRequests")


@_attrs_define
class CreateConversationRequests:
    """
    Attributes:
        channel_id (str): Identifier of the topic under which the conversation is to be created.
        messages (list[File]): Details of the messages that constitute the conversation.
        assigned_agent_id (Union[Unset, str]): Identifier of the agent to whom the conversation is assigned for
            resolution.
        assigned_group_id (Union[Unset, str]): Identifier of the group to which the conversation is assigned for
            resolution.
        assigned_org_agent_id (Union[Unset, str]): Organization-level identifier of the agent to whom the conversation
            is assigned for resolution.
        assigned_org_group_id (Union[Unset, str]): Organization-level identifier of the group to which the conversation
            is assigned for resolution.
    """

    channel_id: str
    messages: list[File]
    assigned_agent_id: Union[Unset, str] = UNSET
    assigned_group_id: Union[Unset, str] = UNSET
    assigned_org_agent_id: Union[Unset, str] = UNSET
    assigned_org_group_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_tuple()

            messages.append(messages_item)

        assigned_agent_id = self.assigned_agent_id

        assigned_group_id = self.assigned_group_id

        assigned_org_agent_id = self.assigned_org_agent_id

        assigned_org_group_id = self.assigned_org_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "messages": messages,
            }
        )
        if assigned_agent_id is not UNSET:
            field_dict["assigned_agent_id"] = assigned_agent_id
        if assigned_group_id is not UNSET:
            field_dict["assigned_group_id"] = assigned_group_id
        if assigned_org_agent_id is not UNSET:
            field_dict["assigned_org_agent_id"] = assigned_org_agent_id
        if assigned_org_group_id is not UNSET:
            field_dict["assigned_org_group_id"] = assigned_org_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = File(payload=BytesIO(messages_item_data))

            messages.append(messages_item)

        assigned_agent_id = d.pop("assigned_agent_id", UNSET)

        assigned_group_id = d.pop("assigned_group_id", UNSET)

        assigned_org_agent_id = d.pop("assigned_org_agent_id", UNSET)

        assigned_org_group_id = d.pop("assigned_org_group_id", UNSET)

        create_conversation_requests = cls(
            channel_id=channel_id,
            messages=messages,
            assigned_agent_id=assigned_agent_id,
            assigned_group_id=assigned_group_id,
            assigned_org_agent_id=assigned_org_agent_id,
            assigned_org_group_id=assigned_org_group_id,
        )

        create_conversation_requests.additional_properties = d
        return create_conversation_requests

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
