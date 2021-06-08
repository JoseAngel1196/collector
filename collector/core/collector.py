from typing import Iterable

from collector.logger import CollectorLogger
from collector.core.models.photo import Photo


class Collector:
    name: str

    logger: CollectorLogger

    def __init__(self, logger: CollectorLogger, name: str = None):
        self.logger = logger

        if name is not None:
            self.name = name
        elif not getattr(self, "name", None):
            raise ValueError(f"{type(self).__name__} must have a name")

    @classmethod
    def from_runner(cls, logger: CollectorLogger):
        return cls(logger=logger)

    def start_requests(self):
        raise NotImplementedError()

    def parse(self, response) -> Iterable[Photo]:
        raise NotImplementedError()

    def process_results(self):
        raise NotImplementedError()
