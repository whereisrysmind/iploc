import pytest

from settings import settings
from src.ipstack import IPStackClient
from src.schemas import IPInformation

EXPECTED_PAYLOAD1 = {'ip': '134.201.250.155', 'type': 'ipv4', 'continent_code': 'NA', 'continent_name': 'North America', 'country_code': 'US', 'country_name': 'United States', 'region_code': 'CA', 'region_name': 'California', 'city': 'Los Angeles', 'zip': '90012', 'latitude': 34.0655517578125, 'longitude': -118.24053955078125, 'location': {'geoname_id': 5368361, 'capital': 'Washington D.C.', 'languages': [{'code': 'en', 'name': 'English', 'native': 'English'}], 'country_flag': 'https://assets.ipstack.com/flags/us.svg', 'country_flag_emoji': '🇺🇸', 'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8', 'calling_code': '1', 'is_eu': False}}
EXPECTED_PAYLOAD2 = {'ip': '76.28.126.17', 'type': 'ipv4', 'continent_code': 'NA', 'continent_name': 'North America', 'country_code': 'US', 'country_name': 'United States', 'region_code': 'CT', 'region_name': 'Connecticut', 'city': 'Madison', 'zip': '06475', 'latitude': 41.286399841308594, 'longitude': -72.40028381347656, 'location': {'geoname_id': 4838116, 'capital': 'Washington D.C.', 'languages': [{'code': 'en', 'name': 'English', 'native': 'English'}], 'country_flag': 'https://assets.ipstack.com/flags/us.svg', 'country_flag_emoji': '🇺🇸', 'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8', 'calling_code': '1', 'is_eu': False}}

@pytest.mark.parametrize('ip_address, expected',
    [
        ('134.201.250.155', IPInformation(**EXPECTED_PAYLOAD1)),
        ('76.28.126.17', IPInformation(**EXPECTED_PAYLOAD2))
    ]
)
def test_get_ip_info(ip_address, expected):
    """
    GIVEN: A configured .env file
    WHEN: IPStackClient.get_ipstack_data is called
    THEN: The expected data is gathered and returned about the ip address
    """
    ipstack_client = IPStackClient(settings)
    ip_info = ipstack_client.get_ipaddress_info(ip_address)

    assert ip_info.dict() == expected.dict()