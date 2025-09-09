from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferencePart")


@_attrs_define
class ReferencePart:
    """Reference Part

    Attributes:
        label (str): label Example: string.
        reference_id (Union[Unset, str]): reference_id Example: 6c03caf2-a37f-45a2-a9a3-6e03aa7b85f9.
    """

    label: str
    reference_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        reference_id = self.reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        reference_id = d.pop("reference_id", UNSET)

        reference_part = cls(
            label=label,
            reference_id=reference_id,
        )

        reference_part.additional_properties = d
        return reference_part

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
