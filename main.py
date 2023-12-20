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

    injector.AddSingleton(Template, lambda: Template())
    injector.AddSingleton(IFileSystemService, lambda: Create_FileSystemService())
    injector.AddSingleton(ITemplateService, lambda: Create_TemplateService())

    injector.AddSingleton(StartupWidgetViewModel, lambda: StartupWidgetViewModel())
    injector.AddTransient(
        NewProjectDialogViewModel, lambda: NewProjectDialogViewModel()
    )

    app = QApplication(sys.argv)

    window = StartupWindowView()
    window.showMaximized()

    sys.exit(app.exec_())
