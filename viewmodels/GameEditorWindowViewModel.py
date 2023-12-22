import nttinject
import models
import constants
import ntt_signal


@nttinject.dependency_inject(models.Project)
class GameEditorWindowViewModel:
    def __init__(
        self,
        mProject: models.Project,
    ) -> None:
        self._mProject = mProject

        self.EditorWindowTitleChangedSignal = ntt_signal.Signal()
        self._mProject.Attach(self.EditorWindowTitleChangedSignal)

    @property
    def WindowTitle(self) -> str:
        return f"{constants.EDITOR_WINDOW_TITLE} - {self._mProject.ProjectName}"
