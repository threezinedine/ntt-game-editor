import ntt_json_model
import typing


class EditorData(ntt_json_model.ModelBase):
    def __init__(self) -> None:
        super().__init__()

        ntt_json_model.ListProperty(self, [], "_strRecentProjectFiles")
        ntt_json_model.BoolProperty(self, False, "_bDarkMode")

    @property
    def RecentProjects(self) -> typing.List[str]:
        return self._strRecentProjectFiles.GetValue()

    @property
    def DarkMode(self) -> bool:
        return self._bDarkMode.GetValue()

    @DarkMode.setter
    def DarkMode(self, bDarkMode: bool) -> None:
        self._bDarkMode.SetValue(bDarkMode)


ntt_json_model.ModelBase.mSubModels[EditorData.__name__] = EditorData
