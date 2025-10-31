import unittest
import os
from export import Export

class TestExtractorConcrete(unittest.TestCase):
    
    def setUp(self):
        self.extractor = Export()
        self.test_output = "test_export.txt"
    
    def tearDown(self):
        if os.path.exists(self.test_output):
            os.remove(self.test_output)
    
    def test_getEventCount_returns_correct_number(self):
        self.assertEqual(self.extractor.getEventCount(), 0)
        
        events = [
            {"date": "Jan 12", "title": "Event 1"},
            {"date": "Jan 19", "title": "Event 2"},
            {"date": "Feb 02", "title": "Event 3"}
        ]
        self.extractor.loadEvents(events)
        
        self.assertEqual(self.extractor.getEventCount(), 3)
        
    def test_exportPath_is_set_after_successful_export(self):
        events = [{"date": "Jan 12", "title": "Test"}]
        self.extractor.loadEvents(events)
        
        self.assertEqual(self.extractor.exportPath, "")
        
        self.extractor.exportEvents(self.test_output)
        self.assertEqual(self.extractor.exportPath, self.test_output)
    
    def test_export_file_format(self):
        events = [
            {"date": "Jan 12", "title": "First Event"},
            {"date": "Feb 02", "title": "Second Event"}
        ]
        self.extractor.loadEvents(events)
        self.extractor.exportEvents(self.test_output)
        
        with open(self.test_output, "r") as f:
            lines = f.readlines()
        
        self.assertIn("SYLLABUS EVENTS", lines[0])
        self.assertIn("=" * 50, lines[1])
        
        content = "".join(lines)
        self.assertIn("Date: Jan 12", content)
        self.assertIn("Title: First Event", content)
        self.assertIn("Date: Feb 02", content)
        self.assertIn("Title: Second Event", content)
        self.assertIn("-" * 50, content)


if __name__ == "__main__":
    unittest.main()