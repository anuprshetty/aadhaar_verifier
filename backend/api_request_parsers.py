from .aadhaar_verifier_api_namespace import aadhaar_verifier_api_ns


# api request parsers
uidai_generate_otp_api_request_parser = aadhaar_verifier_api_ns.parser()
uidai_generate_otp_api_request_parser.add_argument(
    name="aadhaar_no",
    required=True,
    type=str,
    ignore=False,
    location="form",
    help="Aadhaar No. Ex: 123456789011",
    trim=True,
    nullable=False,
)

uidai_verify_aadhaar_api_request_parser = aadhaar_verifier_api_ns.parser()
uidai_verify_aadhaar_api_request_parser.add_argument(
    name="aadhaar_no",
    required=True,
    type=str,
    ignore=False,
    location="form",
    help="Aadhaar No. Ex: 123456789011",
    trim=True,
    nullable=False,
)
uidai_verify_aadhaar_api_request_parser.add_argument(
    name="otp",
    required=True,
    type=str,
    ignore=False,
    location="form",
    help="OTP. Ex: 123456",
    trim=True,
    nullable=False,
)
