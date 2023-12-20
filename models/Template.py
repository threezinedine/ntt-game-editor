from ntt_json_model import *


class Template(ModelBase):
    def __init__(self) -> None:
        super().__init__()

        StrProperty(self, "", "_strTemplateName")

    @property
    def TemplateName(self) -> str:
        return self._strTemplateName.GetValue()

    def __repr__(self) -> str:
        return f'<Template id={id(self)} name="{self._strTemplateName}"/>'


ModelBase.mSubModels[Template.__name__] = Template
