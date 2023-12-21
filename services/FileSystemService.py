import shutil
from typing import *
from abc import *
import os
from typing import List, Tuple, Union
from constants import *


class IFileSystemService(ABC):
    @abstractmethod
    def GetAllTemplateJsonFilesFullPaths(self) -> List[str]:
        pass

    @abstractmethod
    def CreateFolder(self, strFolderPath: str) -> Tuple[bool, Union[str, None]]:
        pass

    @abstractmethod
    def CopyFolderTo(
        self, strSourceBaseFolder: str, strDesBaseFolder: str, strFolder: str
    ) -> Tuple[bool, Union[str, None]]:
        pass

    @abstractmethod
    def CheckFolderExist(self, strFolderName: str) -> bool:
        pass

    @abstractmethod
    def CheckFileExist(self, strFileName: str) -> bool:
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

    def CreateFolder(self, strFolderPath: str) -> Tuple[bool, Union[str, None]]:
        try:
            os.makedirs(strFolderPath)
            return True, None
        except Exception as e:
            return False, str(e)

    def CopyFolderTo(
        self, strSourceBaseFolder: str, strDesBaseFolder: str, strFolder: str
    ) -> Tuple[bool, Union[str, None]]:
        try:
            shutil.copytree(
                os.path.join(strSourceBaseFolder, strFolder),
                os.path.join(strDesBaseFolder, strFolder),
            )
            return True, None
        except Exception as e:
            return False, str(e)

    def CheckFolderExist(self, strFolderName: str) -> bool:
        return os.path.exists(strFolderName)

    def CheckFileExist(self, strFileName: str) -> bool:
        return os.path.exists(strFileName)


def Create_FileSystemService(*args, **kwargs) -> IFileSystemService:
    return FileSystemService(*args, **kwargs)
