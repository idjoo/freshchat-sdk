import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reports_link_status import ReportsLinkStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ReportsLink")


@_attrs_define
class ReportsLink:
    """list of private URL links split according to optimal time periods

    Attributes:
        from_ (Union[Unset, datetime.datetime]): time period from which the sub-report is generated Example:
            2020-02-09T00:00:00Z.
        link (Union[Unset, Link]):
        status (Union[Unset, ReportsLinkStatus]): indicates the status of this particular sub-report fetch Example:
            SUCCESS.
        to (Union[Unset, datetime.datetime]): time period upto which the sub-report is generated Example:
            2020-02-15T18:59:59Z.
    """

    from_: Union[Unset, datetime.datetime] = UNSET
    link: Union[Unset, "Link"] = UNSET
    status: Union[Unset, ReportsLinkStatus] = UNSET
    to: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if link is not UNSET:
            field_dict["link"] = link
        if status is not UNSET:
            field_dict["status"] = status
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.datetime]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _link = d.pop("link", UNSET)
        link: Union[Unset, Link]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportsLinkStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReportsLinkStatus(_status)

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.datetime]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        reports_link = cls(
            from_=from_,
            link=link,
            status=status,
            to=to,
        )

        reports_link.additional_properties = d
        return reports_link

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
