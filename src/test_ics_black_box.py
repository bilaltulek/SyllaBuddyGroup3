import unittest
from ics import ICSConverter

class TestICSBlackBox(unittest.TestCase):

    def test_valid_event(self):
        conv = ICSConverter("Assignment", "2025/11/25", "Homework 8")
        result = conv.to_ics()
        self.assertTrue("BEGIN:VEVENT" in result)
        self.assertTrue("SUMMARY:Assignment: Homework 8" in result)

    def test_invalid_event_type(self):
        conv = ICSConverter("ERROR", "2025/11/25", "Homework 8")
        result = conv.to_ics()
        self.assertEqual(result, "ERROR: Invalid event type.")

    def test_invalid_date_format(self):
        conv = ICSConverter("Assignment", "ERROR", "Homework 8")
        result = conv.to_ics()
        self.assertEqual(result, "ERROR: Invalid date format.")

    def test_invalid_date_values(self):
        conv = ICSConverter("Assignment", "1997/34/65", "Homework 8")
        result = conv.to_ics()
        self.assertTrue(result.startswith("ERROR"))

    def test_invalid_description_length(self):
        conv = ICSConverter("Assignment", "2025/11/25", "Homework Exam Assignment 867839")
        result = conv.to_ics()
        self.assertEqual(result, "ERROR: Invalid description.")

    def test_exceptional_case(self):
        conv = ICSConverter("Assignment", "2025/11/25", None)
        result = conv.to_ics()
        self.assertEqual(result, "ERROR: Invalid description.")
