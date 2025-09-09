from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="OutboundMessageSendResp")


@_attrs_define
class OutboundMessageSendResp:
    """outbound message send response

    Attributes:
        link (Link):
        request_id (str): request identifier Example: 0fcdd6b6-1f80-4643-a294-8e0625ce30dd.
        request_process_time (str): request processing time in seconds Example: 1.
    """

    link: "Link"
    request_id: str
    request_process_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link.to_dict()

        request_id = self.request_id

        request_process_time = self.request_process_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "request_id": request_id,
                "request_process_time": request_process_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        link = Link.from_dict(d.pop("link"))

        request_id = d.pop("request_id")

        request_process_time = d.pop("request_process_time")

        outbound_message_send_resp = cls(
            link=link,
            request_id=request_id,
            request_process_time=request_process_time,
        )

        outbound_message_send_resp.additional_properties = d
        return outbound_message_send_resp

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
