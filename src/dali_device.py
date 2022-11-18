DALI_DEVICE_DEFAULT = "default"
DALI_DEVICE_LIGHT = "switchable"
DALI_DEVICE_LIGHT_DIM = "dimmable"


class DaliDevice:
    """
    DaliDevice super class. Represent any dali devices
    """

    def __init__(
            self,
            id: int,
            name: str,
            info: str,
            type: str = DALI_DEVICE_DEFAULT,
            features=None,
            scenes=None,
            groups=None,
    ):

        if groups is None:
            groups = []
        if scenes is None:
            scenes = []
        if features is None:
            features = {}

        self._id = id
        self._name = name
        self._info = info
        self._type = type
        self._features = features
        self._scenes = scenes
        self._groups = groups


    def __repr__(self):
        return f"Dali device {self.name} ({self.id})"

    def __str__(self):
        return f"{self.name} ({self.id})"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def info(self):
        return self._info

    @property
    def type(self):
        return self._type

    @property
    def features(self):
        return self._features

    def update(self, kargs):
        self._features.update(kargs)
        # {"id": 6, "features": {"switchable": {"status": false}, "dimmable": {"status": 0.0}}}
