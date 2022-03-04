from flask import current_app


class TaskApiException(Exception):

    def __init__(self, task_api_error_response_model):
        super().__init__()

        self.task_api_error_response_model = task_api_error_response_model
        current_app.logger.error(f"Error: {self}")

    def __str__(self):
        return self.task_api_error_response_model.get("message")

    def __repr__(self):
        return self.task_api_error_response_model.get("message")
