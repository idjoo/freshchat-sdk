import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.message_actor_type import MessageActorType
from ..models.message_message_source import MessageMessageSource
from ..models.message_message_type import MessageMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_reply_to import InReplyTo
    from ..models.message_meta_data import MessageMetaData
    from ..models.message_part import MessagePart


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """message model

    Attributes:
        actor_type (MessageActorType):  Example: agent.
        app_id (str):  Example: d01f83a4-6af0-4a05-8906-47284db2e1a8.
        channel_id (str):  Example: 1b99afe4-7b3d-4f9e-b284-d7778b249f6e.
        conversation_id (str):  Example: da8de71b-78c8-4256-8923-0de858ff6a80.
        message_parts (list['MessagePart']):
        message_type (MessageMessageType):  Example: normal.
        actor_id (Union[Unset, str]):  Example: 9d304e8a-31fd-4e4a-85e8-b62edb95d53f.
        created_time (Union[Unset, datetime.datetime]):  Example: 2017-11-16T11:34:04.431Z.
        id (Union[Unset, str]): id Example: 6c03caf2-a37f-45a2-a9a3-6e03aa7b85f5.
        in_reply_to (Union[Unset, InReplyTo]): message reply info model
        message_source (Union[Unset, MessageMessageSource]):  Example: WEB.
        meta_data (Union[Unset, MessageMetaData]):  Example: {"isResolved" : "true"}.
        reply_parts (Union[Unset, list['MessagePart']]):
    """

    actor_type: MessageActorType
    app_id: str
    channel_id: str
    conversation_id: str
    message_parts: list["MessagePart"]
    message_type: MessageMessageType
    actor_id: Union[Unset, str] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    in_reply_to: Union[Unset, "InReplyTo"] = UNSET
    message_source: Union[Unset, MessageMessageSource] = UNSET
    meta_data: Union[Unset, "MessageMetaData"] = UNSET
    reply_parts: Union[Unset, list["MessagePart"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_type = self.actor_type.value

        app_id = self.app_id

        channel_id = self.channel_id

        conversation_id = self.conversation_id

        message_parts = []
        for message_parts_item_data in self.message_parts:
            message_parts_item = message_parts_item_data.to_dict()
            message_parts.append(message_parts_item)

        message_type = self.message_type.value

        actor_id = self.actor_id

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        id = self.id

        in_reply_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.in_reply_to, Unset):
            in_reply_to = self.in_reply_to.to_dict()

        message_source: Union[Unset, str] = UNSET
        if not isinstance(self.message_source, Unset):
            message_source = self.message_source.value

        meta_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        reply_parts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reply_parts, Unset):
            reply_parts = []
            for reply_parts_item_data in self.reply_parts:
                reply_parts_item = reply_parts_item_data.to_dict()
                reply_parts.append(reply_parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor_type": actor_type,
                "app_id": app_id,
                "channel_id": channel_id,
                "conversation_id": conversation_id,
                "message_parts": message_parts,
                "message_type": message_type,
            }
        )
        if actor_id is not UNSET:
            field_dict["actor_id"] = actor_id
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if id is not UNSET:
            field_dict["id"] = id
        if in_reply_to is not UNSET:
            field_dict["in_reply_to"] = in_reply_to
        if message_source is not UNSET:
            field_dict["message_source"] = message_source
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data
        if reply_parts is not UNSET:
            field_dict["reply_parts"] = reply_parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.in_reply_to import InReplyTo
        from ..models.message_meta_data import MessageMetaData
        from ..models.message_part import MessagePart

        d = src_dict.copy()
        actor_type = MessageActorType(d.pop("actor_type"))

        app_id = d.pop("app_id")

        channel_id = d.pop("channel_id")

        conversation_id = d.pop("conversation_id")

        message_parts = []
        _message_parts = d.pop("message_parts")
        for message_parts_item_data in _message_parts:
            message_parts_item = MessagePart.from_dict(message_parts_item_data)

            message_parts.append(message_parts_item)

        message_type = MessageMessageType(d.pop("message_type"))

        actor_id = d.pop("actor_id", UNSET)

        _created_time = d.pop("created_time", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        id = d.pop("id", UNSET)

        _in_reply_to = d.pop("in_reply_to", UNSET)
        in_reply_to: Union[Unset, InReplyTo]
        if isinstance(_in_reply_to, Unset):
            in_reply_to = UNSET
        else:
            in_reply_to = InReplyTo.from_dict(_in_reply_to)

        _message_source = d.pop("message_source", UNSET)
        message_source: Union[Unset, MessageMessageSource]
        if isinstance(_message_source, Unset):
            message_source = UNSET
        else:
            message_source = MessageMessageSource(_message_source)

        _meta_data = d.pop("meta_data", UNSET)
        meta_data: Union[Unset, MessageMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = MessageMetaData.from_dict(_meta_data)

        reply_parts = []
        _reply_parts = d.pop("reply_parts", UNSET)
        for reply_parts_item_data in _reply_parts or []:
            reply_parts_item = MessagePart.from_dict(reply_parts_item_data)

            reply_parts.append(reply_parts_item)

        message = cls(
            actor_type=actor_type,
            app_id=app_id,
            channel_id=channel_id,
            conversation_id=conversation_id,
            message_parts=message_parts,
            message_type=message_type,
            actor_id=actor_id,
            created_time=created_time,
            id=id,
            in_reply_to=in_reply_to,
            message_source=message_source,
            meta_data=meta_data,
            reply_parts=reply_parts,
        )

        message.additional_properties = d
        return message

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
