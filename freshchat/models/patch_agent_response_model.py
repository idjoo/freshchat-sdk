from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_agent_response_model_availability_status import PatchAgentResponseModelAvailabilityStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status import Status


T = TypeVar("T", bound="PatchAgentResponseModel")


@_attrs_define
class PatchAgentResponseModel:
    """patch agent model

    Attributes:
        agent_status (Union[Unset, Status]): Status model
        availability_status (Union[Unset, PatchAgentResponseModelAvailabilityStatus]):  Example: AVAILABLE.
    """

    agent_status: Union[Unset, "Status"] = UNSET
    availability_status: Union[Unset, PatchAgentResponseModelAvailabilityStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.agent_status, Unset):
            agent_status = self.agent_status.to_dict()

        availability_status: Union[Unset, str] = UNSET
        if not isinstance(self.availability_status, Unset):
            availability_status = self.availability_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_status is not UNSET:
            field_dict["agent_status"] = agent_status
        if availability_status is not UNSET:
            field_dict["availability_status"] = availability_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.status import Status

        d = src_dict.copy()
        _agent_status = d.pop("agent_status", UNSET)
        agent_status: Union[Unset, Status]
        if isinstance(_agent_status, Unset):
            agent_status = UNSET
        else:
            agent_status = Status.from_dict(_agent_status)

        _availability_status = d.pop("availability_status", UNSET)
        availability_status: Union[Unset, PatchAgentResponseModelAvailabilityStatus]
        if isinstance(_availability_status, Unset):
            availability_status = UNSET
        else:
            availability_status = PatchAgentResponseModelAvailabilityStatus(_availability_status)

        patch_agent_response_model = cls(
            agent_status=agent_status,
            availability_status=availability_status,
        )

        patch_agent_response_model.additional_properties = d
        return patch_agent_response_model

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
