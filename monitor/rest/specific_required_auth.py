from requests import post
import os

from monitor.rest.generic import GenericRestMonitor

AUTH_LOGIN_URL = "http://example.com/api/v1/login"

class SpecificRequiredAuthMonitor(GenericRestMonitor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self) -> bool:
        result = False
        try:
            self._authenticate()
            response = super()._execute_request()
            result = response.ok
            if result and not self._handle_response(response):
                raise Exception

        except:
            return False
        return result


    def _authenticate(self):
        result = post(AUTH_LOGIN_URL, json = {
            "user": os.getenv("EXAMPLE_USERNAME"),
            "password": os.getenv("EXAMPLE_PASSWORD")
        })
        if not self._headers:
            self._headers = {}

        self._headers["Authorization"] = "Bearer " +  result.json()["accessToken"]


    def _handle_response(self, response):
        pass