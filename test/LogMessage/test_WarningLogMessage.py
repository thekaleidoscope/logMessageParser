import unittest

from main.LogMessage.WarningLogMessage import WarningLogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class WarningLogMessageTest(unittest.TestCase):

    def test_shouldTakeInputWarningLog(self):
        input_log_message = "W 6 Completed armadillo processing"
        expected_log_message = WarningLogMessage(MessageType.WARNING, 6, "Completed armadillo processing")

        log_message_parsed = WarningLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedWarningLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = WarningLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)