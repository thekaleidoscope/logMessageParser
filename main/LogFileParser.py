from main import LogMessageParser
from main.domain.LogMessage.LogMessage import LogMessage
from main.domain.Unknown import Unknown


def parse(file_path: str) -> [LogMessage]:
    log_messages = []
    with open(file_path) as logFile:

        for log_message in logFile:
            parsed_log_message = LogMessageParser.parse(log_message)
            if not isinstance(parsed_log_message, Unknown):
                log_messages.append(parsed_log_message)
    return log_messages
