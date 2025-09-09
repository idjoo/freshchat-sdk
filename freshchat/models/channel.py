import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.image import Image
    from ..models.message import Message


T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """channel model

    Attributes:
        name (str):  Example: Inbox.
        tags (list[str]):  Example: [sales, support].
        assign_to_group (Union[Unset, Group]): group model
        enabled (Union[Unset, bool]):  Example: True.
        icon (Union[Unset, Image]): image model
        id (Union[Unset, str]): id Example: 6c03caf2-a37f-45a2-a9a3-6e03aa7b85f5.
        locale (Union[Unset, str]):  Example: en-Us.
        public (Union[Unset, bool]):  Example: True.
        updated_time (Union[Unset, datetime.datetime]):
        welcome_message (Union[Unset, Message]): message model
    """

    name: str
    tags: list[str]
    assign_to_group: Union[Unset, "Group"] = UNSET
    enabled: Union[Unset, bool] = UNSET
    icon: Union[Unset, "Image"] = UNSET
    id: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    public: Union[Unset, bool] = UNSET
    updated_time: Union[Unset, datetime.datetime] = UNSET
    welcome_message: Union[Unset, "Message"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tags = self.tags

        assign_to_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assign_to_group, Unset):
            assign_to_group = self.assign_to_group.to_dict()

        enabled = self.enabled

        icon: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        id = self.id

        locale = self.locale

        public = self.public

        updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        welcome_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.welcome_message, Unset):
            welcome_message = self.welcome_message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "tags": tags,
            }
        )
        if assign_to_group is not UNSET:
            field_dict["assign_to_group"] = assign_to_group
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if public is not UNSET:
            field_dict["public"] = public
        if updated_time is not UNSET:
            field_dict["updated_time"] = updated_time
        if welcome_message is not UNSET:
            field_dict["welcome_message"] = welcome_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.group import Group
        from ..models.image import Image
        from ..models.message import Message

        d = src_dict.copy()
        name = d.pop("name")

        tags = cast(list[str], d.pop("tags"))

        _assign_to_group = d.pop("assign_to_group", UNSET)
        assign_to_group: Union[Unset, Group]
        if isinstance(_assign_to_group, Unset):
            assign_to_group = UNSET
        else:
            assign_to_group = Group.from_dict(_assign_to_group)

        enabled = d.pop("enabled", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, Image]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = Image.from_dict(_icon)

        id = d.pop("id", UNSET)

        locale = d.pop("locale", UNSET)

        public = d.pop("public", UNSET)

        _updated_time = d.pop("updated_time", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        _welcome_message = d.pop("welcome_message", UNSET)
        welcome_message: Union[Unset, Message]
        if isinstance(_welcome_message, Unset):
            welcome_message = UNSET
        else:
            welcome_message = Message.from_dict(_welcome_message)

        channel = cls(
            name=name,
            tags=tags,
            assign_to_group=assign_to_group,
            enabled=enabled,
            icon=icon,
            id=id,
            locale=locale,
            public=public,
            updated_time=updated_time,
            welcome_message=welcome_message,
        )

        channel.additional_properties = d
        return channel

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
