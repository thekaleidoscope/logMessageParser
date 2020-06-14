import unittest

from main.LogMessage.InformationLogMessage import InformationLogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class InformationLogMessageTest(unittest.TestCase):
    def test_shouldTakeInputInformationLog(self):
        input_log_message = "I 6 Completed armadillo processing"
        expected_log_message = InformationLogMessage(MessageType.INFO, 6, "Completed armadillo processing")

        log_message_parsed = InformationLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)

    def test_shouldReturnUnknownWhenInputIncorrectlyFormattedInfoLogMessage(self):
        input_log_message = "Completed armadillo processing"
        expected_log_message = Unknown(input_log_message)

        log_message_parsed = InformationLogMessage.parse(input_log_message)
        self.assertEqual(expected_log_message, log_message_parsed)
