from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_conversation_requests_properties import UpdateConversationRequestsProperties


T = TypeVar("T", bound="UpdateConversationRequests")


@_attrs_define
class UpdateConversationRequests:
    """
    Attributes:
        conversation_id (str): Identifier of the conversation object, auto-generated when a conversation record is
            created in the Freshchat system.
        assigned_agent_id (Union[Unset, str]): Identifier of the agent assigned to the conversation, auto-generated when
            an agent’s information is configured in the Freshchat system.
        assigned_group_id (Union[Unset, str]): Identifier of the group to which the conversation is assigned, auto-
            generated when a group is created in the Freshchat system.
        assigned_org_agent_id (Union[Unset, str]): Organization-level identifier of the agent, to whom the conversation
            is assigned for resolution.
        assigned_org_group_id (Union[Unset, str]): Organization-level identifier of the group, to which the conversation
            is assigned for resolution.
        channel_id (Union[Unset, str]): Identifier of the topic under which the conversation is created, auto-generated
            when a topic is created in the Freshchat system.
        properties (Union[Unset, UpdateConversationRequestsProperties]): Details of the conversation properties
            configured for the Freshchat account.
        status (Union[Unset, str]): Status of the conversation.
    """

    conversation_id: str
    assigned_agent_id: Union[Unset, str] = UNSET
    assigned_group_id: Union[Unset, str] = UNSET
    assigned_org_agent_id: Union[Unset, str] = UNSET
    assigned_org_group_id: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    properties: Union[Unset, "UpdateConversationRequestsProperties"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        assigned_agent_id = self.assigned_agent_id

        assigned_group_id = self.assigned_group_id

        assigned_org_agent_id = self.assigned_org_agent_id

        assigned_org_group_id = self.assigned_org_group_id

        channel_id = self.channel_id

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
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
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_conversation_requests_properties import UpdateConversationRequestsProperties

        d = src_dict.copy()
        conversation_id = d.pop("conversation_id")

        assigned_agent_id = d.pop("assigned_agent_id", UNSET)

        assigned_group_id = d.pop("assigned_group_id", UNSET)

        assigned_org_agent_id = d.pop("assigned_org_agent_id", UNSET)

        assigned_org_group_id = d.pop("assigned_org_group_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, UpdateConversationRequestsProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = UpdateConversationRequestsProperties.from_dict(_properties)

        status = d.pop("status", UNSET)

        update_conversation_requests = cls(
            conversation_id=conversation_id,
            assigned_agent_id=assigned_agent_id,
            assigned_group_id=assigned_group_id,
            assigned_org_agent_id=assigned_org_agent_id,
            assigned_org_group_id=assigned_org_group_id,
            channel_id=channel_id,
            properties=properties,
            status=status,
        )

        update_conversation_requests.additional_properties = d
        return update_conversation_requests

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
