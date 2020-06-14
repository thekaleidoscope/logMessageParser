import re

from main.domain.LogMessage.LogMessage import LogMessage
from main.domain.MessageType import MessageType
from main.domain.Unknown import Unknown


class ErrorLogMessage(LogMessage):
    def __init__(self, messageType, logLevel, timestamp, message) -> None:
        self.messageType = messageType
        self.logLevel = logLevel
        self.timestamp = timestamp
        self.message = message

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and \
               self.message == other.message and \
               self.timestamp == other.timestamp and \
               self.logLevel == other.logLevel and \
               self.messageType == other.messageType

    @classmethod
    def parse(cls, input_log_message):
        expected_pattern = 'E\s(\d*)\s(\d*)\s(.*)'
        match = re.search(expected_pattern, input_log_message)
        if match:
            return ErrorLogMessage(MessageType.ERROR, int(match.group(1)), int(match.group(2)), match.group(3))
        else:
            return Unknown(input_log_message)