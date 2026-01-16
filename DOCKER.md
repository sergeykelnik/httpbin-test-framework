# Docker Setup

## Quick Start
```bash
docker-compose up --build
```

Tests run automatically. View Allure report at: http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html

## Run Tests
```bash
# All tests
docker-compose run --rm pytest

# Specific file
docker-compose run --rm pytest tests/test_response_formats.py

# With custom arguments
docker-compose run --rm -e PYTEST_ARGS="-v -k test_status" pytest

# Interactive shell
docker-compose run --rm pytest bash
```

## Environment Variables
- `BASE_URL`: API endpoint (default: `https://httpbin.org`)
- `PYTEST_ARGS`: Pytest arguments

## Cleanup
```bash
docker-compose down -v
```
