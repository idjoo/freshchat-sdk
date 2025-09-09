from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.params import Params


T = TypeVar("T", bound="Header")


@_attrs_define
class Header:
    """header for components

    Attributes:
        media_url (str): media_url Example: https://sample.in/sample.jpg.
        type_ (str): type Example: image.
        params (Union[Unset, list['Params']]): text params
    """

    media_url: str
    type_: str
    params: Union[Unset, list["Params"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_url = self.media_url

        type_ = self.type_

        params: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()
                params.append(params_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media_url": media_url,
                "type": type_,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.params import Params

        d = src_dict.copy()
        media_url = d.pop("media_url")

        type_ = d.pop("type")

        params = []
        _params = d.pop("params", UNSET)
        for params_item_data in _params or []:
            params_item = Params.from_dict(params_item_data)

            params.append(params_item)

        header = cls(
            media_url=media_url,
            type_=type_,
            params=params,
        )

        header.additional_properties = d
        return header

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
