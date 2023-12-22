import shutil
import typing
import abc
import os
import constants


class IFileSystemService(abc.ABC):
    @abc.abstractmethod
    def GetAllTemplateJsonFilesFullPaths(self) -> typing.List[str]:
        pass

    @abc.abstractmethod
    def CreateFolder(
        self, strFolderPath: str
    ) -> typing.Tuple[bool, typing.Union[str, None]]:
        pass

    @abc.abstractmethod
    def CopyFolderTo(
        self, strSourceBaseFolder: str, strDesBaseFolder: str, strFolder: str
    ) -> typing.Tuple[bool, typing.Union[str, None]]:
        pass

    @abc.abstractmethod
    def CheckFolderExist(self, strFolderName: str) -> bool:
        pass

    @abc.abstractmethod
    def CheckFileExist(self, strFileName: str) -> bool:
        pass


class FileSystemService(IFileSystemService):
    def __init__(self) -> None:
        pass

    def GetAllTemplateJsonFilesFullPaths(self) -> typing.List[str]:
        strTemplateJsonFilesFullPaths: typing.List[str] = []
        strTemplateFolders: typing.List[str] = os.listdir(constants.TEMPLATES_FOLDER)

        for strTemplateFolder in strTemplateFolders:
            if self._CheckTemplateFolderValid(strTemplateFolder):
                strTemplateJsonFilesFullPaths.append(
                    os.path.join(
                        constants.TEMPLATES_FOLDER,
                        strTemplateFolder,
                        constants.TEMPLATE_JSON_FILE,
                    )
                )

        return strTemplateJsonFilesFullPaths

    def _CheckTemplateFolderValid(self, strTemplateFolder: str) -> bool:
        return (
            True
            if os.path.exists(
                os.path.join(
                    constants.TEMPLATES_FOLDER,
                    strTemplateFolder,
                    constants.TEMPLATE_JSON_FILE,
                )
            )
            else False
        )

    def CreateFolder(
        self, strFolderPath: str
    ) -> typing.Tuple[bool, typing.Union[str, None]]:
        try:
            os.makedirs(strFolderPath)
            return True, None
        except Exception as e:
            return False, str(e)

    def CopyFolderTo(
        self, strSourceBaseFolder: str, strDesBaseFolder: str, strFolder: str
    ) -> typing.Tuple[bool, typing.Union[str, None]]:
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
