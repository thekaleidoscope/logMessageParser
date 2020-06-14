import unittest

from main.LogMessage.ErrorLogMessage import ErrorLogMessage
from main.LogMessage.InformationLogMessage import InformationLogMessage
from main.LogMessage.WarningLogMessage import WarningLogMessage
from main.MessageType import MessageType
from main.Unknown import Unknown


class LogMessageParsingTest(unittest.TestCase):

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