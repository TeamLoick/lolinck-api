class IncorrectParamsException(Exception):
    def __init__(self, details: str) -> None:
        self.details = details
