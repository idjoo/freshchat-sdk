from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.pagination import Pagination
    from ..models.role import Role


T = TypeVar("T", bound="Roles")


@_attrs_define
class Roles:
    """roles model

    Attributes:
        links (Union[Unset, Links]): links model
        pagination (Union[Unset, Pagination]): pagination model
        roles (Union[Unset, list['Role']]):
    """

    links: Union[Unset, "Links"] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    roles: Union[Unset, list["Role"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.pagination import Pagination
        from ..models.role import Role

        d = src_dict.copy()
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

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

        roles = cls(
            links=links,
            pagination=pagination,
            roles=roles,
        )

        roles.additional_properties = d
        return roles

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
