from main.domain.LogMessage.LogMessage import LogMessage
from main.domain.Unknown import Unknown


def parse(input_log) -> LogMessage or Unknown:
    parsed_log_message = Unknown('')
    for logMessage in LogMessage.subclasses:
        parsed_log_message = logMessage.parse(input_log)
        if not isinstance(parsed_log_message, Unknown):
            return parsed_log_message

    return parsed_log_message
