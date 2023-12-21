from typing import *
from PyQt5.QtWidgets import *
from models import *
from services import *
from constants import *
from nttinject import *
from ntt_signal import *


@dependency_inject(ITemplateService, IProjectService, IEditorService)
class StartupWidgetViewModel:
    def __init__(
        self,
        serTemplateService: ITemplateService,
        serProjectService: IProjectService,
        serEditorService: IEditorService,
    ) -> None:
        self._serTemplateService = serTemplateService
        self._serProjectService = serProjectService
        self._serEditorService = serEditorService

        self._mTemplates: List[Template] = serTemplateService.LoadAllTemplates()
        self.OpenProjectErrorSignal = Signal(str)
        self._serProjectService.OpenProjectServiceErrorSignal.Attach(
            self.OpenProjectErrorSignal
        )

    @property
    def TemplateNames(self) -> List[str]:
        return [mTemplate.TemplateName for mTemplate in self._mTemplates]

    @property
    def TemplatesInfo(self) -> List[Tuple[str]]:
        return [(mTemplate.TemplateName) for mTemplate in self._mTemplates]

    @property
    def RecentProjects(self) -> List[str]:
        return self._serEditorService.RecentProjects

    def OpenProject(self, strProjectFile: str) -> bool:
        bResult = self._serProjectService.OpenProject(strProjectFile=strProjectFile)

        if bResult:
            self._serEditorService.AppendNewRecentProject(strProjectFile)

        return bResult

    def ClearRecentProjects(self) -> None:
        self._serEditorService.ClearRecentProjects()
