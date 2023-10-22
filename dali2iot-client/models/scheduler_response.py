from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scheduler_recall_modes import SchedulerRecallModes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_days import ActiveDays
    from ..models.active_months import ActiveMonths
    from ..models.active_period import ActivePeriod
    from ..models.active_week_days import ActiveWeekDays
    from ..models.device_model import DeviceModel
    from ..models.scheduler_action import SchedulerAction
    from ..models.scheduler_time import SchedulerTime


T = TypeVar("T", bound="SchedulerResponse")


@_attrs_define
class SchedulerResponse:
    """
    Attributes:
        targets (List['DeviceModel']):
        recall_mode (SchedulerRecallModes): An enumeration.
        recall_time (SchedulerTime):
        action (SchedulerAction):
        id (int):
        name (Union[Unset, str]):  Default: ''.
        enabled (Union[Unset, bool]):  Default: True.
        active_period (Union[Unset, ActivePeriod]):
        active_months (Union[Unset, ActiveMonths]):
        active_weekdays (Union[Unset, ActiveWeekDays]):
        active_days (Union[Unset, ActiveDays]):
    """

    targets: List["DeviceModel"]
    recall_mode: SchedulerRecallModes
    recall_time: "SchedulerTime"
    action: "SchedulerAction"
    id: int
    name: Union[Unset, str] = ""
    enabled: Union[Unset, bool] = True
    active_period: Union[Unset, "ActivePeriod"] = UNSET
    active_months: Union[Unset, "ActiveMonths"] = UNSET
    active_weekdays: Union[Unset, "ActiveWeekDays"] = UNSET
    active_days: Union[Unset, "ActiveDays"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        recall_mode = self.recall_mode.value

        recall_time = self.recall_time.to_dict()

        action = self.action.to_dict()

        id = self.id
        name = self.name
        enabled = self.enabled
        active_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_period, Unset):
            active_period = self.active_period.to_dict()

        active_months: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_months, Unset):
            active_months = self.active_months.to_dict()

        active_weekdays: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_weekdays, Unset):
            active_weekdays = self.active_weekdays.to_dict()

        active_days: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_days, Unset):
            active_days = self.active_days.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
                "recallMode": recall_mode,
                "recallTime": recall_time,
                "action": action,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if active_period is not UNSET:
            field_dict["activePeriod"] = active_period
        if active_months is not UNSET:
            field_dict["activeMonths"] = active_months
        if active_weekdays is not UNSET:
            field_dict["activeWeekdays"] = active_weekdays
        if active_days is not UNSET:
            field_dict["activeDays"] = active_days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.active_days import ActiveDays
        from ..models.active_months import ActiveMonths
        from ..models.active_period import ActivePeriod
        from ..models.active_week_days import ActiveWeekDays
        from ..models.device_model import DeviceModel
        from ..models.scheduler_action import SchedulerAction
        from ..models.scheduler_time import SchedulerTime

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        recall_mode = SchedulerRecallModes(d.pop("recallMode"))

        recall_time = SchedulerTime.from_dict(d.pop("recallTime"))

        action = SchedulerAction.from_dict(d.pop("action"))

        id = d.pop("id")

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _active_period = d.pop("activePeriod", UNSET)
        active_period: Union[Unset, ActivePeriod]
        if isinstance(_active_period, Unset):
            active_period = UNSET
        else:
            active_period = ActivePeriod.from_dict(_active_period)

        _active_months = d.pop("activeMonths", UNSET)
        active_months: Union[Unset, ActiveMonths]
        if isinstance(_active_months, Unset):
            active_months = UNSET
        else:
            active_months = ActiveMonths.from_dict(_active_months)

        _active_weekdays = d.pop("activeWeekdays", UNSET)
        active_weekdays: Union[Unset, ActiveWeekDays]
        if isinstance(_active_weekdays, Unset):
            active_weekdays = UNSET
        else:
            active_weekdays = ActiveWeekDays.from_dict(_active_weekdays)

        _active_days = d.pop("activeDays", UNSET)
        active_days: Union[Unset, ActiveDays]
        if isinstance(_active_days, Unset):
            active_days = UNSET
        else:
            active_days = ActiveDays.from_dict(_active_days)

        scheduler_response = cls(
            targets=targets,
            recall_mode=recall_mode,
            recall_time=recall_time,
            action=action,
            id=id,
            name=name,
            enabled=enabled,
            active_period=active_period,
            active_months=active_months,
            active_weekdays=active_weekdays,
            active_days=active_days,
        )

        scheduler_response.additional_properties = d
        return scheduler_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
