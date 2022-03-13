"""
Aadhaar Verifier API namespace which contains Aadhaar Verifier related APIs.
"""

__author__ = "Anup Shetty"
__email__ = "anup.shetty@gmail.com"


from flask import current_app
from flask_restx import Namespace, Resource
import json
import os

from core.utils import timeit
from core.custom_exceptions import TaskApiException
from .api_arguments_validator import ApiArgumentsValidator
from config import BASE_DIR
from core.constants import Status

aadhaar_verifier_api_ns = Namespace(
    name="aadhaar_verifier_api_ns",
    description="Aadhaar Verifier API Namespace",
    path="/",
)

from .api_request_parsers import *
from .api_response_models import *


@aadhaar_verifier_api_ns.route("/uidai_generate_otp/")
@aadhaar_verifier_api_ns.expect(uidai_generate_otp_api_request_parser)
class UIDAIGenerateOTP(Resource):

    @aadhaar_verifier_api_ns.doc(description="UIDAI Generate OTP")
    @aadhaar_verifier_api_ns.response(
        code=200, description="OK", model=uidai_generate_otp_api_response_model
    )
    @aadhaar_verifier_api_ns.response(
        code=400, description="BAD REQUEST", model=task_api_400_error_response_model
    )
    @aadhaar_verifier_api_ns.response(
        code=422,
        description="UNPROCESSABLE ENTITY",
        model=task_api_422_error_response_model,
    )
    @aadhaar_verifier_api_ns.response(
        code=500,
        description="INTERNAL SERVER ERROR",
        model=task_api_500_error_response_model,
    )
    @timeit
    def post(self):
        try:
            current_app.logger.info("API EXECUTION START")

            args = uidai_generate_otp_api_request_parser.parse_args()
            api_arguments_validator = ApiArgumentsValidator(**args)

            aadhaar_no = api_arguments_validator.aadhaar_no

            current_app.logger.info("Api arguments validation ... DONE")

            aadhaar_db_json_path = os.path.join(
                BASE_DIR,
                os.getenv("AADHAAR_DB_JSON_PATH", "core/aadhaar_db/aadhaar_info.json"),
            )

            with open(aadhaar_db_json_path, "r") as fd:
                aadhaar_data = json.load(fd)

            if aadhaar_no in aadhaar_data:
                status = Status.SUCCESS
            else:
                status = Status.FAILURE

            response = {"status": status}

            current_app.logger.info(f"response: {response}")

            current_app.logger.info("API EXECUTION END")

            return response, 200

        except TaskApiException as e:
            return e.task_api_error_response_model, e.task_api_error_response_model.get(
                "code"
            )
        except Exception as e:
            error_message = f"Error: {e}"
            current_app.logger.error(error_message)
            task_api_error_response_model = {"code": 422, "message": error_message}
            return task_api_error_response_model, task_api_error_response_model.get(
                "code"
            )


