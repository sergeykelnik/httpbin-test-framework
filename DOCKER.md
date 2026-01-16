# Docker Setup

## Quick Start

For local development (using current directory):
```bash
# Run tests
docker-compose run --rm pytest

# Then start Allure service to view results
docker-compose up allure
```

View Allure report at: http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html

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
