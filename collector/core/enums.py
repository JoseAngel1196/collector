from enum import Enum


class StockType(Enum):
    UNSPLASH = 'unsplash'

    @classmethod
    def get(cls, name):
        try:
            return cls(name)
        except ValueError:
            raise Exception('StockType not supported')
