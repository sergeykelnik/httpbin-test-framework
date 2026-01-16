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
# Run tests
docker-compose run --rm pytest

# View results in Allure
docker-compose up allure
```

Tests and Allure services run separately. Run tests first, then start Allure to view reports at http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html

See [DOCKER.md](DOCKER.md) for details.

