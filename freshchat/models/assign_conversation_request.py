from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignConversationRequest")


@_attrs_define
class AssignConversationRequest:
    """
    Attributes:
        assigned_group_id (Union[Unset, str]): Identifier of the group to which the conversation is assigned, auto-
            generated when a group is created in the Freshchat system.
        status (Union[Unset, str]): Status of the conversation.
    """

    assigned_group_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_group_id = self.assigned_group_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_group_id is not UNSET:
            field_dict["assigned_group_id"] = assigned_group_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        assigned_group_id = d.pop("assigned_group_id", UNSET)

        status = d.pop("status", UNSET)

        assign_conversation_request = cls(
            assigned_group_id=assigned_group_id,
            status=status,
        )

        assign_conversation_request.additional_properties = d
        return assign_conversation_request

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
