from .dali_device import *

class DaliLight(DaliDevice):
    """
    Dali Light device
    """

    def __init__(
        self,
        id: int,
        name: str,
        info: str,
        type: str,
        features=None,
        scenes=None,
        groups=None,
    ):
        super().__init__(
            id=id,
            name=name,
            info=info,
            type=DALI_DEVICE_LIGHT,
            features=features,
            scenes=scenes,
            groups=groups,
        )

    @property
    def is_on(self) -> bool:
        return self.features["switchable"]["status"]

