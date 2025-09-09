from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel
    from ..models.links import Links
    from ..models.pagination import Pagination


T = TypeVar("T", bound="Channels")


@_attrs_define
class Channels:
    """channels model

    Attributes:
        channels (Union[Unset, list['Channel']]):
        links (Union[Unset, Links]): links model
        pagination (Union[Unset, Pagination]): pagination model
    """

    channels: Union[Unset, list["Channel"]] = UNSET
    links: Union[Unset, "Links"] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if links is not UNSET:
            field_dict["links"] = links
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.channel import Channel
        from ..models.links import Links
        from ..models.pagination import Pagination

        d = src_dict.copy()
        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = Channel.from_dict(channels_item_data)

            channels.append(channels_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        channels = cls(
            channels=channels,
            links=links,
            pagination=pagination,
        )

        channels.additional_properties = d
        return channels

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
