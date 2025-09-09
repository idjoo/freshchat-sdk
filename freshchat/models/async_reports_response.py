from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="AsyncReportsResponse")


@_attrs_define
class AsyncReportsResponse:
    """Response for async fetch reports call

    Attributes:
        id (Union[Unset, str]): report id to fetch the status and url of the requested report Example:
            1ac520cf-b1a4-4741-8b01-e383563ae402.
        link (Union[Unset, Link]):
    """

    id: Union[Unset, str] = UNSET
    link: Union[Unset, "Link"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if link is not UNSET:
            field_dict["link"] = link

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

        async_reports_response = cls(
            id=id,
            link=link,
        )

        async_reports_response.additional_properties = d
        return async_reports_response

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
