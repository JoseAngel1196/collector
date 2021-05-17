import inspect
from collector.core.collector import Collector


def iter_stock_classes(module):
    for obj in vars(module).values():
        if (
            inspect.isclass(obj)
            and issubclass(obj, Collector)
            and obj.__module__ == module.__name__
            and getattr(obj, 'name', None)
        ):
            yield obj
