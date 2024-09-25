from loguru import logger

from modules.general.value_objects import CollectRecord
from modules.stock.value_objects import StockPrice


def insert_collect_record(conn, record: CollectRecord):
    sql = '''INSERT INTO collect_record(date, data_type, result, reason)
             VALUES(?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (record.date, record.data_type, record.result, record.reason))
    conn.commit()
    logger.info(f"{record} inserted into 'collect_record'.")


def insert_price(conn, price: StockPrice):
    """Insert a new record into the price table"""
    sql = '''INSERT INTO price(date, symbol, open, high, low, close, volume, `values`)
             VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(
        sql,
        (
            price.date,
            price.symbol,
            price.open,
            price.high,
            price.low,
            price.close,
            price.volume,
            price.values,
        ),
    )
    conn.commit()
    logger.info(f"{price} inserted into 'price'.")
