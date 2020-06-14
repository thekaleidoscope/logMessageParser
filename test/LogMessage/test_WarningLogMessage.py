import unittest

from main.domain.LogMessage.WarningLogMessage import WarningLogMessage
from main.domain.MessageType import MessageType
from main.domain.Unknown import Unknown


class WarningLogMessageTest(unittest.TestCase):

    def test_shouldParseInputWarningLog(self):
        input_log_message = "W 6 Completed armadillo processing"
        expected_log_message = WarningLogMessage(MessageType.WARNING, 6, "Completed armadillo processing")

        log_message_parsed = WarningLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldParseInputWarnLogWithMultipleNumericalValues(self):
        input_log_message = "W 6 312489 Completed armadillo processing"
        expected_log_message = WarningLogMessage(MessageType.WARNING, 6, "312489 Completed armadillo processing")

        log_message_parsed = WarningLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedWarningLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = WarningLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)
