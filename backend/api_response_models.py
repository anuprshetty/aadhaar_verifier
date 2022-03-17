from flask_restx import fields

from .aadhaar_verifier_api_namespace import aadhaar_verifier_api_ns


# api response models
uidai_generate_otp_api_response_model = aadhaar_verifier_api_ns.model(
    name="uidai_generate_otp_api_response_model",
    model={"status": fields.String(required=True, description="Status")},
)

uidai_verify_aadhaar_api_response_model = aadhaar_verifier_api_ns.model(
    name="uidai_verify_aadhaar_api_response_model",
    model={
        "status": fields.String(required=True, description="Status"),
        # 'aadhaar_info': {
        #     'aadhaar_no': fields.String(required=False, description='aadhaar_no'),
        #     'name': fields.String(required=False, description='name'),
        #     'dob': fields.String(required=False, description='dob'),
        #     'gender': fields.String(required=False, description='gender'),
        #     'address': fields.String(required=False, description='address')
        # }
    },
)

task_api_400_error_response_model = aadhaar_verifier_api_ns.model(
    name="task_api_400_error_response_model",
    model={
        "code": fields.Integer(example=400),
        "message": fields.String(example="BAD REQUEST"),
    },
)

task_api_422_error_response_model = aadhaar_verifier_api_ns.model(
    name="task_api_422_error_response_model",
    model={
        "code": fields.Integer(example=422),
        "message": fields.String(example="UNPROCESSABLE ENTITY"),
    },
)

task_api_500_error_response_model = aadhaar_verifier_api_ns.model(
    name="task_api_500_error_response_model",
    model={
        "code": fields.Integer(example=500),
        "message": fields.String(example="INTERNAL SERVER ERROR"),
    },
)
