import random
from urllib.parse import urljoin

import httpx
from pydantic import Field
from pydantic_settings import BaseSettings


class HttpServiceSettings(BaseSettings):
    base_url: str
    timeout: int = Field(10)


class HttpService:
    def __init__(self, settings: HttpServiceSettings):
        self.settings = settings

    def get(self, endpoint: str, **kwargs):
        url = urljoin(self.settings.base_url, endpoint)
        return httpx.get(
            url, headers=self.headers, timeout=self.settings.timeout, **kwargs
        )

    def post(self, endpoint: str, **kwargs):
        url = urljoin(self.settings.base_url, endpoint)
        return httpx.post(
            url, headers=self.headers, timeout=self.settings.timeout, **kwargs
        )

    @property
    def headers(self) -> dict:
        # List of common User-Agent strings from different browsers and devices
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        ]
        # Randomly select a User-Agent from the list
        user_agent = random.choice(user_agents)

        # Additional headers to more closely mimic a browser request
        return {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }
