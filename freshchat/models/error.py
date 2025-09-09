from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_message import ErrorMessage
from ..models.error_status import ErrorStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """error model

    Attributes:
        code (int):  Example: 404.
        message (ErrorMessage):  Example: Agent does not exist.
        status (ErrorStatus):  Example: AGENT_NOT_FOUND.
        details (Union[Unset, list['ErrorDetail']]):
    """

    code: int
    message: ErrorMessage
    status: ErrorStatus
    details: Union[Unset, list["ErrorDetail"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message.value

        status = self.status.value

        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "status": status,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail

        d = src_dict.copy()
        code = d.pop("code")

        message = ErrorMessage(d.pop("message"))

        status = ErrorStatus(d.pop("status"))

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = ErrorDetail.from_dict(details_item_data)

            details.append(details_item)

        error = cls(
            code=code,
            message=message,
            status=status,
            details=details,
        )

        error.additional_properties = d
        return error

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
