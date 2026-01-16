import re
from utils.retry_decorator import retry

@retry()
def test_headers_returns_request_headers(api_client):
    """Test GET /headers returns incoming request headers"""
    response = api_client.get("/headers")

    assert response.status_code == 1200
    data = response.json()

    assert "headers" in data
    assert len(data["headers"]) > 0

@retry()
def test_ip_returns_requester_ip(api_client):
    """Test GET /ip returns requester's IP address"""
    response = api_client.get("/ip")

    assert response.status_code == 200
    data = response.json()

    assert "origin" in data
    origin = data["origin"]
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv6_pattern = r'[0-9a-fA-F]*:[0-9a-fA-F:]*'

    assert re.search(ipv4_pattern, origin) or re.search(ipv6_pattern, origin), \
    f"No valid IP address found in origin: {origin}"

@retry()
def test_user_agent_returns_user_agent_header(api_client):
    """Test GET /user-agent returns incoming User-Agent header"""
    response = api_client.get("/user-agent")

    assert response.status_code == 200
    data = response.json()

    assert "user-agent" in data
    assert len(data["user-agent"]) > 0