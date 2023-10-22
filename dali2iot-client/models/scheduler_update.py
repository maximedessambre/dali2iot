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


T = TypeVar("T", bound="SchedulerUpdate")


@_attrs_define
class SchedulerUpdate:
    """
    Attributes:
        name (Union[Unset, str]):
        targets (Union[Unset, List['DeviceModel']]):
        enabled (Union[Unset, bool]):
        active_period (Union[Unset, ActivePeriod]):
        active_months (Union[Unset, ActiveMonths]):
        active_weekdays (Union[Unset, ActiveWeekDays]):
        active_days (Union[Unset, ActiveDays]):
        recall_mode (Union[Unset, SchedulerRecallModes]): An enumeration.
        recall_time (Union[Unset, SchedulerTime]):
        action (Union[Unset, SchedulerAction]):
    """

    name: Union[Unset, str] = UNSET
    targets: Union[Unset, List["DeviceModel"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    active_period: Union[Unset, "ActivePeriod"] = UNSET
    active_months: Union[Unset, "ActiveMonths"] = UNSET
    active_weekdays: Union[Unset, "ActiveWeekDays"] = UNSET
    active_days: Union[Unset, "ActiveDays"] = UNSET
    recall_mode: Union[Unset, SchedulerRecallModes] = UNSET
    recall_time: Union[Unset, "SchedulerTime"] = UNSET
    action: Union[Unset, "SchedulerAction"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

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

        recall_mode: Union[Unset, str] = UNSET
        if not isinstance(self.recall_mode, Unset):
            recall_mode = self.recall_mode.value

        recall_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recall_time, Unset):
            recall_time = self.recall_time.to_dict()

        action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if targets is not UNSET:
            field_dict["targets"] = targets
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
        if recall_mode is not UNSET:
            field_dict["recallMode"] = recall_mode
        if recall_time is not UNSET:
            field_dict["recallTime"] = recall_time
        if action is not UNSET:
            field_dict["action"] = action

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
        name = d.pop("name", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

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

        _recall_mode = d.pop("recallMode", UNSET)
        recall_mode: Union[Unset, SchedulerRecallModes]
        if isinstance(_recall_mode, Unset):
            recall_mode = UNSET
        else:
            recall_mode = SchedulerRecallModes(_recall_mode)

        _recall_time = d.pop("recallTime", UNSET)
        recall_time: Union[Unset, SchedulerTime]
        if isinstance(_recall_time, Unset):
            recall_time = UNSET
        else:
            recall_time = SchedulerTime.from_dict(_recall_time)

        _action = d.pop("action", UNSET)
        action: Union[Unset, SchedulerAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = SchedulerAction.from_dict(_action)

        scheduler_update = cls(
            name=name,
            targets=targets,
            enabled=enabled,
            active_period=active_period,
            active_months=active_months,
            active_weekdays=active_weekdays,
            active_days=active_days,
            recall_mode=recall_mode,
            recall_time=recall_time,
            action=action,
        )

        scheduler_update.additional_properties = d
        return scheduler_update

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
