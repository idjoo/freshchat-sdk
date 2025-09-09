from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thumbnail import Thumbnail


T = TypeVar("T", bound="ImageResponse")


@_attrs_define
class ImageResponse:
    """image model

    Attributes:
        content_type (Union[Unset, str]):  Example: image/jpg.
        height (Union[Unset, int]):  Example: 200.
        id (Union[Unset, str]):  Example: 96738e3d-9473-45c5-9eeb-cfe5e4da2434.
        name (Union[Unset, str]):  Example: img_1604986580513.jpeg.
        thumbnail (Union[Unset, Thumbnail]): thumbnail model
        url (Union[Unset, str]):  Example: https://chat.s3.amazonaws.com/f_marketingpicFull/u_8ace8de9b2545716308776dc1d
            f471f347f1057db625ce8ee57b713146b8023a/img_1602510533617.png.
        width (Union[Unset, int]):  Example: 100.
    """

    content_type: Union[Unset, str] = UNSET
    height: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    thumbnail: Union[Unset, "Thumbnail"] = UNSET
    url: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        height = self.height

        id = self.id

        name = self.name

        thumbnail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        url = self.url

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.thumbnail import Thumbnail

        d = src_dict.copy()
        content_type = d.pop("content_type", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: Union[Unset, Thumbnail]
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = Thumbnail.from_dict(_thumbnail)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        image_response = cls(
            content_type=content_type,
            height=height,
            id=id,
            name=name,
            thumbnail=thumbnail,
            url=url,
            width=width,
        )

        image_response.additional_properties = d
        return image_response

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
