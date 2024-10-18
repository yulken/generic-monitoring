from typing import List
from dotenv import load_dotenv
from monitor.monitor import Monitor
from monitor.rest.generic import GenericRestMonitor
from monitor.rest.has_body import HasBodyRestMonitor
from integrations import Integration

def __main__():
    load_dotenv()



def first_project() -> List[Monitor]:
    monitors = []
    monitors.append(GenericRestMonitor(**Integration.EXAMPLE_REQUEST))
    monitors.append(HasBodyRestMonitor(**Integration.EXAMPLE_REQUEST_WITH_POST))
    return monitors

__main__()