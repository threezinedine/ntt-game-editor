from abc import *
import os
from models import *
from constants import *
from nttinject import *
from ntt_signal import *
from .FileSystemService import IFileSystemService


class IProjectService(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.ServiceErrorSignal = Signal(str)

    @abstractmethod
    def CreateProject(
        self,
        strProjectName: str,
        strProjectPath: str,
        strTemplateName: str,
        bIsProject: str,
    ) -> bool:
        pass


@dependency_inject(IFileSystemService, Project)
class ProjectService(IProjectService):
    def __init__(
        self, serFileSystemService: IFileSystemService, mProject: Project
    ) -> None:
        super().__init__()
        self._serFileSystemService = serFileSystemService
        self._mProject = mProject

    def CreateProject(
        self,
        strProjectName: str,
        strProjectPath: str,
        strTemplateName: str,
        bIsProject: str,
    ) -> bool:
        strProjectFolder = os.path.join(strProjectPath, strProjectName)
        strTemplateFolder = os.path.join(TEMPLATES_FOLDER, strTemplateName)
        strTemplateJsonFile = os.path.join(strTemplateFolder, TEMPLATE_JSON_FILE)

        mTemplate = Template()
        mTemplate.FromFile(strTemplateJsonFile)

        bResult, strMessage = self._serFileSystemService.CreateFolder(strProjectFolder)

        if bResult:
            for strFolder in mTemplate.Folders:
                bResult, strMessage = self._serFileSystemService.CopyFolderTo(
                    strTemplateFolder, strProjectFolder, strFolder
                )

                if not bResult:
                    self.ServiceErrorSignal.Emit(strMessage)
                    return False

            bResult = self._CreateProjectFile(
                mTemplate=mTemplate,
                strProjectName=strProjectName,
                strProjectFolder=strProjectFolder,
            )

            if not bResult:
                return False

        else:
            self.ServiceErrorSignal.Emit(strMessage)
            return False

        return True

    def _CreateProjectFile(
        self, mTemplate: Template, strProjectName: str, strProjectFolder: str
    ) -> bool:
        try:
            self._mProject.ProjectName = strProjectName
            self._mProject.Folders.clear()

            for strFolder in mTemplate.Folders:
                self._mProject.Folders.append(strFolder)

            self._mProject.ToFile(
                os.path.join(strProjectFolder, f"{strProjectName}.{PROJECT_EXTENSION}")
            )
            return True
        except Exception as e:
            self.ServiceErrorSignal.Emit(str(e))
            return False


def Create_ProjectService(*args, **kwargs) -> IProjectService:
    return ProjectService(*args, **kwargs)
