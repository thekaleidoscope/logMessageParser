class LogMessage:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @classmethod
    def parse(cls, input_log_message):
        pass
