import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.property_ import Property
    from ..models.social_profile import SocialProfile


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """user model

    Attributes:
        avatar (Union[Unset, Image]): image model
        created_time (Union[Unset, datetime.datetime]): created_time Example: 2018-08-16T11:34:04.431Z.
        email (Union[Unset, str]): email Example: govind.patel@freshworks.com.
        first_name (Union[Unset, str]): first_name Example: Govind.
        id (Union[Unset, str]): id Example: 2681d294-3460-4f32-b5fb-828958995b5c.
        last_name (Union[Unset, str]): last_name Example: Patel.
        phone (Union[Unset, str]):  Example: 123456789.
        properties (Union[Unset, list['Property']]): user properties
        reference_id (Union[Unset, str]): reference_id Example: 9d83ebc5-e036-4b48-b655-b0d79584b2c6.
        social_profiles (Union[Unset, list['SocialProfile']]):
    """

    avatar: Union[Unset, "Image"] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    properties: Union[Unset, list["Property"]] = UNSET
    reference_id: Union[Unset, str] = UNSET
    social_profiles: Union[Unset, list["SocialProfile"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        created_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        email = self.email

        first_name = self.first_name

        id = self.id

        last_name = self.last_name

        phone = self.phone

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        reference_id = self.reference_id

        social_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.social_profiles, Unset):
            social_profiles = []
            for social_profiles_item_data in self.social_profiles:
                social_profiles_item = social_profiles_item_data.to_dict()
                social_profiles.append(social_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if properties is not UNSET:
            field_dict["properties"] = properties
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id
        if social_profiles is not UNSET:
            field_dict["social_profiles"] = social_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.property_ import Property
        from ..models.social_profile import SocialProfile

        d = src_dict.copy()
        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Image]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Image.from_dict(_avatar)

        _created_time = d.pop("created_time", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Property.from_dict(properties_item_data)

            properties.append(properties_item)

        reference_id = d.pop("reference_id", UNSET)

        social_profiles = []
        _social_profiles = d.pop("social_profiles", UNSET)
        for social_profiles_item_data in _social_profiles or []:
            social_profiles_item = SocialProfile.from_dict(social_profiles_item_data)

            social_profiles.append(social_profiles_item)

        user = cls(
            avatar=avatar,
            created_time=created_time,
            email=email,
            first_name=first_name,
            id=id,
            last_name=last_name,
            phone=phone,
            properties=properties,
            reference_id=reference_id,
            social_profiles=social_profiles,
        )

        user.additional_properties = d
        return user

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
