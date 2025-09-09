from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_template import MessageTemplate


T = TypeVar("T", bound="Data")


@_attrs_define
class Data:
    """Data sent to the recipient

    Attributes:
        message_template (Union[Unset, MessageTemplate]): whatsapp message template
    """

    message_template: Union[Unset, "MessageTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_template: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message_template, Unset):
            message_template = self.message_template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_template is not UNSET:
            field_dict["message_template"] = message_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.message_template import MessageTemplate

        d = src_dict.copy()
        _message_template = d.pop("message_template", UNSET)
        message_template: Union[Unset, MessageTemplate]
        if isinstance(_message_template, Unset):
            message_template = UNSET
        else:
            message_template = MessageTemplate.from_dict(_message_template)

        data = cls(
            message_template=message_template,
        )

        data.additional_properties = d
        return data

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
