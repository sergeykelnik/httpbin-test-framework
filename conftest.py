import pytest
import requests
from utils.config_loader import config

@pytest.fixture()
def api_client():
    """Create API client with retry logic"""
    class APIClient:
        def __init__(self):
            self.base_url = config.base_url
            self.timeout = config.timeout

        def request(self, method, endpoint, **kwargs):
            url = f"{self.base_url}{endpoint}"
            kwargs.setdefault('timeout', self.timeout)
            return requests.request(method, url, **kwargs)

        def get(self, endpoint, **kwargs):
            response = self.request('GET', endpoint, **kwargs)
            return response

        def post(self, endpoint, **kwargs):
            response = self.request('POST', endpoint, **kwargs)
            return response

        def put(self, endpoint, **kwargs):
            response = self.request('PUT', endpoint, **kwargs)
            return response

        def delete(self, endpoint, **kwargs):
            response = self.request('DELETE', endpoint, **kwargs)
            return response

        def patch(self, endpoint, **kwargs):
            response = self.request('PATCH', endpoint, **kwargs)
            return response

    return APIClient()