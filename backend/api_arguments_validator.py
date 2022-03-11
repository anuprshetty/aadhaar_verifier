class ApiArgumentsValidator:

    def __init__(self, otp=None, aadhaar_no=None):
        self._otp = otp
        self._aadhaar_no = aadhaar_no

    @property
    def otp(self):
        return self._otp

    @property
    def aadhaar_no(self):
        return self._aadhaar_no
