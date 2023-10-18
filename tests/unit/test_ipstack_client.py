import pytest
from src.ipstack import IPStackClient


def test_init_ipstack_client(mock_settings):
    """"
    GIVEN: A Settings object
    WHEN: An IPStackClient object is instantiated
    THEN: The IPStackClient object has the correct API access attributes pulled from settings
    """
    ipstack_client = IPStackClient(mock_settings)
    assert ipstack_client._ipstack_api_host == "foo.ipstack.com"
    assert ipstack_client._ipstack_api_key == "super-secret-key"


def test_request_ip_info(mock_settings, mock_response, mocker):
    """
    GIVEN: An instantiated IPStackClient object
    WHEN: IPStackClient.get_ipstack_data is called
    THEN: The correct URL is used to request IP info and an IPAddressInfo object is returned
    """
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"foo": "bar"}
    mock_request = mocker.patch("src.ipstack.requests.get", return_value=mock_response)
    mock_ip_information = mocker.patch("src.ipstack.IPInformation")

    ipstack_client = IPStackClient(mock_settings)
    ipstack_client.get_ipaddress_info('10.10.10.10')
    
    expected_url = url = f"http://{mock_settings.ipstack_api_host}/10.10.10.10?access_key={mock_settings.ipstack_api_key.get_secret_value()}"
    assert mock_request.called_once_with(expected_url)
    assert mock_ip_information.called_once_with(foo="bar")
