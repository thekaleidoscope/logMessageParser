import unittest
from pathlib import Path

from main import LogFileParser
from main.domain.LogMessage.LogMessage import LogMessage
from main.domain.Unknown import Unknown


class LogFileParserTest(unittest.TestCase):

    def test_shouldBeAbleToParseLogFile(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../sample.log").resolve()

        log_messages = LogFileParser.parse(file_path)
        self.assertTrue(log_messages.__len__() > 0)
        for log_message in log_messages:
            self.assertFalse(isinstance(log_message, Unknown))
            self.assertTrue(isinstance(log_message, LogMessage))
