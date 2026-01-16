# Docker Setup

## Quick Start

For local development (using current directory):
```bash
docker-compose up --build
```

Tests run automatically. View Allure report at: http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html

To build from GitHub repository:
```bash
git clone https://github.com/sergeykelnik/httpbin-test-framework.git
cd httpbin-test-framework
docker-compose up --build
```

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
