from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_profile_type import SocialProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialProfile")


@_attrs_define
class SocialProfile:
    """social profiles model

    Attributes:
        type_ (SocialProfileType):  Example: facebook.
        id (Union[Unset, str]):  Example: govind.patel.
    """

    type_: SocialProfileType
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = SocialProfileType(d.pop("type"))

        id = d.pop("id", UNSET)

        social_profile = cls(
            type_=type_,
            id=id,
        )

        social_profile.additional_properties = d
        return social_profile

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
