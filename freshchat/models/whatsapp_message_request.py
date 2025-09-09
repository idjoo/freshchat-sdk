from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data import Data
    from ..models.user_handle import UserHandle


T = TypeVar("T", bound="WhatsappMessageRequest")


@_attrs_define
class WhatsappMessageRequest:
    """Request body to send proactive whatsapp messages

    Attributes:
        data (Data): Data sent to the recipient
        from_ (UserHandle): User handler to send outbound message
        to (list['UserHandle']): list of recipients
    """

    data: "Data"
    from_: "UserHandle"
    to: list["UserHandle"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        from_ = self.from_.to_dict()

        to = []
        for to_item_data in self.to:
            to_item = to_item_data.to_dict()
            to.append(to_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data import Data
        from ..models.user_handle import UserHandle

        d = src_dict.copy()
        data = Data.from_dict(d.pop("data"))

        from_ = UserHandle.from_dict(d.pop("from"))

        to = []
        _to = d.pop("to")
        for to_item_data in _to:
            to_item = UserHandle.from_dict(to_item_data)

            to.append(to_item)

        whatsapp_message_request = cls(
            data=data,
            from_=from_,
            to=to,
        )

        whatsapp_message_request.additional_properties = d
        return whatsapp_message_request

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
