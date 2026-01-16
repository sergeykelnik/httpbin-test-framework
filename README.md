# httpbin-test-framework

Pytest-based test framework for https://httpbin.org

## Setup
```bash
pip install -r requirements.txt
```

## Run Tests
```bash
pytest
pytest tests/test_response_formats.py
pytest --alluredir=allure-results
```

## Docker
```bash
docker-compose up
```

See [DOCKER.md](DOCKER.md) for details.

