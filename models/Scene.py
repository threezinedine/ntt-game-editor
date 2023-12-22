import ntt_json_model


class Scene(ntt_json_model.ModelBase):
    def __init__(
        self,
        strSceneName: str = "Default Scene",
    ) -> None:
        super().__init__()

        ntt_json_model.StrProperty(
            self,
            strSceneName,
            "_strSceneName",
        )

    @property
    def SceneName(self) -> str:
        return self._strSceneName.GetValue()

    @SceneName.setter
    def SceneName(self, strSceneName: str) -> None:
        return self._strSceneName.SetValue(strSceneName)


ntt_json_model.ModelBase.mSubModels[Scene.__name__] = Scene
