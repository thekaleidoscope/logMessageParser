import unittest

from main.LogMessage.ErrorLogMessage import ErrorLogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class ErrorLogMessageTest(unittest.TestCase):
    def test_shouldTakeInputErrorLog(self):
        input_log_message = "E 2 6 Completed armadillo processing"
        expected_log_message = ErrorLogMessage(MessageType.ERROR, 2, 6, "Completed armadillo processing")

        log_message_parsed = ErrorLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedErrorLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = ErrorLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)
