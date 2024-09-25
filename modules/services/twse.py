from datetime import date as Date

from pydantic_settings import SettingsConfigDict

from infra.http_service import HttpService, HttpServiceSettings
from modules.services.exceptions import ExceedDataRangeError


class TwseServiceSettings(HttpServiceSettings):
    model_config = SettingsConfigDict(env_prefix='TWSE_', env_file_encoding='utf-8')


class TwseService(HttpService):
    def __init__(self, settings: TwseServiceSettings) -> None:
        self.base_url = settings.base_url
        self.settings = settings

    def get_stock_price(self, date: Date) -> list[dict]:

        data_start_dates = Date(year=2004, month=3, day=1)
        if date < data_start_dates:
            raise ExceedDataRangeError(start=str(data_start_dates))

        params = {
            'response': 'json',
            'date': str(date.strftime('%Y%m%d')),  # e.g. 20231229
            'type': 'ALLBUT0999',  # 全部(不含權證、牛熊證、可展延牛熊證)
        }
        result = self.get('/exchangeReport/MI_INDEX', params=params)
        data = result.json()

        # 2011/8/1 開始，response 裡的資料變成放在 data9
        # 所有資料從 2004/2/11 開始
        if date >= Date(year=2011, month=8, day=1):
            fk = 'fields9'
            dk = 'data9'
        else:
            fk = 'fields8'
            dk = 'data8'

        fields = data[fk]
        stock_data = data[dk]

        output = []
        for s in stock_data:
            d = dict(zip(fields, s))
            symbol = d.get('證券代號')
            if len(symbol) == 4 and not symbol.startswith('0'):
                output.append(
                    {
                        'symbol': d.get('證券代號'),
                        'name': d.get('證券名稱'),
                        'volume': d.get('成交股數'),
                        'count': d.get('成交筆數'),
                        'values': d.get('成交金額'),
                        'open': d.get('開盤價'),
                        'high': d.get('最高價'),
                        'low': d.get('最低價'),
                        'close': d.get('收盤價'),
                        'sign': d.get('漲跌'),
                        'change': d.get('漲跌價差'),
                        'last_revealed_buy_price': d.get('最後揭示買價'),
                        'last_revealed_buy_volume': d.get('最後揭示買量'),
                        'last_revealed_sell_price': d.get('最後揭示賣價'),
                        'last_revealed_sell_volume': d.get('最後揭示賣量'),
                        'pe': d.get('本益比'),
                    }
                )
        return output


def get_twse_service_settings() -> TwseServiceSettings:
    return TwseServiceSettings()


def get_twse_service() -> TwseService:
    return TwseService(get_twse_service_settings())
