import ntt_json_model
import typing


class Template(ntt_json_model.ModelBase):
    def __init__(self) -> None:
        super().__init__()

        ntt_json_model.StrProperty(self, "", "_strTemplateName")
        ntt_json_model.ListProperty(self, [], "_strFolders")

    @property
    def TemplateName(self) -> str:
        return self._strTemplateName.GetValue()

    @property
    def Folders(self) -> typing.List[str]:
        return self._strFolders.GetValue()

    def __repr__(self) -> str:
        return f'<Template id={id(self)} name="{self._strTemplateName}"/>'


ntt_json_model.ModelBase.mSubModels[Template.__name__] = Template
