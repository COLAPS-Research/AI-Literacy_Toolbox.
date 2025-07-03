import logging
from abc import ABC, abstractmethod


class BaseLogger(ABC):
    """
    Abstract base class for custom loggers.
    Provides a structure for defining loggers with specific configurations.
    """

    @abstractmethod
    def get_logger(self, name=None):
        """
        Retrieve a logger instance.

        Args:
            name (str): The name of the logger (optional).

        Returns:
            logging.Logger: Configured logger instance.
        """
        pass


class MyLogger(BaseLogger):
    """
    Default logger with custom formatting and configuration.
    """

    def __init__(self, level=logging.DEBUG):
        self.level = level
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    def get_logger(self, name=None):
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(self.formatter)
            logger.addHandler(handler)
        logger.setLevel(self.level)
        return logger
