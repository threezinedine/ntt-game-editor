from typing import *
from PyQt5.QtWidgets import *
from models import *
from services import *
from constants import *
from nttinject import *
from ntt_signal import *


@dependency_inject(ITemplateService)
class StartupWidgetViewModel:
    def __init__(self, serTemplateService: ITemplateService) -> None:
        self._serTemplateService = ITemplateService

        self._mTemplates: List[Template] = serTemplateService.LoadAllTemplates()

    @property
    def TemplateNames(self) -> List[str]:
        return [mTemplate.TemplateName for mTemplate in self._mTemplates]

    @property
    def TemplatesInfo(self) -> List[Tuple[str]]:
        return [(mTemplate.TemplateName) for mTemplate in self._mTemplates]

    def CreateNewProjectDialog(self, strTemplateName: str) -> None:
        pass
