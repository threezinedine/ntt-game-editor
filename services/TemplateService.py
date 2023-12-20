from typing import *
from abc import *
from typing import List
from models import *
from nttinject import *

from .FileSystemService import IFileSystemService


class ITemplateService(ABC):
    @abstractmethod
    def LoadAllTemplates(self) -> List[Template]:
        pass


@dependency_inject(IFileSystemService)
class TemplateService(ITemplateService):
    def __init__(self, serFileSystemService: IFileSystemService) -> None:
        self._serFileSystemService = serFileSystemService

    def LoadAllTemplates(self) -> List[Template]:
        mTemplates: List[Template] = []

        strTemplateJsonFiles: List[
            str
        ] = self._serFileSystemService.GetAllTemplateJsonFilesFullPaths()

        for strTemplateJsonFile in strTemplateJsonFiles:
            mTemplate = Template()
            mTemplate.FromFile(strTemplateJsonFile)
            mTemplates.append(mTemplate)

        return mTemplates


def Create_TemplateService(*args, **kwargs) -> ITemplateService:
    return TemplateService(*args, **kwargs)
