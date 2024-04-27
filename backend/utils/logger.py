import functools
import inspect
import time
from enum import Enum

from loguru import logger


class LogLevel(Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def detailed_logging_factory(
    level: LogLevel = LogLevel.INFO,
    log_execution_time: bool = False,
):
    def internal_logger(func):
        name = func.__name__

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            logger_ = logger.opt(depth=1)
            logger_.log(
                level.value, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
            )

            # task = func(*args, **kwargs)
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error("Exception '{}' occurred in '{}'", e, name)
                raise e

            end_time = time.time()

            if log_execution_time:
                logger_.log(
                    level.value,
                    "Function '{}' executed in {} s",
                    name,
                    end_time - start_time,
                )
            logger_.log(level.value, "Exiting '{}' (result={})", name, result)
            return result

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            logger_ = logger.opt(depth=1)

            logger_.log(
                level.value, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
            )

            # task = func(*args, **kwargs)
            try:
                result = await func(*args, **kwargs)
            except Exception as e:
                logger.error("Exception '{}' occurred in '{}'", e, name)
                raise e

            end_time = time.time()

            if log_execution_time:
                logger_.log(
                    level.value,
                    "Function '{}' executed in {} s",
                    name,
                    end_time - start_time,
                )

            logger_.log(level.value, "Exiting '{}' (result={})", name, result)
            return result

        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return internal_logger


def logging_factory(
    level: LogLevel = LogLevel.INFO,
    log_execution_time: bool = False,
):
    def internal_logger(func):
        name = func.__name__

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            logger_ = logger.opt(depth=1)
            logger_.log(
                level.value, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
            )

            # task = func(*args, **kwargs)
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error("Exception '{}' occurred in '{}'", e, name)
                raise e

            end_time = time.time()

            if log_execution_time:
                logger_.log(
                    level.value,
                    "Function '{}' executed in {} s",
                    name,
                    end_time - start_time,
                )
            logger_.log(level.value, "Exiting '{}'", name)
            return result

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            logger_ = logger.opt(depth=1)

            logger_.log(
                level.value, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
            )

            # task = func(*args, **kwargs)
            try:
                result = await func(*args, **kwargs)
            except Exception as e:
                logger.error("Exception '{}' occurred in '{}'", e, name)
                raise e

            end_time = time.time()

            if log_execution_time:
                logger_.log(
                    level.value,
                    "Function '{}' executed in {} s",
                    name,
                    end_time - start_time,
                )

            logger_.log(level.value, "Exiting '{}'", name)

            return result

        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return internal_logger
