import abc
import os
import models
import constants
import nttinject
import ntt_signal

from .FileSystemService import IFileSystemService
from .LogService import ILogService


class IProjectService(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.CreateProjectServiceErrorSignal = ntt_signal.Signal(str)
        self.OpenProjectServiceErrorSignal = ntt_signal.Signal(str)

    @abc.abstractmethod
    def CreateProject(
        self,
        strProjectName: str,
        strProjectPath: str,
        strTemplateName: str,
        bIsProject: str,
    ) -> bool:
        pass

    @abc.abstractmethod
    def OpenProject(self, strProjectFile: str) -> bool:
        pass


@nttinject.dependency_inject(IFileSystemService, models.Project, ILogService)
class ProjectService(IProjectService):
    def __init__(
        self,
        serFileSystemService: IFileSystemService,
        mProject: models.Project,
        serLogService: ILogService,
    ) -> None:
        super().__init__()
        self._serFileSystemService = serFileSystemService
        self._serLogService = serLogService
        self._mProject = mProject

    def CreateProject(
        self,
        strProjectName: str,
        strProjectPath: str,
        strTemplateName: str,
        bIsProject: str,
    ) -> bool:
        strProjectFolder = os.path.join(strProjectPath, strProjectName)
        strTemplateFolder = os.path.join(constants.TEMPLATES_FOLDER, strTemplateName)
        strTemplateJsonFile = os.path.join(
            strTemplateFolder,
            constants.TEMPLATE_JSON_FILE,
        )

        mTemplate = models.Template()
        mTemplate.FromFile(strTemplateJsonFile)

        bResult, strMessage = self._serFileSystemService.CreateFolder(strProjectFolder)

        if bResult:
            for strFolder in mTemplate.Folders:
                bResult, strMessage = self._serFileSystemService.CopyFolderTo(
                    strTemplateFolder,
                    strProjectFolder,
                    strFolder,
                )

                if not bResult:
                    self.CreateProjectServiceErrorSignal.Emit(strMessage)
                    return False

            bResult = self._CreateProjectFile(
                mTemplate=mTemplate,
                strProjectName=strProjectName,
                strProjectFolder=strProjectFolder,
            )

            if not bResult:
                return False

        else:
            self.CreateProjectServiceErrorSignal.Emit(strMessage)
            return False

        self._serLogService.Info(f"Create Project {strProjectName} successfully")
        return True

    def _CreateProjectFile(
        self,
        mTemplate: models.Template,
        strProjectName: str,
        strProjectFolder: str,
    ) -> bool:
        try:
            self._mProject.ProjectName = strProjectName
            self._mProject.Folders.clear()

            for strFolder in mTemplate.Folders:
                self._mProject.Folders.append(strFolder)

            self._mProject.ToFile(
                os.path.join(
                    strProjectFolder,
                    f"{strProjectName}.{constants.PROJECT_EXTENSION}",
                )
            )
            return True
        except Exception as e:
            self.CreateProjectServiceErrorSignal.Emit(str(e))
            return False

    def OpenProject(self, strProjectFile: str) -> bool:
        try:
            self._mProject.FromFile(strProjectFile)
            self._serLogService.Info(f"Open Project File {strProjectFile} sucessfully.")
            return True
        except Exception as e:
            self.OpenProjectServiceErrorSignal.Emit(str(e))
            return False


def Create_ProjectService(*args, **kwargs) -> IProjectService:
    return ProjectService(*args, **kwargs)
