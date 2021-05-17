from collector.core.collector import Collector
from collector.core.stock_loader import StockLoader
from collector.settings import Settings
from collector.utils.project import get_project_settings


class CollectorRunner():

    stock_loader = StockLoader()

    def __init__(self, settings=None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        self.settings = settings

    def run(self):
        try:
            self.collectorcls = self.stock_loader.load(
                self.settings.stock_name)
            self.collector = self._create_collector(self.collectorcls)
            start_requests = self.collector.start_requests()
        except Exception as e:
            raise

    def _create_collector(self, collectorcls) -> Collector:
        return collectorcls.from_runner()


def execute():
    settings = get_project_settings()
    collector_runner = CollectorRunner(settings)
    collector_runner.run()


execute()
