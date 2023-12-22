import sys
import PyQt5
import views
import viewmodels
import nttinject
import models
import services


if __name__ == "__main__":
    try:
        injector = nttinject.Injector()

        # Models registration
        injector.AddSingleton(
            models.Project,
            lambda: models.Project(),
        )
        injector.AddSingleton(
            models.EditorData,
            lambda: models.EditorData(),
        )

        # Services registration
        injector.AddSingleton(
            services.ILogService,
            lambda: services.Create_LogService(),
        )
        injector.AddSingleton(
            services.IFileSystemService,
            lambda: services.Create_FileSystemService(),
        )
        injector.AddSingleton(
            services.ITemplateService,
            lambda: services.Create_TemplateService(),
        )
        injector.AddSingleton(
            services.IProjectService,
            lambda: services.Create_ProjectService(),
        )
        injector.AddSingleton(
            services.IEditorService,
            lambda: services.Create_EditorService(),
        )

        # ViewModels registration
        injector.AddTransient(
            viewmodels.NewProjectDialogViewModel,
            lambda: viewmodels.NewProjectDialogViewModel(),
        )
        injector.AddSingleton(
            viewmodels.GameEditorCentralWidgetViewModel,
            lambda: viewmodels.GameEditorCentralWidgetViewModel(),
        )
        injector.AddSingleton(
            viewmodels.StartupWidgetViewModel,
            lambda: viewmodels.StartupWidgetViewModel(),
        )
        injector.AddSingleton(
            viewmodels.GameEditorWindowViewModel,
            lambda: viewmodels.GameEditorWindowViewModel(),
        )
        injector.AddSingleton(
            viewmodels.LogDockWidgetViewModel,
            lambda: viewmodels.LogDockWidgetViewModel(),
        )

        app = PyQt5.QtWidgets.QApplication(sys.argv)

        window = views.StartupWindowView(views.GameEditorWindowView())
        window.showMaximized()

        sys.exit(app.exec_())

    # except:
    except Exception as e:
        print(e)
        # input()
        # pass
