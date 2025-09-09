from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.message import Message


T = TypeVar("T", bound="TranscriptMessageResponse")


@_attrs_define
class TranscriptMessageResponse:
    """get Messages for a conversation call

    Attributes:
        link (Union[Unset, Link]):
        messages (Union[Unset, list['Message']]): list of messages belonging to the conversation
    """

    link: Union[Unset, "Link"] = UNSET
    messages: Union[Unset, list["Message"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link is not UNSET:
            field_dict["link"] = link
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.link import Link
        from ..models.message import Message

        d = src_dict.copy()
        _link = d.pop("link", UNSET)
        link: Union[Unset, Link]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        transcript_message_response = cls(
            link=link,
            messages=messages,
        )

        transcript_message_response.additional_properties = d
        return transcript_message_response

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
