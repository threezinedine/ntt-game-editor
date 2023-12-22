import os
import services
import nttinject
import constants
import ntt_signal


@nttinject.dependency_inject(
    services.IProjectService, services.IFileSystemService, services.IEditorService
)
class NewProjectDialogViewModel:
    def __init__(
        self,
        serProjectService: services.IProjectService,
        serFileSystemService: services.IFileSystemService,
        serEditorService: services.IEditorService,
    ) -> None:
        self._serProjectService = serProjectService
        self._serFileSystemService = serFileSystemService
        self._serEditorService = serEditorService

        self._strProjectName: str = ""
        self._strProjectPath: str = ""
        self._strTemplateName: str = ""
        self._bIsProject: bool = True

        self.ProjectNameSignal = ntt_signal.Signal(str)
        self.ProjectPathSignal = ntt_signal.Signal(str)
        self.TemplateNameSignal = ntt_signal.Signal(str)
        self.ProjectFullPathSignal = ntt_signal.Signal(str)
        self.IsValidSignal = ntt_signal.Signal()
        self.CreateProjectErrorSignal = ntt_signal.Signal(str)

        self.ProjectNameSignal.Attach(self.ProjectFullPathSignal)
        self.ProjectPathSignal.Attach(self.ProjectFullPathSignal)
        self.ProjectNameSignal.Attach(self.IsValidSignal)
        self.ProjectPathSignal.Attach(self.IsValidSignal)
        self._serProjectService.CreateProjectServiceErrorSignal.Attach(
            self.CreateProjectErrorSignal
        )

    @property
    def ProjectName(self) -> str:
        return self._strProjectName

    @ProjectName.setter
    def ProjectName(self, strProjectName: str) -> None:
        if self._strProjectName != strProjectName:
            self._strProjectName = strProjectName
            self.ProjectNameSignal.Emit(self._strProjectName)

    @property
    def ProjectPath(self) -> str:
        return self._strProjectPath

    @ProjectPath.setter
    def ProjectPath(self, strProjectPath: str) -> None:
        if self._strProjectPath != strProjectPath:
            self._strProjectPath = strProjectPath
            self.ProjectPathSignal.Emit(strProjectPath)

    @property
    def ProjectFullPath(self) -> str:
        return os.path.join(
            self._strProjectPath,
            self._strProjectName,
            f"{self._strProjectName}.{constants.PROJECT_EXTENSION}",
        )

    @property
    def TemplateName(self) -> str:
        return self._strTemplateName

    @TemplateName.setter
    def TemplateName(self, strTemplateName: str) -> None:
        if self._strTemplateName != strTemplateName:
            self._strTemplateName = strTemplateName
            self.TemplateNameSignal.Emit(strTemplateName)

    @property
    def IsProject(self) -> bool:
        return self._bIsProject

    @IsProject.setter
    def IsProject(self, bIsProject: bool) -> None:
        self._bIsProject = bIsProject

    @property
    def IsValid(self) -> bool:
        return (
            self._strProjectName != ""
            and self._strProjectName.find(" ") == -1
            and self._strProjectName[0].isupper()
            and not self._serFileSystemService.CheckFolderExist(
                os.path.join(
                    self._strProjectPath,
                    self._strProjectName,
                )
            )
        )

    def CreateNewProject(self) -> bool:
        bResult = self._serProjectService.CreateProject(
            self._strProjectName,
            self._strProjectPath,
            self._strTemplateName,
            self._bIsProject,
        )

        if bResult:
            self._serEditorService.AppendNewRecentProject(
                os.path.join(
                    self._strProjectPath,
                    self._strProjectName,
                    f"{self._strProjectName}.{constants.PROJECT_EXTENSION}",
                )
            )

        return bResult
