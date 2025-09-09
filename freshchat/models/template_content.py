from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_content_type import TemplateContentType

if TYPE_CHECKING:
    from ..models.sections import Sections


T = TypeVar("T", bound="TemplateContent")


@_attrs_define
class TemplateContent:
    """dynamic message template content part

    Attributes:
        sections (list['Sections']): sections
        type_ (TemplateContentType): type Example: quick_reply_dropdown.
    """

    sections: list["Sections"]
    type_: TemplateContentType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sections": sections,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sections import Sections

        d = src_dict.copy()
        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = Sections.from_dict(sections_item_data)

            sections.append(sections_item)

        type_ = TemplateContentType(d.pop("type"))

        template_content = cls(
            sections=sections,
            type_=type_,
        )

        template_content.additional_properties = d
        return template_content

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
