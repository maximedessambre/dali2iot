from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.circadian_step import CircadianStep


T = TypeVar("T", bound="CircadianCurve")


@_attrs_define
class CircadianCurve:
    """
    Attributes:
        day (int):
        month (int):
        steps (List['CircadianStep']):
    """

    day: int
    month: int
    steps: List["CircadianStep"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day
        month = self.month
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "month": month,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.circadian_step import CircadianStep

        d = src_dict.copy()
        day = d.pop("day")

        month = d.pop("month")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = CircadianStep.from_dict(steps_item_data)

            steps.append(steps_item)

        circadian_curve = cls(
            day=day,
            month=month,
            steps=steps,
        )

        circadian_curve.additional_properties = d
        return circadian_curve

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
