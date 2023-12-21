from ntt_json_model import *


class Project(ModelBase):
    def __init__(self) -> None:
        super().__init__()

        StrProperty(self, "", "_strProjectName")
        ListProperty(self, [], "_strFolders")

    @property
    def ProjectName(self) -> str:
        return self._strProjectName.GetValue()

    @ProjectName.setter
    def ProjectName(self, strProjectName: str) -> None:
        self._strProjectName.SetValue(strProjectName)

    @property
    def Folders(self) -> List[str]:
        return self._strFolders.GetValue()

    def __repr__(self) -> str:
        return f'<Project id={id(self)} name="{self._strProjectName}"/>'


ModelBase.mSubModels[Project.__name__] = Project
