import ntt_json_model
import typing


class Project(ntt_json_model.ModelBase):
    def __init__(self) -> None:
        super().__init__()

        ntt_json_model.StrProperty(self, "", "_strProjectName")
        ntt_json_model.ListProperty(self, [], "_strFolders")

    @property
    def ProjectName(self) -> str:
        return self._strProjectName.GetValue()

    @ProjectName.setter
    def ProjectName(self, strProjectName: str) -> None:
        self._strProjectName.SetValue(strProjectName)

    @property
    def Folders(self) -> typing.List[str]:
        return self._strFolders.GetValue()

    def __repr__(self) -> str:
        return f'<Project id={id(self)} name="{self._strProjectName}"/>'


ntt_json_model.ModelBase.mSubModels[Project.__name__] = Project
