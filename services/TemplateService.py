import typing
import abc
import models
import nttinject

from .FileSystemService import IFileSystemService


class ITemplateService(abc.ABC):
    @abc.abstractmethod
    def LoadAllTemplates(self) -> typing.List[models.Template]:
        pass


@nttinject.dependency_inject(IFileSystemService)
class TemplateService(ITemplateService):
    def __init__(self, serFileSystemService: IFileSystemService) -> None:
        self._serFileSystemService = serFileSystemService

    def LoadAllTemplates(self) -> typing.List[models.Template]:
        mTemplates: typing.List[models.Template] = []

        strTemplateJsonFiles: typing.List[
            str
        ] = self._serFileSystemService.GetAllTemplateJsonFilesFullPaths()

        for strTemplateJsonFile in strTemplateJsonFiles:
            mTemplate = models.Template()
            mTemplate.FromFile(strTemplateJsonFile)
            mTemplates.append(mTemplate)

        return mTemplates


def Create_TemplateService(*args, **kwargs) -> ITemplateService:
    return TemplateService(*args, **kwargs)
