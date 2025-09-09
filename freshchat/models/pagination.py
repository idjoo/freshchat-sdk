from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """pagination model

    Attributes:
        current_page (Union[Unset, int]):  Example: 2.
        items_per_page (Union[Unset, int]):  Example: 10.
        total_items (Union[Unset, int]):  Example: 100.
        total_pages (Union[Unset, int]):  Example: 10.
    """

    current_page: Union[Unset, int] = UNSET
    items_per_page: Union[Unset, int] = UNSET
    total_items: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        items_per_page = self.items_per_page

        total_items = self.total_items

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if items_per_page is not UNSET:
            field_dict["items_per_page"] = items_per_page
        if total_items is not UNSET:
            field_dict["total_items"] = total_items
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        current_page = d.pop("current_page", UNSET)

        items_per_page = d.pop("items_per_page", UNSET)

        total_items = d.pop("total_items", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        pagination = cls(
            current_page=current_page,
            items_per_page=items_per_page,
            total_items=total_items,
            total_pages=total_pages,
        )

        pagination.additional_properties = d
        return pagination

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
