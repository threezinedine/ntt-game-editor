from ntt_json_model import *


class EditorData(ModelBase):
    def __init__(self) -> None:
        super().__init__()

        ListProperty(self, [], "_strRecentProjectFiles")
        BoolProperty(self, False, "_bDarkMode")

    @property
    def RecentProjects(self) -> List[str]:
        return self._strRecentProjectFiles.GetValue()

    @property
    def DarkMode(self) -> bool:
        return self._bDarkMode.GetValue()

    @DarkMode.setter
    def DarkMode(self, bDarkMode: bool) -> None:
        self._bDarkMode.SetValue(bDarkMode)


ModelBase.mSubModels[EditorData.__name__] = EditorData
