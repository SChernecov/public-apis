import pytest
from api_methods.public_api_client import PublicApiClient


@pytest.fixture(scope="session")
def client(request):
    base_url = request.config.getoption("--url")
    return PublicApiClient(base_url=base_url)
