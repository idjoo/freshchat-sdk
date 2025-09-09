from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        deprecation (Union[Unset, str]):  Example: string.
        href (Union[Unset, str]):  Example: string.
        hreflang (Union[Unset, str]):  Example: string.
        media (Union[Unset, str]):  Example: string.
        rel (Union[Unset, str]):  Example: string.
        title (Union[Unset, str]):  Example: string.
        type_ (Union[Unset, str]):  Example: string.
    """

    deprecation: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    hreflang: Union[Unset, str] = UNSET
    media: Union[Unset, str] = UNSET
    rel: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deprecation = self.deprecation

        href = self.href

        hreflang = self.hreflang

        media = self.media

        rel = self.rel

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deprecation is not UNSET:
            field_dict["deprecation"] = deprecation
        if href is not UNSET:
            field_dict["href"] = href
        if hreflang is not UNSET:
            field_dict["hreflang"] = hreflang
        if media is not UNSET:
            field_dict["media"] = media
        if rel is not UNSET:
            field_dict["rel"] = rel
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        deprecation = d.pop("deprecation", UNSET)

        href = d.pop("href", UNSET)

        hreflang = d.pop("hreflang", UNSET)

        media = d.pop("media", UNSET)

        rel = d.pop("rel", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        link = cls(
            deprecation=deprecation,
            href=href,
            hreflang=hreflang,
            media=media,
            rel=rel,
            title=title,
            type_=type_,
        )

        link.additional_properties = d
        return link

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
