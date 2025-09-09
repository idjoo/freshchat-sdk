from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reports_response_v2_status import ReportsResponseV2Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reports_link import ReportsLink


T = TypeVar("T", bound="ReportsResponseV2")


@_attrs_define
class ReportsResponseV2:
    """Response for GET reports call with sub-reports

    Attributes:
        id (Union[Unset, str]): Unique Id given to the customers for the requested query Example:
            1ac520cf-b1a4-4741-8b01-e383563ae402.
        interval (Union[Unset, str]): Interval between two ranges Example: 2019-08-21 05:30:00.0_2019-10-30 23:59:59.0.
        links (Union[Unset, list['ReportsLink']]): List of Private URL Links split according to optimal time period.
        status (Union[Unset, ReportsResponseV2Status]): Indicates the status of the job results Example: COMPLETED.
    """

    id: Union[Unset, str] = UNSET
    interval: Union[Unset, str] = UNSET
    links: Union[Unset, list["ReportsLink"]] = UNSET
    status: Union[Unset, ReportsResponseV2Status] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        interval = self.interval

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if interval is not UNSET:
            field_dict["interval"] = interval
        if links is not UNSET:
            field_dict["links"] = links
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.reports_link import ReportsLink

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        interval = d.pop("interval", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ReportsLink.from_dict(links_item_data)

            links.append(links_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportsResponseV2Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReportsResponseV2Status(_status)

        reports_response_v2 = cls(
            id=id,
            interval=interval,
            links=links,
            status=status,
        )

        reports_response_v2.additional_properties = d
        return reports_response_v2

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
