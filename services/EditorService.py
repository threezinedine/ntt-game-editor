import os
from models import *
from constants import *
from nttinject import *
from abc import *
from typing import *


class IEditorService(ABC):
    @abstractproperty
    def RecentProjects(self) -> List[str]:
        pass

    @abstractmethod
    def Load(self) -> None:
        pass

    @abstractmethod
    def ClearRecentProjects(self) -> None:
        pass

    @abstractmethod
    def AppendNewRecentProject(self, strProjectFile: str) -> None:
        pass


@dependency_inject(EditorData)
class EditorService(IEditorService):
    def __init__(self, mEditorData: EditorData) -> None:
        super().__init__()
        self._mEditorData = mEditorData

        self.Load()

    @property
    def RecentProjects(self) -> List[str]:
        return self._mEditorData.RecentProjects

    def Load(self) -> None:
        try:
            self._mEditorData.FromFile(EDITOR_DATA_JSON)
        except:
            self._SaveEditorData()

    def _SaveEditorData(self) -> None:
        self._mEditorData.ToFile(EDITOR_DATA_JSON)

    def ClearRecentProjects(self) -> None:
        self._mEditorData.RecentProjects.clear()
        self._SaveEditorData()

    def AppendNewRecentProject(self, strProjectFile: str) -> None:
        for strFile in self._mEditorData.RecentProjects:
            if strProjectFile == strFile:
                self._mEditorData.RecentProjects.remove(strProjectFile)
                break

        self._mEditorData.RecentProjects.append(strProjectFile)
        self._SaveEditorData()


def Create_EditorService(*args, **kwargs) -> IEditorService:
    return EditorService(*args, **kwargs)
