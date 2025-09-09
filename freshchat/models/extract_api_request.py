from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extract_api_request_event import ExtractApiRequestEvent
from ..models.extract_api_request_format import ExtractApiRequestFormat

T = TypeVar("T", bound="ExtractApiRequest")


@_attrs_define
class ExtractApiRequest:
    """Request body for extract api

    Attributes:
        end (str):  Example: 2019-05-25T10:00:00.000Z.
        event (ExtractApiRequestEvent):  Example: Conversation-Agent-Assigned.
        format_ (ExtractApiRequestFormat):  Example: csv.
        start (str):  Example: 2019-05-20T10:00:00.000Z.
    """

    end: str
    event: ExtractApiRequestEvent
    format_: ExtractApiRequestFormat
    start: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        event = self.event.value

        format_ = self.format_.value

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "event": event,
                "format": format_,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end = d.pop("end")

        event = ExtractApiRequestEvent(d.pop("event"))

        format_ = ExtractApiRequestFormat(d.pop("format"))

        start = d.pop("start")

        extract_api_request = cls(
            end=end,
            event=event,
            format_=format_,
            start=start,
        )

        extract_api_request.additional_properties = d
        return extract_api_request

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
