import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reports_api_request_aggregator import ReportsApiRequestAggregator
from ..models.reports_api_request_filter_by import ReportsApiRequestFilterBy
from ..models.reports_api_request_name import ReportsApiRequestName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportsApiRequest")


@_attrs_define
class ReportsApiRequest:
    """Request body for reports api post request

    Attributes:
        end (datetime.date):
        name (ReportsApiRequestName): report name to query Example: string.
        start (datetime.date):
        aggregator (Union[Unset, ReportsApiRequestAggregator]): list of aggregators which can be applied Example:
            string.
        filter_by (Union[Unset, ReportsApiRequestFilterBy]): filtering params Example: group%3D1%2Cgroup%3D2.
    """

    end: datetime.date
    name: ReportsApiRequestName
    start: datetime.date
    aggregator: Union[Unset, ReportsApiRequestAggregator] = UNSET
    filter_by: Union[Unset, ReportsApiRequestFilterBy] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        name = self.name.value

        start = self.start.isoformat()

        aggregator: Union[Unset, str] = UNSET
        if not isinstance(self.aggregator, Unset):
            aggregator = self.aggregator.value

        filter_by: Union[Unset, str] = UNSET
        if not isinstance(self.filter_by, Unset):
            filter_by = self.filter_by.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "name": name,
                "start": start,
            }
        )
        if aggregator is not UNSET:
            field_dict["aggregator"] = aggregator
        if filter_by is not UNSET:
            field_dict["filter_by"] = filter_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end = isoparse(d.pop("end")).date()

        name = ReportsApiRequestName(d.pop("name"))

        start = isoparse(d.pop("start")).date()

        _aggregator = d.pop("aggregator", UNSET)
        aggregator: Union[Unset, ReportsApiRequestAggregator]
        if isinstance(_aggregator, Unset):
            aggregator = UNSET
        else:
            aggregator = ReportsApiRequestAggregator(_aggregator)

        _filter_by = d.pop("filter_by", UNSET)
        filter_by: Union[Unset, ReportsApiRequestFilterBy]
        if isinstance(_filter_by, Unset):
            filter_by = UNSET
        else:
            filter_by = ReportsApiRequestFilterBy(_filter_by)

        reports_api_request = cls(
            end=end,
            name=name,
            start=start,
            aggregator=aggregator,
            filter_by=filter_by,
        )

        reports_api_request.additional_properties = d
        return reports_api_request

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
