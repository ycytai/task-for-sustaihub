from datetime import date as Date

from loguru import logger

from database.operations import insert_collect_record, insert_price
from database.session import create_connection
from modules.general.enums import CollectResult, DataType
from modules.general.value_objects import CollectRecord
from modules.services import get_twse_service
from modules.stock.value_objects import StockPrice
from pipelines.stock import StockPriceCP


# NOTE: For demo purpose, we will use a simple function to simulate the task.
def get_stock_price_task(date: Date = Date.today()):
    conn = create_connection()

    try:
        # get data
        twse_service = get_twse_service()
        data = twse_service.get_stock_price(date)

        # clean data
        pipeline = StockPriceCP()
        cleaned_data = pipeline.run(data=data)

        # insert data
        for d in cleaned_data:
            price = StockPrice(**d, date=date)
            insert_price(conn, price)

        insert_collect_record(
            conn,
            CollectRecord(
                date=date, data_type=DataType.STOCK_PRICE, result=CollectResult.SUCCESS
            ),
        )
        logger.info(f'{str(date)} Stock price collect task is done')

    except Exception as e:
        insert_collect_record(
            conn,
            CollectRecord(
                date=date,
                data_type=DataType.STOCK_PRICE,
                result=CollectResult.FAIL,
                reason=str(e),
            ),
        )
        logger.debug(e)
