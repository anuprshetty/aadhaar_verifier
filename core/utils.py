import os
import time
from flask import current_app, request, has_request_context
import logging
from .custom_exceptions import TaskApiException


def timeit(method):
    def timed(*args, **kwargs):
        method_name = method.__name__
        try:
            try:
                start_time = time.perf_counter()
                result = method(*args, **kwargs)
                end_time = time.perf_counter()
                time_taken_ms = (end_time - start_time) * 1000
                current_app.logger.info(
                    f"Method {method_name} executed in {time_taken_ms:5.2f} ms"
                )

                return result

            except Exception as e:
                task_api_error_response_model = {
                    "code": 422,
                    "message": f"Error while computing execution time of the method {method_name}: {e}",
                }
                raise TaskApiException(task_api_error_response_model)
        except TaskApiException as e:
            return e.task_api_error_response_model, e.task_api_error_response_model.get(
                "code"
            )

    return timed


class LogFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """

    def filter(self, record):
        record.microServiceID = os.getenv(key="MICRO_SERVICE_ID")
        record.url = request.path if has_request_context() else None

        return True
