

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
        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")
        else:
            for url in self.start_urls:
                pass

    def parse(self, response, **kwargs):
        raise NotImplementedError()
