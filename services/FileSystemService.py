from typing import *
from abc import *
import os
from typing import List
from constants import *


class IFileSystemService(ABC):
    @abstractmethod
    def GetAllTemplateJsonFilesFullPaths(self) -> List[str]:
        pass


class FileSystemService(IFileSystemService):
    def __init__(self) -> None:
        pass

    def GetAllTemplateJsonFilesFullPaths(self) -> List[str]:
        strTemplateJsonFilesFullPaths: List[str] = []
        strTemplateFolders: List[str] = os.listdir(TEMPLATES_FOLDER)

        for strTemplateFolder in strTemplateFolders:
            if self._CheckTemplateFolderValid(strTemplateFolder):
                strTemplateJsonFilesFullPaths.append(
                    os.path.join(
                        TEMPLATES_FOLDER,
                        strTemplateFolder,
                        TEMPLATE_JSON_FILE,
                    )
                )

        return strTemplateJsonFilesFullPaths

    def _CheckTemplateFolderValid(self, strTemplateFolder: str) -> bool:
        return (
            True
            if os.path.exists(
                os.path.join(TEMPLATES_FOLDER, strTemplateFolder, TEMPLATE_JSON_FILE)
            )
            else False
        )


def Create_FileSystemService(*args, **kwargs) -> IFileSystemService:
    return FileSystemService(*args, **kwargs)
