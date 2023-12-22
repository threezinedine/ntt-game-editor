import os
import constants


class CssLoader:
    def __init__(self, strCssFile) -> None:
        with open(os.path.join(constants.CSS_FOLDER, strCssFile), "r") as file:
            self._strContent = file.read()

    @property
    def Content(self) -> str:
        return self._strContent
