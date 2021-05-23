class Request():
    def __init__(self, url, method='get', headers=None):
        self.method = str(method).lower()
        self.url = url

        if headers is not None:
            self.headers = headers
