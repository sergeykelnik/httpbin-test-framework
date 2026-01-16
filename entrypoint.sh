#!/bin/sh
# Run tests; always exit 0 so downstream services start regardless of test result
pytest tests/ -v --tb=short --alluredir=allure-results ${PYTEST_ARGS:-}
exit 0
