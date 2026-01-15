from utils.retry_decorator import retry


@retry()
def test_brotli_returns_brotli_encoded_data(api_client):
    """Test GET /brotli returns Brotli-encoded data"""
    response = api_client.get("/brotli")
        
    assert response.status_code == 200
    data = response.json()

    assert "brotli" in data
    assert data["brotli"] is True

@retry()
def test_deflate_returns_deflate_encoded_data(api_client):
    """Test GET /deflate returns Deflate-encoded data"""
    response = api_client.get("/deflate")

    assert response.status_code == 200
    data = response.json()

    assert "deflated" in data
    assert data["deflated"] is True

@retry()
def test_deny_returns_denied_page(api_client):
    """Test GET /deny returns page denied by robots.txt"""
    response = api_client.get("/deny")

    assert response.status_code == 200
    assert "text/plain" in response.headers.get("Content-Type", "")
    assert "YOU SHOULDN'T BE HERE" in response.text.upper()

@retry()
def test_encoding_utf8_returns_utf8_body(api_client):
    """Test GET /encoding/utf8 returns UTF-8 encoded body"""
    response = api_client.get("/encoding/utf8")

    assert response.status_code == 200
    assert response.encoding.lower() == 'utf-8'
    assert len(response.text) > 0

@retry()
def test_gzip_returns_gzip_encoded_data(api_client):
    """Test GET /gzip returns GZip-encoded data"""
    response = api_client.get("/gzip")

    assert response.status_code == 200
    data = response.json()

    assert "gzipped" in data
    assert data["gzipped"] is True

@retry()
def test_html_returns_html_document(api_client):
    """Test GET /html returns simple HTML document"""
    response = api_client.get("/html")

    assert response.status_code == 200
    assert "text/html" in response.headers.get("Content-Type", "")
    assert "<html>" in response.text.lower()

@retry()
def test_json_returns_json_document(api_client):
    """Test GET /json returns simple JSON document"""
    response = api_client.get("/json")

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()
    assert isinstance(data, dict)

@retry()
def test_robots_txt_returns_robots_rules(api_client):
    """Test GET /robots.txt returns robots.txt rules"""
    response = api_client.get("/robots.txt")

    assert response.status_code == 200
    assert "text/plain" in response.headers.get("Content-Type", "")
    assert "User-agent:" in response.text or "Disallow:" in response.text

@retry()
def test_xml_returns_xml_document(api_client):
    """Test GET /xml returns simple XML document"""
    response = api_client.get("/xml")

    assert response.status_code == 200
    assert "application/xml" in response.headers.get("Content-Type", "")
    assert "<?xml" in response.text