from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcript_conversation_response import TranscriptConversationResponse


T = TypeVar("T", bound="ConversationListResponse")


@_attrs_define
class ConversationListResponse:
    """get Conversations for a given user

    Attributes:
        conversations (Union[Unset, list['TranscriptConversationResponse']]): list of conversations belonging to the
            userId
    """

    conversations: Union[Unset, list["TranscriptConversationResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conversations, Unset):
            conversations = []
            for conversations_item_data in self.conversations:
                conversations_item = conversations_item_data.to_dict()
                conversations.append(conversations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversations is not UNSET:
            field_dict["conversations"] = conversations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transcript_conversation_response import TranscriptConversationResponse

        d = src_dict.copy()
        conversations = []
        _conversations = d.pop("conversations", UNSET)
        for conversations_item_data in _conversations or []:
            conversations_item = TranscriptConversationResponse.from_dict(conversations_item_data)

            conversations.append(conversations_item)

        conversation_list_response = cls(
            conversations=conversations,
        )

        conversation_list_response.additional_properties = d
        return conversation_list_response

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
