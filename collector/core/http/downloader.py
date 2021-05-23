import requests


class Downloader(requests.Session):

    def __init__(self, headers=None):
        super().__init__()

        if headers is not None:
            self.headers = headers

    def generate_and_set_user_agent(self):
        user_agent_string = self.get_user_agent()
        self.set_user_agent(user_agent_string)

    def set_user_agent(self, user_agent_string: str):
        self.headers.update({"User-Agent": user_agent_string})

    def get_user_agent() -> str:
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"

    def request(self, *args, **kwargs):
        response = super().request(*args, **kwargs)
        return response

    # HTTP Methods:

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
