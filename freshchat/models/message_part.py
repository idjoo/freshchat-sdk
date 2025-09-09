from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.callback_part import CallbackPart
    from ..models.collection_part import CollectionPart
    from ..models.image_part import ImagePart
    from ..models.quick_reply_button_part import QuickReplyButtonPart
    from ..models.reference_part import ReferencePart
    from ..models.template_content import TemplateContent
    from ..models.text_part import TextPart
    from ..models.url_button_part import UrlButtonPart


T = TypeVar("T", bound="MessagePart")


@_attrs_define
class MessagePart:
    """message part model. Exactly one part should be present

    Attributes:
        callback (Union[Unset, CallbackPart]): callback part
        collection (Union[Unset, CollectionPart]): collection part
        image (Union[Unset, ImagePart]): image part
        quick_reply_button (Union[Unset, QuickReplyButtonPart]): quick reply button part
        reference (Union[Unset, ReferencePart]): Reference Part
        template_content (Union[Unset, TemplateContent]): dynamic message template content part
        text (Union[Unset, TextPart]): text part
        url_button (Union[Unset, UrlButtonPart]): url button part
    """

    callback: Union[Unset, "CallbackPart"] = UNSET
    collection: Union[Unset, "CollectionPart"] = UNSET
    image: Union[Unset, "ImagePart"] = UNSET
    quick_reply_button: Union[Unset, "QuickReplyButtonPart"] = UNSET
    reference: Union[Unset, "ReferencePart"] = UNSET
    template_content: Union[Unset, "TemplateContent"] = UNSET
    text: Union[Unset, "TextPart"] = UNSET
    url_button: Union[Unset, "UrlButtonPart"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        collection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.collection, Unset):
            collection = self.collection.to_dict()

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        quick_reply_button: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quick_reply_button, Unset):
            quick_reply_button = self.quick_reply_button.to_dict()

        reference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()

        template_content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_content, Unset):
            template_content = self.template_content.to_dict()

        text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        url_button: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.url_button, Unset):
            url_button = self.url_button.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callback is not UNSET:
            field_dict["callback"] = callback
        if collection is not UNSET:
            field_dict["collection"] = collection
        if image is not UNSET:
            field_dict["image"] = image
        if quick_reply_button is not UNSET:
            field_dict["quick_reply_button"] = quick_reply_button
        if reference is not UNSET:
            field_dict["reference"] = reference
        if template_content is not UNSET:
            field_dict["template_content"] = template_content
        if text is not UNSET:
            field_dict["text"] = text
        if url_button is not UNSET:
            field_dict["url_button"] = url_button

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.callback_part import CallbackPart
        from ..models.collection_part import CollectionPart
        from ..models.image_part import ImagePart
        from ..models.quick_reply_button_part import QuickReplyButtonPart
        from ..models.reference_part import ReferencePart
        from ..models.template_content import TemplateContent
        from ..models.text_part import TextPart
        from ..models.url_button_part import UrlButtonPart

        d = src_dict.copy()
        _callback = d.pop("callback", UNSET)
        callback: Union[Unset, CallbackPart]
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = CallbackPart.from_dict(_callback)

        _collection = d.pop("collection", UNSET)
        collection: Union[Unset, CollectionPart]
        if isinstance(_collection, Unset):
            collection = UNSET
        else:
            collection = CollectionPart.from_dict(_collection)

        _image = d.pop("image", UNSET)
        image: Union[Unset, ImagePart]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ImagePart.from_dict(_image)

        _quick_reply_button = d.pop("quick_reply_button", UNSET)
        quick_reply_button: Union[Unset, QuickReplyButtonPart]
        if isinstance(_quick_reply_button, Unset):
            quick_reply_button = UNSET
        else:
            quick_reply_button = QuickReplyButtonPart.from_dict(_quick_reply_button)

        _reference = d.pop("reference", UNSET)
        reference: Union[Unset, ReferencePart]
        if isinstance(_reference, Unset):
            reference = UNSET
        else:
            reference = ReferencePart.from_dict(_reference)

        _template_content = d.pop("template_content", UNSET)
        template_content: Union[Unset, TemplateContent]
        if isinstance(_template_content, Unset):
            template_content = UNSET
        else:
            template_content = TemplateContent.from_dict(_template_content)

        _text = d.pop("text", UNSET)
        text: Union[Unset, TextPart]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = TextPart.from_dict(_text)

        _url_button = d.pop("url_button", UNSET)
        url_button: Union[Unset, UrlButtonPart]
        if isinstance(_url_button, Unset):
            url_button = UNSET
        else:
            url_button = UrlButtonPart.from_dict(_url_button)

        message_part = cls(
            callback=callback,
            collection=collection,
            image=image,
            quick_reply_button=quick_reply_button,
            reference=reference,
            template_content=template_content,
            text=text,
            url_button=url_button,
        )

        message_part.additional_properties = d
        return message_part

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
