class Unknown:
    def __init__(self, message) -> None:
        self.message = message

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.message == other.message


