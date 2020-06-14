import unittest

from main import LogMessageParser
from main.domain.LogMessage.ErrorLogMessage import ErrorLogMessage
from main.domain.LogMessage.InformationLogMessage import InformationLogMessage
from main.domain.LogMessage.WarningLogMessage import WarningLogMessage
from main.domain.MessageType import MessageType
from main.domain.Unknown import Unknown


class LogMessageParsingTest(unittest.TestCase):

    def test_shouldBeAbleToParseInfoLog(self):
        input_log_message = "I 6 Completed armadillo processing"
        expected_log_message = InformationLogMessage(MessageType.INFO, 6, "Completed armadillo processing")

        log_message_parsed = LogMessageParser.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldBeAbleToParseWarningLog(self):
        input_log_message = "W 6 Completed armadillo processing"
        expected_log_message = WarningLogMessage(MessageType.WARNING, 6, "Completed armadillo processing")

        log_message_parsed = LogMessageParser.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldBeAbleToParseErrorLog(self):
        input_log_message = "E 100 6 Completed armadillo processing"
        expected_log_message = ErrorLogMessage(MessageType.ERROR, 100, 6, "Completed armadillo processing")

        log_message_parsed = LogMessageParser.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenIncorrectLogMessageIsInput(self):
        input_log_messages = [
            "Completed armadillo processing",
            "I Completed armadillo processing",
            "W Completed armadillo processing",
            "E 1 Completed armadillo processing",
            "E Completed armadillo processing",
        ]

        for input_log_message in input_log_messages:
            expected_log_message = Unknown(input_log_message)
            log_message_parsed = LogMessageParser.parse(input_log_message)
            self.assertEqual(expected_log_message, log_message_parsed)
