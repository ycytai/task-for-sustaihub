import re

from pipelines.base import BaseCleaningPipeline


class StockPriceCP(BaseCleaningPipeline):
    def _extract_sign(self, value: str) -> str:
        """
        Example:
        >>> print(value)
        <p style= color:green>-</p>
        """
        pattern = r'<p.*?>(.*?)<\/p>'
        matches = re.findall(pattern, value)
        if matches:
            return matches[0]
        else:
            raise ValueError('Invalid format. Cannot extract text.')

    def _cleaning(self, data: dict) -> dict:
        num_fields = {
            'open',
            'high',
            'low',
            'close',
            'last_revealed_buy_price',
            'last_revealed_buy_volume',
            'last_revealed_sell_price',
            'last_revealed_sell_volume',
        }
        cleaned_data = data.copy()
        cleaned_data = self._remove_comma(cleaned_data)
        if cleaned_data.get('sign'):
            cleaned_data['sign'] = self._extract_sign(cleaned_data.get('sign'))
        for field in num_fields:
            cleaned_data[field] = self._turn_num_string_to_decimal(
                cleaned_data.get(field)
            )
        return cleaned_data

    def run(self, data: list[dict]) -> list[dict]:
        output = []
        for d in data:
            output.append(self._cleaning(d))
        return output
