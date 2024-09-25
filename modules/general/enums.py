from enum import Enum


class DataType(str, Enum):
    STOCK_PRICE = 'stock_price'


class CollectResult(str, Enum):
    SUCCESS = 'success'
    FAIL = 'fail'
