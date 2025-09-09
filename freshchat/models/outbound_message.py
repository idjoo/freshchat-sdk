from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outbound_message_provider import OutboundMessageProvider
from ..models.outbound_message_status import OutboundMessageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data import Data
    from ..models.user_handle import UserHandle


T = TypeVar("T", bound="OutboundMessage")


@_attrs_define
class OutboundMessage:
    """outbound message

    Attributes:
        created_on (int): message created timestamp in epoch format Example: 1566970961.
        data (Data): Data sent to the recipient
        from_ (UserHandle): User handler to send outbound message
        message_id (str): message id Example: 5841b28c-7869-474f-9b25-c2b1ba9aa7b9.
        provider (OutboundMessageProvider): medium to send outbound messages Example: whatsapp.
        request_id (str): identifier for every request Example: 5841b28c-7869-474f-9b25-c2b1ba9aa7b9.
        status (OutboundMessageStatus): status of the message Example: Sent.
        to (UserHandle): User handler to send outbound message
        failure_code (Union[Unset, str]): failure code Example: OBM001.
        failure_reason (Union[Unset, str]): reason for the failure Example: no template exists.
    """

    created_on: int
    data: "Data"
    from_: "UserHandle"
    message_id: str
    provider: OutboundMessageProvider
    request_id: str
    status: OutboundMessageStatus
    to: "UserHandle"
    failure_code: Union[Unset, str] = UNSET
    failure_reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_on = self.created_on

        data = self.data.to_dict()

        from_ = self.from_.to_dict()

        message_id = self.message_id

        provider = self.provider.value

        request_id = self.request_id

        status = self.status.value

        to = self.to.to_dict()

        failure_code = self.failure_code

        failure_reason = self.failure_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_on": created_on,
                "data": data,
                "from": from_,
                "message_id": message_id,
                "provider": provider,
                "request_id": request_id,
                "status": status,
                "to": to,
            }
        )
        if failure_code is not UNSET:
            field_dict["failure_code"] = failure_code
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data import Data
        from ..models.user_handle import UserHandle

        d = src_dict.copy()
        created_on = d.pop("created_on")

        data = Data.from_dict(d.pop("data"))

        from_ = UserHandle.from_dict(d.pop("from"))

        message_id = d.pop("message_id")

        provider = OutboundMessageProvider(d.pop("provider"))

        request_id = d.pop("request_id")

        status = OutboundMessageStatus(d.pop("status"))

        to = UserHandle.from_dict(d.pop("to"))

        failure_code = d.pop("failure_code", UNSET)

        failure_reason = d.pop("failure_reason", UNSET)

        outbound_message = cls(
            created_on=created_on,
            data=data,
            from_=from_,
            message_id=message_id,
            provider=provider,
            request_id=request_id,
            status=status,
            to=to,
            failure_code=failure_code,
            failure_reason=failure_reason,
        )

        outbound_message.additional_properties = d
        return outbound_message

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
