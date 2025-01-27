import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConversationResponse")


@_attrs_define
class UpdateConversationResponse:
    """
    Attributes:
        app_id (Union[Unset, str]):
        assigned_group_id (Union[Unset, str]):
        channel_id (Union[Unset, str]):
        conversation_id (Union[Unset, str]):
        conversation_internal_id (Union[Unset, int]):
        created_time (Union[Unset, datetime.datetime]):
        org_contact_id (Union[Unset, str]):
        skill_id (Union[Unset, int]):
        status (Union[Unset, str]):
        updated_time (Union[Unset, datetime.datetime]):
        url (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    app_id: Union[Unset, str] = UNSET
    assigned_group_id: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    conversation_id: Union[Unset, str] = UNSET
    conversation_internal_id: Union[Unset, int] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    org_contact_id: Union[Unset, str] = UNSET
    skill_id: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    updated_time: Union[Unset, datetime.datetime] = UNSET
    url: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        assigned_group_id = self.assigned_group_id

        channel_id = self.channel_id

        conversation_id = self.conversation_id

        conversation_internal_id = self.conversation_internal_id

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        org_contact_id = self.org_contact_id

        skill_id = self.skill_id

        status = self.status

        updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        url = self.url

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if assigned_group_id is not UNSET:
            field_dict["assigned_group_id"] = assigned_group_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if conversation_internal_id is not UNSET:
            field_dict["conversation_internal_id"] = conversation_internal_id
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if org_contact_id is not UNSET:
            field_dict["org_contact_id"] = org_contact_id
        if skill_id is not UNSET:
            field_dict["skill_id"] = skill_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_time is not UNSET:
            field_dict["updated_time"] = updated_time
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("app_id", UNSET)

        assigned_group_id = d.pop("assigned_group_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        conversation_internal_id = d.pop("conversation_internal_id", UNSET)

        _created_time = d.pop("created_time", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        org_contact_id = d.pop("org_contact_id", UNSET)

        skill_id = d.pop("skill_id", UNSET)

        status = d.pop("status", UNSET)

        _updated_time = d.pop("updated_time", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        url = d.pop("url", UNSET)

        user_id = d.pop("user_id", UNSET)

        update_conversation_response = cls(
            app_id=app_id,
            assigned_group_id=assigned_group_id,
            channel_id=channel_id,
            conversation_id=conversation_id,
            conversation_internal_id=conversation_internal_id,
            created_time=created_time,
            org_contact_id=org_contact_id,
            skill_id=skill_id,
            status=status,
            updated_time=updated_time,
            url=url,
            user_id=user_id,
        )

        update_conversation_response.additional_properties = d
        return update_conversation_response

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
