import sys
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    print("Uncaught exception", exc_type, exc_value)


class CustomException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
        self.message = message
        self.traceback = sys.exc_info()[2]
        self.exc_type = sys.exc_info()[0]
        self.exc_value = sys.exc_info()[1]


def __str__(self):
    return f"{self.exc_type.__name__}: {self.message} (Traceback: {self.traceback})"

