from nttinject import *
from models import *
from services import *
from typing import *
from constants import *
from nttinject import *
from ntt_signal import *


@dependency_inject(Project)
class GameEditorWindowViewModel:
    def __init__(self, mProject: Project) -> None:
        self._mProject = mProject

        self.EditorWindowTitleChangedSignal = Signal()
        self._mProject.Attach(self.EditorWindowTitleChangedSignal)

    @property
    def WindowTitle(self) -> str:
        return f"{EDITOR_WINDOW_TITLE} - {self._mProject.ProjectName}"
