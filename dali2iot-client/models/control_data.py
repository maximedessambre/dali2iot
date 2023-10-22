from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.color_kelvin_with_fade_data import ColorKelvinWithFadeData
    from ..models.color_rgb_data import ColorRGBData
    from ..models.color_rgb_with_fade_data import ColorRGBWithFadeData
    from ..models.color_waf_data import ColorWAFData
    from ..models.color_waf_with_fade_data import ColorWAFWithFadeData
    from ..models.color_xy_data import ColorXYData
    from ..models.color_xy_with_fade_data import ColorXYWithFadeData
    from ..models.dimmable_with_fade_data import DimmableWithFadeData
    from ..models.scene_with_fade_data import SceneWithFadeData
    from ..models.with_fade_time_data import WithFadeTimeData


T = TypeVar("T", bound="ControlData")


@_attrs_define
class ControlData:
    """
    Attributes:
        switchable (Union[Unset, bool]): Whether to switch a device on (``true``) or off (``false``). Example: True.
        dimmable (Union[Unset, float]): Percentage in the [0, 100] interval to dim a device to. Example: 50.0.
        dimmable_with_fade (Union[Unset, DimmableWithFadeData]):
        goto_last_active (Union[Unset, bool]): Value must be ``true``. Example: True.
        goto_last_active_with_fade (Union[Unset, WithFadeTimeData]):
        scene (Union[Unset, int]): Scene number of the scene to recall. Example: 15.
        scene_with_fade (Union[Unset, SceneWithFadeData]):
        fade_time (Union[Unset, float]): Set the fade time in seconds. Example: 1.0.
        fade_rate (Union[Unset, float]): Set the fade rate in steps per second. Example: 15.8.
        save_to_scene (Union[Unset, int]): Scene number of the scene to save to. Example: 15.
        color_rgb (Union[Unset, ColorRGBData]): Data model for the ``colorRGB`` feature.
        color_rgb_with_fade (Union[Unset, ColorRGBWithFadeData]):
        color_waf (Union[Unset, ColorWAFData]): Data model for the ``colorWAF`` feature.
        color_waf_with_fade (Union[Unset, ColorWAFWithFadeData]):
        color_kelvin (Union[Unset, float]): Color temperature in Kelvin. Example: 4000.0.
        color_kelvin_with_fade (Union[Unset, ColorKelvinWithFadeData]):
        color_xy (Union[Unset, ColorXYData]): Data model for the ``colorXY`` feature.
        color_xy_with_fade (Union[Unset, ColorXYWithFadeData]):
    """

    switchable: Union[Unset, bool] = UNSET
    dimmable: Union[Unset, float] = UNSET
    dimmable_with_fade: Union[Unset, "DimmableWithFadeData"] = UNSET
    goto_last_active: Union[Unset, bool] = UNSET
    goto_last_active_with_fade: Union[Unset, "WithFadeTimeData"] = UNSET
    scene: Union[Unset, int] = UNSET
    scene_with_fade: Union[Unset, "SceneWithFadeData"] = UNSET
    fade_time: Union[Unset, float] = UNSET
    fade_rate: Union[Unset, float] = UNSET
    save_to_scene: Union[Unset, int] = UNSET
    color_rgb: Union[Unset, "ColorRGBData"] = UNSET
    color_rgb_with_fade: Union[Unset, "ColorRGBWithFadeData"] = UNSET
    color_waf: Union[Unset, "ColorWAFData"] = UNSET
    color_waf_with_fade: Union[Unset, "ColorWAFWithFadeData"] = UNSET
    color_kelvin: Union[Unset, float] = UNSET
    color_kelvin_with_fade: Union[Unset, "ColorKelvinWithFadeData"] = UNSET
    color_xy: Union[Unset, "ColorXYData"] = UNSET
    color_xy_with_fade: Union[Unset, "ColorXYWithFadeData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        switchable = self.switchable
        dimmable = self.dimmable
        dimmable_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dimmable_with_fade, Unset):
            dimmable_with_fade = self.dimmable_with_fade.to_dict()

        goto_last_active = self.goto_last_active
        goto_last_active_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.goto_last_active_with_fade, Unset):
            goto_last_active_with_fade = self.goto_last_active_with_fade.to_dict()

        scene = self.scene
        scene_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scene_with_fade, Unset):
            scene_with_fade = self.scene_with_fade.to_dict()

        fade_time = self.fade_time
        fade_rate = self.fade_rate
        save_to_scene = self.save_to_scene
        color_rgb: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_rgb, Unset):
            color_rgb = self.color_rgb.to_dict()

        color_rgb_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_rgb_with_fade, Unset):
            color_rgb_with_fade = self.color_rgb_with_fade.to_dict()

        color_waf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_waf, Unset):
            color_waf = self.color_waf.to_dict()

        color_waf_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_waf_with_fade, Unset):
            color_waf_with_fade = self.color_waf_with_fade.to_dict()

        color_kelvin = self.color_kelvin
        color_kelvin_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_kelvin_with_fade, Unset):
            color_kelvin_with_fade = self.color_kelvin_with_fade.to_dict()

        color_xy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_xy, Unset):
            color_xy = self.color_xy.to_dict()

        color_xy_with_fade: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color_xy_with_fade, Unset):
            color_xy_with_fade = self.color_xy_with_fade.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switchable is not UNSET:
            field_dict["switchable"] = switchable
        if dimmable is not UNSET:
            field_dict["dimmable"] = dimmable
        if dimmable_with_fade is not UNSET:
            field_dict["dimmableWithFade"] = dimmable_with_fade
        if goto_last_active is not UNSET:
            field_dict["gotoLastActive"] = goto_last_active
        if goto_last_active_with_fade is not UNSET:
            field_dict["gotoLastActiveWithFade"] = goto_last_active_with_fade
        if scene is not UNSET:
            field_dict["scene"] = scene
        if scene_with_fade is not UNSET:
            field_dict["sceneWithFade"] = scene_with_fade
        if fade_time is not UNSET:
            field_dict["fadeTime"] = fade_time
        if fade_rate is not UNSET:
            field_dict["fadeRate"] = fade_rate
        if save_to_scene is not UNSET:
            field_dict["saveToScene"] = save_to_scene
        if color_rgb is not UNSET:
            field_dict["colorRGB"] = color_rgb
        if color_rgb_with_fade is not UNSET:
            field_dict["colorRGBWithFade"] = color_rgb_with_fade
        if color_waf is not UNSET:
            field_dict["colorWAF"] = color_waf
        if color_waf_with_fade is not UNSET:
            field_dict["colorWAFWithFade"] = color_waf_with_fade
        if color_kelvin is not UNSET:
            field_dict["colorKelvin"] = color_kelvin
        if color_kelvin_with_fade is not UNSET:
            field_dict["colorKelvinWithFade"] = color_kelvin_with_fade
        if color_xy is not UNSET:
            field_dict["colorXY"] = color_xy
        if color_xy_with_fade is not UNSET:
            field_dict["colorXYWithFade"] = color_xy_with_fade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.color_kelvin_with_fade_data import ColorKelvinWithFadeData
        from ..models.color_rgb_data import ColorRGBData
        from ..models.color_rgb_with_fade_data import ColorRGBWithFadeData
        from ..models.color_waf_data import ColorWAFData
        from ..models.color_waf_with_fade_data import ColorWAFWithFadeData
        from ..models.color_xy_data import ColorXYData
        from ..models.color_xy_with_fade_data import ColorXYWithFadeData
        from ..models.dimmable_with_fade_data import DimmableWithFadeData
        from ..models.scene_with_fade_data import SceneWithFadeData
        from ..models.with_fade_time_data import WithFadeTimeData

        d = src_dict.copy()
        switchable = d.pop("switchable", UNSET)

        dimmable = d.pop("dimmable", UNSET)

        _dimmable_with_fade = d.pop("dimmableWithFade", UNSET)
        dimmable_with_fade: Union[Unset, DimmableWithFadeData]
        if isinstance(_dimmable_with_fade, Unset):
            dimmable_with_fade = UNSET
        else:
            dimmable_with_fade = DimmableWithFadeData.from_dict(_dimmable_with_fade)

        goto_last_active = d.pop("gotoLastActive", UNSET)

        _goto_last_active_with_fade = d.pop("gotoLastActiveWithFade", UNSET)
        goto_last_active_with_fade: Union[Unset, WithFadeTimeData]
        if isinstance(_goto_last_active_with_fade, Unset):
            goto_last_active_with_fade = UNSET
        else:
            goto_last_active_with_fade = WithFadeTimeData.from_dict(_goto_last_active_with_fade)

        scene = d.pop("scene", UNSET)

        _scene_with_fade = d.pop("sceneWithFade", UNSET)
        scene_with_fade: Union[Unset, SceneWithFadeData]
        if isinstance(_scene_with_fade, Unset):
            scene_with_fade = UNSET
        else:
            scene_with_fade = SceneWithFadeData.from_dict(_scene_with_fade)

        fade_time = d.pop("fadeTime", UNSET)

        fade_rate = d.pop("fadeRate", UNSET)

        save_to_scene = d.pop("saveToScene", UNSET)

        _color_rgb = d.pop("colorRGB", UNSET)
        color_rgb: Union[Unset, ColorRGBData]
        if isinstance(_color_rgb, Unset):
            color_rgb = UNSET
        else:
            color_rgb = ColorRGBData.from_dict(_color_rgb)

        _color_rgb_with_fade = d.pop("colorRGBWithFade", UNSET)
        color_rgb_with_fade: Union[Unset, ColorRGBWithFadeData]
        if isinstance(_color_rgb_with_fade, Unset):
            color_rgb_with_fade = UNSET
        else:
            color_rgb_with_fade = ColorRGBWithFadeData.from_dict(_color_rgb_with_fade)

        _color_waf = d.pop("colorWAF", UNSET)
        color_waf: Union[Unset, ColorWAFData]
        if isinstance(_color_waf, Unset):
            color_waf = UNSET
        else:
            color_waf = ColorWAFData.from_dict(_color_waf)

        _color_waf_with_fade = d.pop("colorWAFWithFade", UNSET)
        color_waf_with_fade: Union[Unset, ColorWAFWithFadeData]
        if isinstance(_color_waf_with_fade, Unset):
            color_waf_with_fade = UNSET
        else:
            color_waf_with_fade = ColorWAFWithFadeData.from_dict(_color_waf_with_fade)

        color_kelvin = d.pop("colorKelvin", UNSET)

        _color_kelvin_with_fade = d.pop("colorKelvinWithFade", UNSET)
        color_kelvin_with_fade: Union[Unset, ColorKelvinWithFadeData]
        if isinstance(_color_kelvin_with_fade, Unset):
            color_kelvin_with_fade = UNSET
        else:
            color_kelvin_with_fade = ColorKelvinWithFadeData.from_dict(_color_kelvin_with_fade)

        _color_xy = d.pop("colorXY", UNSET)
        color_xy: Union[Unset, ColorXYData]
        if isinstance(_color_xy, Unset):
            color_xy = UNSET
        else:
            color_xy = ColorXYData.from_dict(_color_xy)

        _color_xy_with_fade = d.pop("colorXYWithFade", UNSET)
        color_xy_with_fade: Union[Unset, ColorXYWithFadeData]
        if isinstance(_color_xy_with_fade, Unset):
            color_xy_with_fade = UNSET
        else:
            color_xy_with_fade = ColorXYWithFadeData.from_dict(_color_xy_with_fade)

        control_data = cls(
            switchable=switchable,
            dimmable=dimmable,
            dimmable_with_fade=dimmable_with_fade,
            goto_last_active=goto_last_active,
            goto_last_active_with_fade=goto_last_active_with_fade,
            scene=scene,
            scene_with_fade=scene_with_fade,
            fade_time=fade_time,
            fade_rate=fade_rate,
            save_to_scene=save_to_scene,
            color_rgb=color_rgb,
            color_rgb_with_fade=color_rgb_with_fade,
            color_waf=color_waf,
            color_waf_with_fade=color_waf_with_fade,
            color_kelvin=color_kelvin,
            color_kelvin_with_fade=color_kelvin_with_fade,
            color_xy=color_xy,
            color_xy_with_fade=color_xy_with_fade,
        )

        control_data.additional_properties = d
        return control_data

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
