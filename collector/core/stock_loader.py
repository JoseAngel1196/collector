from collector.utils.stock import iter_stock_classes
from collector.utils import walk_modules

STOCK_MODULE = ['collector.stocks']


class StockLoader():

    def __init__(self):
        self._stocks = {}
        self._load_all_stocks()

    def _load_stocks(self, module):
        for stock_cls in iter_stock_classes(module):
            self._stocks[stock_cls.name] = stock_cls

    def _load_all_stocks(self):
        for name in STOCK_MODULE:
            try:
                for module in walk_modules(name):
                    self._load_stocks(module)
            except ImportError:
                raise

    def load(self, stock_name: str):
        try:
            return self._stocks[stock_name]
        except KeyError:
            raise KeyError(f"Stock not found: {stock_name}")
