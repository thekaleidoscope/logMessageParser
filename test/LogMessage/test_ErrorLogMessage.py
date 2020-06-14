import unittest

from main.domain.LogMessage.ErrorLogMessage import ErrorLogMessage
from main.domain.MessageType import MessageType
from main.domain.Unknown import Unknown


class ErrorLogMessageTest(unittest.TestCase):
    def test_shouldParseInputErrorLog(self):
        input_log_message = "E 2 6 Completed armadillo processing"
        expected_log_message = ErrorLogMessage(MessageType.ERROR, 2, 6, "Completed armadillo processing")

        log_message_parsed = ErrorLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldParseInputErrorLogWithMultipleNumericalValues(self):
        input_log_message = "E 2 6 100 Completed armadillo processing"
        expected_log_message = ErrorLogMessage(MessageType.ERROR, 2, 6, "100 Completed armadillo processing")

        log_message_parsed = ErrorLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedErrorLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = ErrorLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)
