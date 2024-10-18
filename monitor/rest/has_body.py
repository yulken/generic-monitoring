from monitor.rest.generic import GenericRestMonitor

class HasBodyRestValidation(GenericRestMonitor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self) -> bool:
        result = False
        try:
            response = super()._execute_request()
            result = response.ok
            if result and not response.content:
                raise Exception
                
        except:
            return False
        return result