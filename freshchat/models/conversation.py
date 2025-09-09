from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_status import ConversationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent import Agent
    from ..models.message import Message
    from ..models.user import User


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """conversation model

    Attributes:
        app_id (str):  Example: 9d83ebc5-e036-4b48-b655-b0d79584b2c5.
        assigned_agent_id (str):  Example: c2937604-0a08-43c2-a09c-e77f5f565a0e.
        assigned_group_id (str):  Example: c2937604-0a08-43c2-a09c-e77f5f565a0e.
        conversation_id (str):  Example: c2937604-0a08-43c2-a09c-e77f5f565a0e.
        messages (list['Message']):
        status (ConversationStatus):  Example: new.
        agents (Union[Unset, list['Agent']]):
        channel_id (Union[Unset, str]):  Example: 2681d294-3460-4f32-b5fb-828958995b5c.
        users (Union[Unset, list['User']]):
    """

    app_id: str
    assigned_agent_id: str
    assigned_group_id: str
    conversation_id: str
    messages: list["Message"]
    status: ConversationStatus
    agents: Union[Unset, list["Agent"]] = UNSET
    channel_id: Union[Unset, str] = UNSET
    users: Union[Unset, list["User"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        assigned_agent_id = self.assigned_agent_id

        assigned_group_id = self.assigned_group_id

        conversation_id = self.conversation_id

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        status = self.status.value

        agents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)

        channel_id = self.channel_id

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "assigned_agent_id": assigned_agent_id,
                "assigned_group_id": assigned_group_id,
                "conversation_id": conversation_id,
                "messages": messages,
                "status": status,
            }
        )
        if agents is not UNSET:
            field_dict["agents"] = agents
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.message import Message
        from ..models.user import User

        d = src_dict.copy()
        app_id = d.pop("app_id")

        assigned_agent_id = d.pop("assigned_agent_id")

        assigned_group_id = d.pop("assigned_group_id")

        conversation_id = d.pop("conversation_id")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        status = ConversationStatus(d.pop("status"))

        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = Agent.from_dict(agents_item_data)

            agents.append(agents_item)

        channel_id = d.pop("channel_id", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        conversation = cls(
            app_id=app_id,
            assigned_agent_id=assigned_agent_id,
            assigned_group_id=assigned_group_id,
            conversation_id=conversation_id,
            messages=messages,
            status=status,
            agents=agents,
            channel_id=channel_id,
            users=users,
        )

        conversation.additional_properties = d
        return conversation

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
