import sys
from PyQt5.QtWidgets import QApplication
from views import *
from constants import *
from nttinject import *
from models import *
from viewmodels import *
from services import *


if __name__ == "__main__":
    try:
        injector = Injector()

        # Models registration
        injector.AddSingleton(Project, lambda: Project())
        injector.AddSingleton(EditorData, lambda: EditorData())

        # Services registration
        injector.AddSingleton(IFileSystemService, lambda: Create_FileSystemService())
        injector.AddSingleton(ITemplateService, lambda: Create_TemplateService())
        injector.AddSingleton(IProjectService, lambda: Create_ProjectService())
        injector.AddSingleton(IEditorService, lambda: Create_EditorService())

        # ViewModels registration
        injector.AddTransient(
            NewProjectDialogViewModel, lambda: NewProjectDialogViewModel()
        )
        injector.AddSingleton(
            GameEditorCentralWidgetViewModel, lambda: GameEditorCentralWidgetViewModel()
        )
        injector.AddSingleton(StartupWidgetViewModel, lambda: StartupWidgetViewModel())
        injector.AddSingleton(
            GameEditorWindowViewModel, lambda: GameEditorWindowViewModel()
        )
        injector.AddSingleton(LogDockWidgetViewModel, lambda: LogDockWidgetViewModel())

        app = QApplication(sys.argv)

        window = StartupWindowView(GameEditorWindowView())
        window.showMaximized()

        sys.exit(app.exec_())

    except:
        # except Exception as e:
        # print(e)
        # input()
        pass
