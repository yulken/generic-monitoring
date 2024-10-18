from typing import Dict
from monitor.monitor import Monitor
from requests import Response, get, post

class GenericRestMonitor(Monitor):
    def __init__(self, description: str, method: str, url: str, json = None, headers: Dict = None):
        self._description = description
        self._method = method
        self._url = url
        self._json = json
        self._headers = headers

    def validate(self) -> bool:
        result = False
        try:
            response = self._execute_request()
            result = response.ok
        except:
            return False
        return result

    def get_description(self):
        return self._description

    def _execute_request(self) -> Response:
        if self._method == 'GET':
            return get(url = self._url)
        elif self._method == 'POST':
            return post(url = self._url, json = self._json, headers = self._headers)
