import sys
from PyQt5.QtWidgets import QApplication
from views import *
from constants import *
from nttinject import *
from models import *
from viewmodels import *
from services import *


if __name__ == "__main__":
    injector = Injector()

    # Models registration
    injector.AddSingleton(Project, lambda: Project())

    # Services registration
    injector.AddSingleton(IFileSystemService, lambda: Create_FileSystemService())
    injector.AddSingleton(ITemplateService, lambda: Create_TemplateService())
    injector.AddSingleton(IProjectService, lambda: Create_ProjectService())

    # ViewModels registration
    injector.AddSingleton(StartupWidgetViewModel, lambda: StartupWidgetViewModel())
    injector.AddTransient(
        NewProjectDialogViewModel, lambda: NewProjectDialogViewModel()
    )
    injector.AddSingleton(
        GameEditorCentralWidgetViewModel, lambda: GameEditorCentralWidgetViewModel()
    )
    injector.AddSingleton(LogDockWidgetViewModel, lambda: LogDockWidgetViewModel())

    app = QApplication(sys.argv)

    window = StartupWindowView(GameEditorWindowView())
    window.showMaximized()

    sys.exit(app.exec_())
