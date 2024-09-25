from datetime import date as Date

from pydantic import Field

from domain.value_object import ValueObject


class StockPrice(ValueObject):
    date: Date = Field(title='日期', examples=['2024-05-15'])
    symbol: str = Field(title='證券代號', examples=['2330'])
    open: float | None = Field(title='開盤價', examples=['838.00'])
    high: float | None = Field(title='最高價', examples=['844.00'])
    low: float | None = Field(title='最低價', examples=['837.00'])
    close: float | None = Field(title='收盤價', examples=['839.00'])
    volume: float | None = Field(title='成交股數', examples=['41805778.00'])
    values: float | None = Field(title='成交金額', examples=['35112739055.00'])
