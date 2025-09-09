from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status import Status


T = TypeVar("T", bound="StatusList")


@_attrs_define
class StatusList:
    """List of status

    Attributes:
        states (Union[Unset, list['Status']]):
    """

    states: Union[Unset, list["Status"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        states: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.status import Status

        d = src_dict.copy()
        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            states_item = Status.from_dict(states_item_data)

            states.append(states_item)

        status_list = cls(
            states=states,
        )

        status_list.additional_properties = d
        return status_list

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
