import requests
from pydantic_settings import BaseSettings

from src.schemas import IPInformation


class IPStackConnectionError(Exception):
    pass


class IPStackClient():
    def __init__(self, settings: BaseSettings):
        """Initialize the IPStackClient object with the API key and host from settings"""
        self._ipstack_api_key = settings.ipstack_api_key.get_secret_value()
        self._ipstack_api_host = settings.ipstack_api_host

    def get_ipaddress_info(self, ip_address: str) -> IPInformation:
        """Get All IP Address info from IPStack API"""
        url = f"http://{self._ipstack_api_host}/{ip_address}?access_key={self._ipstack_api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return IPInformation(**response.json())
        else:
            raise IPStackConnectionError(f"IPStack API returned status code {response.status_code}: {response.text}")
