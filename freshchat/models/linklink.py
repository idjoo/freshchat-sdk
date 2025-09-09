from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linklink_rel import LinklinkRel
from ..types import UNSET, Unset

T = TypeVar("T", bound="Linklink")


@_attrs_define
class Linklink:
    """link model

    Attributes:
        href (Union[Unset, str]):  Example: /v1/groups?sort_by=name&items_per_page=10&sort_order=asc&page=3.
        rel (Union[Unset, LinklinkRel]):  Example: group.
        type_ (Union[Unset, str]):  Example: GET.
    """

    href: Union[Unset, str] = UNSET
    rel: Union[Unset, LinklinkRel] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        rel: Union[Unset, str] = UNSET
        if not isinstance(self.rel, Unset):
            rel = self.rel.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if rel is not UNSET:
            field_dict["rel"] = rel
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _rel = d.pop("rel", UNSET)
        rel: Union[Unset, LinklinkRel]
        if isinstance(_rel, Unset):
            rel = UNSET
        else:
            rel = LinklinkRel(_rel)

        type_ = d.pop("type", UNSET)

        linklink = cls(
            href=href,
            rel=rel,
            type_=type_,
        )

        linklink.additional_properties = d
        return linklink

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
