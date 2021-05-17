import os
import sys
from importlib import import_module

STOCK_MODULE = 'collector.stocks'


def import_file():
    module = import_module(STOCK_MODULE)
    return module
