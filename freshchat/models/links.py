from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linklink import Linklink


T = TypeVar("T", bound="Links")


@_attrs_define
class Links:
    """links model

    Attributes:
        first_page (Union[Unset, Linklink]): link model
        last_page (Union[Unset, Linklink]): link model
        next_page (Union[Unset, Linklink]): link model
        previous_page (Union[Unset, Linklink]): link model
    """

    first_page: Union[Unset, "Linklink"] = UNSET
    last_page: Union[Unset, "Linklink"] = UNSET
    next_page: Union[Unset, "Linklink"] = UNSET
    previous_page: Union[Unset, "Linklink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_page, Unset):
            first_page = self.first_page.to_dict()

        last_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_page, Unset):
            last_page = self.last_page.to_dict()

        next_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_page, Unset):
            next_page = self.next_page.to_dict()

        previous_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous_page, Unset):
            previous_page = self.previous_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_page is not UNSET:
            field_dict["first_page"] = first_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.linklink import Linklink

        d = src_dict.copy()
        _first_page = d.pop("first_page", UNSET)
        first_page: Union[Unset, Linklink]
        if isinstance(_first_page, Unset):
            first_page = UNSET
        else:
            first_page = Linklink.from_dict(_first_page)

        _last_page = d.pop("last_page", UNSET)
        last_page: Union[Unset, Linklink]
        if isinstance(_last_page, Unset):
            last_page = UNSET
        else:
            last_page = Linklink.from_dict(_last_page)

        _next_page = d.pop("next_page", UNSET)
        next_page: Union[Unset, Linklink]
        if isinstance(_next_page, Unset):
            next_page = UNSET
        else:
            next_page = Linklink.from_dict(_next_page)

        _previous_page = d.pop("previous_page", UNSET)
        previous_page: Union[Unset, Linklink]
        if isinstance(_previous_page, Unset):
            previous_page = UNSET
        else:
            previous_page = Linklink.from_dict(_previous_page)

        links = cls(
            first_page=first_page,
            last_page=last_page,
            next_page=next_page,
            previous_page=previous_page,
        )

        links.additional_properties = d
        return links

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
