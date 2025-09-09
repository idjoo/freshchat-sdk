from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reports_response_v1_status import ReportsResponseV1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ReportsResponseV1")


@_attrs_define
class ReportsResponseV1:
    """Response for GET reports call with a singular link

    Attributes:
        id (Union[Unset, str]): Unique Id given to the customers for the requested query Example:
            1ac520cf-b1a4-4741-8b01-e383563ae402.
        link (Union[Unset, Link]):
        status (Union[Unset, ReportsResponseV1Status]): Indicates the status of the job results Example: COMPLETED.
    """

    id: Union[Unset, str] = UNSET
    link: Union[Unset, "Link"] = UNSET
    status: Union[Unset, ReportsResponseV1Status] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if link is not UNSET:
            field_dict["link"] = link
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _link = d.pop("link", UNSET)
        link: Union[Unset, Link]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = Link.from_dict(_link)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportsResponseV1Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReportsResponseV1Status(_status)

        reports_response_v1 = cls(
            id=id,
            link=link,
            status=status,
        )

        reports_response_v1.additional_properties = d
        return reports_response_v1

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
