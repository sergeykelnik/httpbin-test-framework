import time
import functools
import logging
import requests
from .config_loader import config

logger = logging.getLogger(__name__)

def log_http(response, level=logging.INFO):
    if response is None:
        return

    request = response.request
    logger.log(level, "---- HTTP REQUEST ----")
    logger.log(level, f"{request.method} {request.url}")
    logger.log(level, f"Headers: {dict(request.headers)}")
    logger.log(level, f"Body: {request.body}")

    logger.log(level, "---- HTTP RESPONSE ----")
    logger.log(level, f"Status: {response.status_code}")
    logger.log(level, f"Headers: {dict(response.headers)}")
    logger.log(level, f"Body: {response.text}")

def retry(
    times=config.max_retry_attempts,
    delay=config.retry_delay,
    exceptions=(AssertionError, requests.RequestException),
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            original_request = requests.Session.request

            def logged_request(self, method, url, **kwargs):
                response = original_request(self, method, url, **kwargs)
                log_http(response)
                return response

            for attempt in range(1, times + 1):
                try:
                    logger.info(f"Attempt {attempt}/{times} for {func.__name__}")
                    requests.Session.request = logged_request
                    return func(*args, **kwargs)
                
                except exceptions as e:
                    logger.warning(
                        f"Exception on attempt {attempt}/{times}: {e}"
                    )

                    response = getattr(e, "response", None)
                    if response is not None:
                        log_http(response, level=logging.WARNING)

                    if attempt == times:
                        logger.exception("Retries exhausted")
                        raise

                    if delay:
                        time.sleep(delay)

                finally:
                    requests.Session.request = original_request

        return wrapper
    return decorator  