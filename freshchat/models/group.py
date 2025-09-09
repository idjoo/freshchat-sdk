from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent import Agent


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """group model

    Attributes:
        agents (list['Agent']):
        id (str): id Example: 6c03caf2-a37f-45a2-a9a3-6e03aa7b85f5.
        name (str): name Example: Support.
        description (Union[Unset, str]): description Example: Support.
        routing_type (Union[Unset, str]): routing_type Example: OCR,DISABLED.
    """

    agents: list["Agent"]
    id: str
    name: str
    description: Union[Unset, str] = UNSET
    routing_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        id = self.id

        name = self.name

        description = self.description

        routing_type = self.routing_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents": agents,
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if routing_type is not UNSET:
            field_dict["routing_type"] = routing_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.agent import Agent

        d = src_dict.copy()
        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = Agent.from_dict(agents_item_data)

            agents.append(agents_item)

        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        routing_type = d.pop("routing_type", UNSET)

        group = cls(
            agents=agents,
            id=id,
            name=name,
            description=description,
            routing_type=routing_type,
        )

        group.additional_properties = d
        return group

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
