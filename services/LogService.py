import abc
import typing
import ntt_observable_list
import constants
import logging
import datetime


class LogMessage:
    def __init__(
        self,
        eLevel: int = logging.DEBUG,
        strLevel: str = "DEBUG",
        time: datetime.datetime = datetime.datetime.now(),
        strFile: str = "",
        nLine: int = 1,
        strMessage: str = "",
    ) -> None:
        self._eLevel = eLevel
        self._strLevel = strLevel
        self._strFile = strFile
        self._time = time
        self._nLine = nLine
        self._strMessage = strMessage

    @property
    def Levelo(self) -> int:
        return self._eLevel

    @property
    def Level(self) -> str:
        return self._strLevel

    @property
    def File(self) -> str:
        return self._strFile

    @property
    def Time(self) -> datetime.datetime:
        return self._time

    @property
    def Line(self) -> int:
        return self._nLine

    @property
    def Message(self) -> str:
        return self._strMessage

    def __repr__(self) -> str:
        return (
            "<Message "
            f'level="{self.Level}"'
            f'file="{self.File}"/>'
            f'line="{self.Line}"'
            f'time="{datetime.datetime.fromtimestamp(self.Time)}"'
            f'message="{self.Message}"'
            " />"
        )


class ILogService(abc.ABC):
    @abc.abstractmethod
    def AddMessage(self, oLogMessage: LogMessage) -> None:
        pass

    @abc.abstractmethod
    def Debug(self, strMessage: str) -> None:
        pass

    @abc.abstractmethod
    def Info(self, strMessage: str) -> None:
        pass

    @abc.abstractmethod
    def Warn(self, strMessage: str) -> None:
        pass

    @abc.abstractmethod
    def Error(self, strMessage: str) -> None:
        pass


class EngineLoggingHandler(logging.Handler):
    def __init__(self, serLogService: ILogService, level: int = 0) -> None:
        super().__init__(level)
        self._serLogService = serLogService

    def emit(self, record: logging.LogRecord) -> None:
        oLogMessage = LogMessage(
            eLevel=record.levelno,
            strLevel=record.levelname,
            time=record.created,
            strFile=record.filename,
            nLine=record.lineno,
            strMessage=record.getMessage(),
        )

        print(oLogMessage)


class LogService(ILogService):
    def __init__(self) -> None:
        super().__init__()

        self._oLogMessages: typing.List[
            LogMessage
        ] = ntt_observable_list.ObservableList([])

        self._oLogger = logging.getLogger(constants.LOGGER_NAME)
        self._oLogger.addHandler(EngineLoggingHandler(self))

    def AddMessage(self, oLogMessage: LogMessage) -> None:
        self._oLogMessages.append(oLogMessage)

    def Info(self, strMessage: str) -> None:
        self._oLogger.info(strMessage)

    def Debug(self, strMessage: str) -> None:
        self._oLogger.debug(strMessage)

    def Warn(self, strMessage: str) -> None:
        self._oLogger.warn(strMessage)

    def Error(self, strMessage: str) -> None:
        self._oLogger.error(strMessage)


def Create_LogService(*args, **kwargs) -> ILogService:
    return LogService(*args, **kwargs)
