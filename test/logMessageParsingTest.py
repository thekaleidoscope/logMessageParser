import unittest

from main.LogMessage import LogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class LogMessageParsingTest(unittest.TestCase):

    def test_shouldTakeInputInformationLog(self):
        input_log_message = "I 6 Completed armadillo processing"
        expected_log_message = LogMessage(MessageType.INFO, 6, "Completed armadillo processing")

        log_message_parsed = LogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = LogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)