import datetime
import logging
from typing import Optional
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)

        if not log_record.get("timestamp"):
            now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now

        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def get_json_formatter():
    return CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")


def get_logger(name: str = ""):
    logger = logging.getLogger(name)
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(get_json_formatter())
    logger.addHandler(log_handler)
    return logger


class CollectorLogger:
    def __init__(self, name: str, level: Optional[int] = logging.INFO):
        self.logger = get_logger(name)
        self.logger.propagate = False
        logging.basicConfig(level=level)

    def critical(self, msg: str, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
