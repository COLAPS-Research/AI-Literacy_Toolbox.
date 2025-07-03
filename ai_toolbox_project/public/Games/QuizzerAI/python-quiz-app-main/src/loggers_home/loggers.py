from src.loggers_home.base_logger_impl import BaseLogger, MyLogger


class TimerLogger(BaseLogger):
    """
    Logger for timing-related logs.
    """

    def get_logger(self, name=None):
        logger = MyLogger().get_logger(name)
        logger.info("TimerLogger initialized")
        return logger


class ExceptionLogger(BaseLogger):
    """
    Logger for handling and recording exceptions.
    """

    def get_logger(self, name=None):
        logger = MyLogger().get_logger(name)
        logger.error("ExceptionLogger initialized")
        return logger


class InfoLogger(BaseLogger):
    """
    Logger for recording informational messages.
    """

    def get_logger(self, name=None):
        logger = MyLogger().get_logger(name)
        logger.info("InfoLogger initialized")
        return logger


class DebugLogger(BaseLogger):
    """
    Logger for detailed debugging information.
    """

    def get_logger(self, name=None):
        logger = MyLogger().get_logger(name)
        logger.debug("DebugLogger initialized")
        return logger
