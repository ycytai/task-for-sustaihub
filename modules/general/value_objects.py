from datetime import date as Date

from pydantic import Field

from domain.value_object import ValueObject

from .enums import CollectResult, DataType


class CollectRecord(ValueObject):
    date: Date = Field(title='交易日')
    data_type: DataType = Field(title='資料類型')
    result: CollectResult = Field(title='蒐集結果')
    reason: str | None = Field(None, title='失敗原因')
