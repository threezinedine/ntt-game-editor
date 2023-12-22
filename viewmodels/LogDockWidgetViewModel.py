import typing
import nttinject
import services
import ntt_signal


@nttinject.dependency_inject(services.ILogService)
class LogDockWidgetViewModel:
    def __init__(self, serLogService: services.ILogService) -> None:
        self._serLogService = serLogService

        self.NewLogMessgeSignal = ntt_signal.Signal()
        self._serLogService.Messages.Attach(self.NewLogMessgeSignal)

    @property
    def MessagesInfo(self) -> typing.List[typing.Tuple[str, str, int, str, str]]:
        return [
            (
                message.Level,
                message.File,
                message.Line,
                message.TimeString,
                message.Message,
            )
            for message in self._serLogService.Messages
        ]

    def ClearLog(self) -> None:
        self._serLogService.ClearLog()
