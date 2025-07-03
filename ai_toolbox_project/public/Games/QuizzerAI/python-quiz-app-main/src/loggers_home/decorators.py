import functools
import time
from src.loggers_home.base_logger_impl import MyLogger


# Initialize the default logger
logger = MyLogger().get_logger()


def exception_logger(func):
    """
    A decorator that logs exceptions raised in the wrapped function.

    Logs exception details and re-raises the exception.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The wrapped function with exception logging.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(
                f"Exception raised in {func.__name__}. Exception: {str(e)}"
            )
            raise e

    return wrapper


def debug_logger(func):
    """
    A decorator that logs debug-level messages for function calls and their results.

    Logs the arguments passed and the result returned.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The wrapped function with debug logging.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"Result of {func.__name__}: {result}")
        return result

    return wrapper


def info_logger(func):
    """
    A decorator that logs info-level messages for function calls and their results.

    Logs the arguments passed and the result returned.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The wrapped function with info logging.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Result of {func.__name__}: {result}")
        return result

    return wrapper


def timer_logger(func):
    """
    A decorator that logs the execution time of the wrapped function.

    Logs the time taken to execute the function.

    Args:
        func (Callable): The function to wrap.

    Returns:
        Callable: The wrapped function with execution time logging.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Time taken for {func.__name__}: {end_time -start_time} seconds")
        return result

    return wrapper
