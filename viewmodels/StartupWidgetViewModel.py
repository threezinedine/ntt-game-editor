import typing
import models
import services
import nttinject
import ntt_signal


@nttinject.dependency_inject(
    services.ITemplateService,
    services.IProjectService,
    services.IEditorService,
)
class StartupWidgetViewModel:
    def __init__(
        self,
        serTemplateService: services.ITemplateService,
        serProjectService: services.IProjectService,
        serEditorService: services.IEditorService,
    ) -> None:
        self._serTemplateService = serTemplateService
        self._serProjectService = serProjectService
        self._serEditorService = serEditorService

        self._mTemplates: typing.List[
            models.Template
        ] = serTemplateService.LoadAllTemplates()
        self.OpenProjectErrorSignal = ntt_signal.Signal(str)
        self._serProjectService.OpenProjectServiceErrorSignal.Attach(
            self.OpenProjectErrorSignal
        )

    @property
    def TemplateNames(self) -> typing.List[str]:
        return [mTemplate.TemplateName for mTemplate in self._mTemplates]

    @property
    def TemplatesInfo(self) -> typing.List[typing.Tuple[str]]:
        return [(mTemplate.TemplateName) for mTemplate in self._mTemplates]

    @property
    def RecentProjects(self) -> typing.List[str]:
        return self._serEditorService.RecentProjects

    def OpenProject(self, strProjectFile: str) -> bool:
        bResult = self._serProjectService.OpenProject(strProjectFile=strProjectFile)

        if bResult:
            self._serEditorService.AppendNewRecentProject(strProjectFile)

        return bResult

    def ClearRecentProjects(self) -> None:
        self._serEditorService.ClearRecentProjects()
