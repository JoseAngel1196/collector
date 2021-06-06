from collector.core.models.photo import Photo
from collector.core.db_connector import DbConnector
from typing import Iterable, List

from collector.core.http.request import Request
from collector.core.http.downloader import Downloader
from collector.core.collector import Collector
from collector.core.stock_loader import StockLoader
from collector.settings import Settings
from collector.utils.project import get_project_settings
from collector.core.settings import DB_NAME, HOST, PASSWORD, PORT, USER


class CollectorRunner:

    stock_loader = StockLoader()

    def __init__(self, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.settings = settings
        self.downloader = Downloader()
        self.db = DbConnector(
            dbname=DB_NAME, user=USER, pswd=PASSWORD, host=HOST, port=PORT
        )

    def run(self):
        try:
            self.collectorcls = self.stock_loader.load(self.settings.stock_name)
            self.collector = self._create_collector(self.collectorcls)
            start_requests = self.collector.start_requests()
            self._open_collector(start_requests)
        except Exception as e:
            raise e

    def _create_collector(self, collectorcls) -> Collector:
        return collectorcls.from_runner()

    def _open_collector(self, start_requests: List[Iterable]):
        for start_request in start_requests:
            request_proceeded = self._process_request(start_request)
            parsed_request = self.collector.parse(request_proceeded)

    def _process_request(self, request: Request):
        method = getattr(self.downloader, request.method)
        return method(url=request.url)

    def _save_request(self, photos: List[Photo]):
        pass


def execute():
    settings = get_project_settings()
    collector_runner = CollectorRunner(settings)
    collector_runner.run()


execute()
