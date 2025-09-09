from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_availability_status import AgentAvailabilityStatus
from ..models.agent_routing_type import AgentRoutingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.social_profile import SocialProfile
    from ..models.status import Status


T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """agent model

    Attributes:
        agent_status (Union[Unset, Status]): Status model
        availability_status (Union[Unset, AgentAvailabilityStatus]):  Example: AVAILABLE.
        avatar (Union[Unset, Image]): image model
        biography (Union[Unset, str]):  Example: I'm your friendly neighbourhood support guy!.
        email (Union[Unset, str]): email Example: govind.patel@freshworks.com.
        first_name (Union[Unset, str]): first_name Example: Govind.
        freshid_uuid (Union[Unset, str]):  Example: d01faba8-6655-4cce-88fa-a596cc75ece5.
        get_ocr_available (Union[Unset, int]):
        groups (Union[Unset, list[str]]):  Example: [string1, string2].
        id (Union[Unset, str]): id Example: 2681d294-3460-4f32-b5fb-828958995b5c.
        is_deactivated (Union[Unset, bool]):
        last_name (Union[Unset, str]): last_name Example: Patel.
        locale (Union[Unset, str]):  Example: en-us.
        phone (Union[Unset, str]):  Example: 123456789.
        role_id (Union[Unset, str]):  Example: string.
        routing_type (Union[Unset, AgentRoutingType]):  Example: OCR.
        skill_id (Union[Unset, str]):  Example: d01faba8-6655-4cce-88fa-a596cc75ece5.
        social_profiles (Union[Unset, list['SocialProfile']]):
        timezone (Union[Unset, str]):  Example: Asia/Kolkata.
    """

    agent_status: Union[Unset, "Status"] = UNSET
    availability_status: Union[Unset, AgentAvailabilityStatus] = UNSET
    avatar: Union[Unset, "Image"] = UNSET
    biography: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    freshid_uuid: Union[Unset, str] = UNSET
    get_ocr_available: Union[Unset, int] = UNSET
    groups: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    is_deactivated: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    role_id: Union[Unset, str] = UNSET
    routing_type: Union[Unset, AgentRoutingType] = UNSET
    skill_id: Union[Unset, str] = UNSET
    social_profiles: Union[Unset, list["SocialProfile"]] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.agent_status, Unset):
            agent_status = self.agent_status.to_dict()

        availability_status: Union[Unset, str] = UNSET
        if not isinstance(self.availability_status, Unset):
            availability_status = self.availability_status.value

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        biography = self.biography

        email = self.email

        first_name = self.first_name

        freshid_uuid = self.freshid_uuid

        get_ocr_available = self.get_ocr_available

        groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        id = self.id

        is_deactivated = self.is_deactivated

        last_name = self.last_name

        locale = self.locale

        phone = self.phone

        role_id = self.role_id

        routing_type: Union[Unset, str] = UNSET
        if not isinstance(self.routing_type, Unset):
            routing_type = self.routing_type.value

        skill_id = self.skill_id

        social_profiles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.social_profiles, Unset):
            social_profiles = []
            for social_profiles_item_data in self.social_profiles:
                social_profiles_item = social_profiles_item_data.to_dict()
                social_profiles.append(social_profiles_item)

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_status is not UNSET:
            field_dict["agent_status"] = agent_status
        if availability_status is not UNSET:
            field_dict["availability_status"] = availability_status
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if biography is not UNSET:
            field_dict["biography"] = biography
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if freshid_uuid is not UNSET:
            field_dict["freshid_uuid"] = freshid_uuid
        if get_ocr_available is not UNSET:
            field_dict["get_ocr_available"] = get_ocr_available
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if is_deactivated is not UNSET:
            field_dict["is_deactivated"] = is_deactivated
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if locale is not UNSET:
            field_dict["locale"] = locale
        if phone is not UNSET:
            field_dict["phone"] = phone
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if routing_type is not UNSET:
            field_dict["routing_type"] = routing_type
        if skill_id is not UNSET:
            field_dict["skill_id"] = skill_id
        if social_profiles is not UNSET:
            field_dict["social_profiles"] = social_profiles
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.social_profile import SocialProfile
        from ..models.status import Status

        d = src_dict.copy()
        _agent_status = d.pop("agent_status", UNSET)
        agent_status: Union[Unset, Status]
        if isinstance(_agent_status, Unset):
            agent_status = UNSET
        else:
            agent_status = Status.from_dict(_agent_status)

        _availability_status = d.pop("availability_status", UNSET)
        availability_status: Union[Unset, AgentAvailabilityStatus]
        if isinstance(_availability_status, Unset):
            availability_status = UNSET
        else:
            availability_status = AgentAvailabilityStatus(_availability_status)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Image]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Image.from_dict(_avatar)

        biography = d.pop("biography", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        freshid_uuid = d.pop("freshid_uuid", UNSET)

        get_ocr_available = d.pop("get_ocr_available", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        id = d.pop("id", UNSET)

        is_deactivated = d.pop("is_deactivated", UNSET)

        last_name = d.pop("last_name", UNSET)

        locale = d.pop("locale", UNSET)

        phone = d.pop("phone", UNSET)

        role_id = d.pop("role_id", UNSET)

        _routing_type = d.pop("routing_type", UNSET)
        routing_type: Union[Unset, AgentRoutingType]
        if isinstance(_routing_type, Unset):
            routing_type = UNSET
        else:
            routing_type = AgentRoutingType(_routing_type)

        skill_id = d.pop("skill_id", UNSET)

        social_profiles = []
        _social_profiles = d.pop("social_profiles", UNSET)
        for social_profiles_item_data in _social_profiles or []:
            social_profiles_item = SocialProfile.from_dict(social_profiles_item_data)

            social_profiles.append(social_profiles_item)

        timezone = d.pop("timezone", UNSET)

        agent = cls(
            agent_status=agent_status,
            availability_status=availability_status,
            avatar=avatar,
            biography=biography,
            email=email,
            first_name=first_name,
            freshid_uuid=freshid_uuid,
            get_ocr_available=get_ocr_available,
            groups=groups,
            id=id,
            is_deactivated=is_deactivated,
            last_name=last_name,
            locale=locale,
            phone=phone,
            role_id=role_id,
            routing_type=routing_type,
            skill_id=skill_id,
            social_profiles=social_profiles,
            timezone=timezone,
        )

        agent.additional_properties = d
        return agent

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
