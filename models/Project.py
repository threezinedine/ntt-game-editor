import ntt_json_model
import ntt_observable_list

from .Scene import Scene


class Project(ntt_json_model.ModelBase):
    def __init__(self) -> None:
        super().__init__()

        ntt_json_model.StrProperty(self, "", "_strProjectName")
        ntt_json_model.ListProperty(self, [], "_strFolders")
        ntt_json_model.ListProperty(self, [], "_mScenes")

    @property
    def ProjectName(self) -> str:
        return self._strProjectName.GetValue()

    @ProjectName.setter
    def ProjectName(self, strProjectName: str) -> None:
        self._strProjectName.SetValue(strProjectName)

    @property
    def Folders(self) -> ntt_observable_list.ObservableList[str]:
        return self._strFolders.GetValue()

    @property
    def Scenes(self) -> ntt_observable_list.ObservableList[Scene]:
        return self._mScenes.GetValue()

    def __repr__(self) -> str:
        return f'<Project id={id(self)} name="{self._strProjectName}"/>'


ntt_json_model.ModelBase.mSubModels[Project.__name__] = Project
