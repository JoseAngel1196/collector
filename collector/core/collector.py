from collector.core.models.photo import Photo
from typing import List


class Collector():
    name: str

    def __init__(self, name=None):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError(f'{type(self).__name__} must have a name')

        if not hasattr(self, 'start_urls'):
            self.start_urls = []

    @classmethod
    def from_runner(cls):
        return cls()

    def start_requests(self):
        raise NotImplementedError()

    def parse(self, response) -> List[Photo]:
        raise NotImplementedError()

    def process_results(self):
        raise NotImplementedError()
