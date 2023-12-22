import models
import typing
import constants
import nttinject
import abc


class IEditorService(abc.ABC):
    @abc.abstractproperty
    def RecentProjects(self) -> typing.List[str]:
        pass

    @abc.abstractmethod
    def Load(self) -> None:
        pass

    @abc.abstractmethod
    def ClearRecentProjects(self) -> None:
        pass

    @abc.abstractmethod
    def AppendNewRecentProject(self, strProjectFile: str) -> None:
        pass


@nttinject.dependency_inject(models.EditorData)
class EditorService(IEditorService):
    def __init__(
        self,
        mEditorData: models.EditorData,
    ) -> None:
        super().__init__()
        self._mEditorData = mEditorData

        self.Load()

    @property
    def RecentProjects(self) -> typing.List[str]:
        return self._mEditorData.RecentProjects

    def Load(self) -> None:
        try:
            self._mEditorData.FromFile(constants.EDITOR_DATA_JSON)
        except:
            self._SaveEditorData()

    def _SaveEditorData(self) -> None:
        self._mEditorData.ToFile(constants.EDITOR_DATA_JSON)

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
