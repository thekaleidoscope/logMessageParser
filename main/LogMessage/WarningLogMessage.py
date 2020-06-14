import re

from main.LogMessage.LogMessage import LogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class WarningLogMessage(LogMessage):
    def __init__(self, messageType, timestamp, message) -> None:
        self.messageType = messageType
        self.timestamp = timestamp
        self.message = message

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and \
               self.message == other.message and \
               self.timestamp == other.timestamp and \
               self.messageType == other.messageType

    @classmethod
    def parse(cls, input_log_message):
        expected_pattern = 'W\s(\d*)\s(.*)'
        match = re.search(expected_pattern, input_log_message)
        if match:
            return WarningLogMessage(MessageType.WARNING, int(match.group(1)), match.group(2))
        else:
            return Unknown(input_log_message)
