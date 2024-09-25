import sqlite3

from loguru import logger


def create_collect_record_table(conn):
    try:
        cur = conn.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS collect_record (
            date TEXT NOT NULL,
            data_type TEXT NOT NULL,
            result TEXT NOT NULL,
            reason TEXT,
            PRIMARY KEY (date, data_type)
        );
        """
        cur.execute(create_table_sql)
        logger.info("Table 'collect_record' created successfully.")
    except sqlite3.Error as e:
        logger.debug(e)


def create_price_table(conn):
    try:
        cur = conn.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS price (
            date TEXT NOT NULL,
            symbol TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            `values` REAL,
            PRIMARY KEY (date, symbol)
        );
        """
        cur.execute(create_table_sql)
        logger.info("Table 'price' created successfully.")
    except sqlite3.Error as e:
        logger.debug(e)


def create_connection(db_name: str = 'demo.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        logger.info(f'Connected to SQLite database: {db_name}')
        return conn
    except sqlite3.Error as e:
        logger.debug(e)


def initialize():
    # Create a database connection
    conn = create_connection('demo.db')

    # Create tables if the connection is successful
    if conn is not None:
        create_collect_record_table(conn)
        create_price_table(conn)
        conn.close()
        logger.info('Database initialization completed.')
    else:
        logger.debug('Error! Cannot create the database connection.')


if __name__ == '__main__':
    # NOTE: For demo purpose, we make initialization simple.
    initialize()
