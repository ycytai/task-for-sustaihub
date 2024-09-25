import abc
from decimal import Decimal


class BaseCleaningPipeline(abc.ABC):
    """
    Base class for a data cleaning pipeline.

    NOTE: use `CP` across system to represent `Cleaning Pipeline`
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def _cleaning(self):
        """
        Abstract method for source-specific cleaning logic.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def run(self):
        """
        Complete pipeline process: load, clean, and return the cleaned data.
        """
        raise NotImplementedError()

    def _remove_comma(self, data: dict) -> dict:
        for k, v in data.items():
            data[k] = v.replace(',', '') if isinstance(v, str) else v
        return data

    def _turn_num_string_to_decimal(
        self, value: str, error_return: Decimal | None = None
    ) -> Decimal | None:
        try:
            return Decimal(value)
        except Exception:
            return error_return

    def _chi_to_ad_year(self, year: int) -> int:
        return year + 1911

    def _ad_to_chi_year(self, year: int) -> int:
        return year - 1911
