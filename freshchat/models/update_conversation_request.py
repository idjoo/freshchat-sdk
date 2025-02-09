from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_conversation_request_status import UpdateConversationRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_conversation_request_properties import UpdateConversationRequestProperties


T = TypeVar("T", bound="UpdateConversationRequest")


@_attrs_define
class UpdateConversationRequest:
    """
    Attributes:
        assigned_group_id (Union[Unset, str]): Identifier of the group to which the conversation is assigned, auto-
            generated when a group is created in the Freshchat system.
        properties (Union[Unset, UpdateConversationRequestProperties]): Details of the conversation properties
            configured for the Freshchat account. The attribute contains the names of the conversation properties configured
            and the corresponding values populated, as a valid JSON object of key - value pairs.
        status (Union[Unset, UpdateConversationRequestStatus]): Status of the conversation.
    """

    assigned_group_id: Union[Unset, str] = UNSET
    properties: Union[Unset, "UpdateConversationRequestProperties"] = UNSET
    status: Union[Unset, UpdateConversationRequestStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_group_id = self.assigned_group_id

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_group_id is not UNSET:
            field_dict["assigned_group_id"] = assigned_group_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_conversation_request_properties import UpdateConversationRequestProperties

        d = src_dict.copy()
        assigned_group_id = d.pop("assigned_group_id", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, UpdateConversationRequestProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = UpdateConversationRequestProperties.from_dict(_properties)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateConversationRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateConversationRequestStatus(_status)

        update_conversation_request = cls(
            assigned_group_id=assigned_group_id,
            properties=properties,
            status=status,
        )

        update_conversation_request.additional_properties = d
        return update_conversation_request

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
