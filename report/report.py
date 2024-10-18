from typing import List
from monitor.monitor import Monitor


class Colors:
    GREEN = '\033[92m]'
    FAIL = '\033[91m]'
    ENDC = '\033[0m]'


class Report:
    def __init__(self, description: str, integrations: List[Monitor]):
        self._description = description
        self._integrations = integrations
    
    def validate(self):
        print("Project: {0}".format(self._description))
        for integration in self._integrations:
            print(self._format_string(integration.validate(), integration.get_description()))

    def _format_string(self, result: bool, name: str) -> str:
        color = None
        result_str = None
        if (result):
            result_str = "OK"
            color = Colors.GREEN
        else:
            result_str = "UNAVAILABLE"
            color = Colors.FAIL

        return "\tSystem: {0:40} Status: {2}{1}{3}".format(name, result_str, color, Colors.ENDC)