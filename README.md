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
docker-compose up --build
```

The pytest service runs tests on start and always exits 0 so the Allure service comes up even if tests fail. View reports at http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html once containers are up.

See [DOCKER.md](DOCKER.md) for details.

