from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_template_storage import MessageTemplateStorage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language
    from ..models.rich_media_template_data import RichMediaTemplateData
    from ..models.template_data import TemplateData


T = TypeVar("T", bound="MessageTemplate")


@_attrs_define
class MessageTemplate:
    """whatsapp message template

    Attributes:
        language (Language): language
        namespace (str): Whatsapp template namespace Example: XXXXXXXX_XXXX_XXXX_XXXX_XXXXXXXXXXXX.
        storage (MessageTemplateStorage): storage Example: none.
        template_data (list['TemplateData']): template_data
        template_name (str): whatsapp template name Example: hello_world.
        rich_template_data (Union[Unset, RichMediaTemplateData]): for rich media contents
    """

    language: "Language"
    namespace: str
    storage: MessageTemplateStorage
    template_data: list["TemplateData"]
    template_name: str
    rich_template_data: Union[Unset, "RichMediaTemplateData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language.to_dict()

        namespace = self.namespace

        storage = self.storage.value

        template_data = []
        for template_data_item_data in self.template_data:
            template_data_item = template_data_item_data.to_dict()
            template_data.append(template_data_item)

        template_name = self.template_name

        rich_template_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rich_template_data, Unset):
            rich_template_data = self.rich_template_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "namespace": namespace,
                "storage": storage,
                "template_data": template_data,
                "template_name": template_name,
            }
        )
        if rich_template_data is not UNSET:
            field_dict["rich_template_data"] = rich_template_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.language import Language
        from ..models.rich_media_template_data import RichMediaTemplateData
        from ..models.template_data import TemplateData

        d = src_dict.copy()
        language = Language.from_dict(d.pop("language"))

        namespace = d.pop("namespace")

        storage = MessageTemplateStorage(d.pop("storage"))

        template_data = []
        _template_data = d.pop("template_data")
        for template_data_item_data in _template_data:
            template_data_item = TemplateData.from_dict(template_data_item_data)

            template_data.append(template_data_item)

        template_name = d.pop("template_name")

        _rich_template_data = d.pop("rich_template_data", UNSET)
        rich_template_data: Union[Unset, RichMediaTemplateData]
        if isinstance(_rich_template_data, Unset):
            rich_template_data = UNSET
        else:
            rich_template_data = RichMediaTemplateData.from_dict(_rich_template_data)

        message_template = cls(
            language=language,
            namespace=namespace,
            storage=storage,
            template_data=template_data,
            template_name=template_name,
            rich_template_data=rich_template_data,
        )

        message_template.additional_properties = d
        return message_template

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
