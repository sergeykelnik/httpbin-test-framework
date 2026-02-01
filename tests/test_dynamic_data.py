import base64
import json
import time
from uuid import UUID

import pytest

from utils.retry_decorator import retry
from utils.test_data_generator import test_data


@retry()
def test_base64_decodes_value(api_client):
    """Test GET /base64/{value} decodes base64url-encoded string"""
    test_string = test_data.random_sentence(3)
    base64_str = base64.b64encode(
        bytes(test_string, 'utf-8')).decode('utf-8')
    response = api_client.get(f"/base64/{base64_str}")

    assert response.status_code == 200
    assert test_string in response.text


@retry()
def test_bytes_returns_n_random_bytes(api_client):
    """Test GET /bytes/{n} returns n random bytes"""
    bytes = test_data.random_integer(1, 512)
    response = api_client.get(f"/bytes/{bytes}")

    assert response.status_code == 200
    assert len(response.content) == bytes


@retry()
@pytest.mark.parametrize("method", ["GET", "DELETE", "PATCH", "POST", "PUT"])
def test_delay_returns_delayed_response(api_client, method):
    """Test delay endpoints return delayed responses"""
    delay = test_data.random_integer(1, 5)
    start_time = time.time()
    response = api_client.request(method, f"/delay/{delay}")
    elapsed_time = time.time() - start_time

    assert response.status_code == 200
    assert elapsed_time >= delay
    assert elapsed_time < delay + 2


@retry()
def test_drip_returns_dripped_data(api_client):
    """Test GET /drip returns data over duration"""

    duration = test_data.random_integer(1, 5)
    numbytes = test_data.random_integer(10, 50)
    code = test_data.random_integer(200, 500)
    delay = test_data.random_integer(1, 5)

    start_time = time.time()
    response = api_client.get("/drip", params={
        "duration": duration,
        "numbytes": numbytes,
        "code": code,
        "delay": delay
    })
    elapsed = time.time() - start_time

    assert response.status_code == code
    assert len(response.content) == numbytes
    # Should take at least delay + duration = 4 seconds
    assert elapsed >= delay + duration


@retry()
def test_links_generates_page_with_links(api_client):
    """Test GET /links/{n}/{offset} generates page with n links"""
    pages = test_data.random_integer(1, 10)
    offset = test_data.random_integer(1, 10)
    response = api_client.get(f"/links/{pages}/{offset}")

    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "")

    assert f"<a href='/links/{pages}" in response.text


@retry()
def test_range_streams_numbytes(api_client):
    """Test GET /range/{numbytes} streams n random bytes"""
    numbytes = test_data.random_integer(1, 512)
    response = api_client.get(f"/range/{numbytes}", stream=True)

    assert len(response.content) == numbytes
    assert response.headers.get("Content-Length") == str(numbytes)
    assert response.headers.get(
        "Content-Range") == f"bytes 0-{numbytes - 1}/{numbytes}"
    assert response.headers.get("Accept-Ranges") == "bytes"


@retry()
def test_stream_bytes_returns_n_bytes(api_client):
    """Test GET /stream-bytes/{n} streams n random bytes"""
    numbytes = test_data.random_integer(1, 512)
    response = api_client.get(f"/range/{numbytes}", stream=True)

    chunks = []
    for chunk in response.iter_content(chunk_size=None):
        chunks.append(chunk)

    assert response.status_code == 200
    total_bytes = b''.join(chunks)
    assert len(total_bytes) == numbytes
    assert len(response.content) == numbytes


@retry()
def test_stream_returns_n_json_responses(api_client):
    """Test GET /stream/{n} streams n JSON responses"""
    response_number = test_data.random_integer(1, 5)
    response = api_client.get(f"/stream/{response_number}")

    assert response.status_code == 200
    json_responses = response.text.strip().split('\n')

    assert len(json_responses) == response_number
    check_ids = set()
    for line in json_responses:
        data = json.loads(line)
        check_ids.add(data.get("id"))
    # check ids are from 0 to response_number -1
    assert check_ids == set(range(response_number))


@retry()
def test_uuid_returns_valid_uuid4(api_client):
    """Test GET /uuid returns valid UUID4"""
    response = api_client.get("/uuid")

    assert response.status_code == 200
    data = response.json()

    assert "uuid" in data

    uuid_obj = UUID(data["uuid"])
    assert uuid_obj.version == 4


@retry()
def test_uuid_generates_different_values(api_client):
    """Test GET /uuid generates different UUIDs on each call"""
    response1 = api_client.get("/uuid")
    response2 = api_client.get("/uuid")

    uuid1 = response1.json()["uuid"]
    uuid2 = response2.json()["uuid"]

    assert uuid1 != uuid2
