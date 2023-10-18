import pytest


@pytest.fixture
def mock_settings(mocker):
    _settings = mocker.MagicMock()
    _settings.ipstack_api_host = "foo.ipstack.com"
    _settings.ipstack_api_key.get_secret_value.return_value = "super-secret-key"
    
    return _settings

@pytest.fixture
def mock_response(mocker):
    _response = ""
