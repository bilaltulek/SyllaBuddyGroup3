import unittest
import os
from export import Export

class TestExtractorBlackBox(unittest.TestCase):
    """Black box testing based on the test case table"""
    
    def setUp(self):
        """Setup before each test"""
        self.extractor = Export()
        self.test_output = "test_export.txt"
    
    def tearDown(self):
        """Cleanup after each test"""
        if os.path.exists(self.test_output):
            os.remove(self.test_output)
    
    def test_case_1_successful_export_with_events(self):
        """Test Case 1: Events loaded (5), export should be successful"""
        # Setup: Load 5 events
        events = [
            {"date": "Jan 12", "title": "Introduction to Course"},
            {"date": "Jan 19", "title": "Chapter 1 Review"},
            {"date": "Feb 02", "title": "Midterm Exam"},
            {"date": "Mar 15", "title": "Project Due"},
            {"date": "Apr 20", "title": "Final Exam"}
        ]
        self.extractor.loadEvents(events)
        
        # Action: Export events
        result = self.extractor.exportEvents(self.test_output)
        
        # Assert: Export successful and file exists
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_output))
        self.assertEqual(self.extractor.getEventCount(), 5)
        
        # Verify file contents
        with open(self.test_output, "r") as f:
            content = f.read()
            self.assertIn("SYLLABUS EVENTS", content)
            self.assertIn("Jan 12", content)
            self.assertIn("Introduction to Course", content)
    
    def test_case_2_no_events_loaded(self):
        """Test Case 2: No events loaded (0), export should fail with message"""
        # Setup: Don't load any events
        
        # Action: Try to export
        result = self.extractor.exportEvents(self.test_output)
        
        # Assert: Export fails and error message is set
        self.assertFalse(result)
        self.assertEqual(self.extractor.errorMessage, "No events available for export.")
        self.assertFalse(os.path.exists(self.test_output))
    
    def test_case_3_empty_export_path(self):
        """Test Case 3: Events loaded but empty export path"""
        # Setup: Load events
        events = [
            {"date": "Jan 12", "title": "Introduction to Course"},
            {"date": "Feb 02", "title": "Midterm Exam"}
        ]
        self.extractor.loadEvents(events)
        
        # Action: Try to export with empty path
        result = self.extractor.exportEvents("")
        
        # Assert: Export fails with error message
        self.assertFalse(result)
        self.assertIn("Export path cannot be empty", self.extractor.errorMessage)
    
    def test_case_4_invalid_export_path(self):
        """Test Case 4: Events loaded but invalid export path (simulates network/IO error)"""
        # Setup: Load events
        events = [
            {"date": "Jan 12", "title": "Introduction to Course"},
            {"date": "Feb 02", "title": "Midterm Exam"}
        ]
        self.extractor.loadEvents(events)
        
        # Action: Try to export to invalid path
        invalid_path = "/invalid/path/that/does/not/exist/output.txt"
        result = self.extractor.exportEvents(invalid_path)
        
        # Assert: Export fails with error message
        self.assertFalse(result)
        self.assertIn("Export failed", self.extractor.errorMessage)
    
    def test_load_invalid_events_type(self):
        """Test that loadEvents raises error for non-list input"""
        with self.assertRaises(ValueError):
            self.extractor.loadEvents("not a list")
    
    def test_multiple_exports(self):
        """Test that multiple exports work correctly"""
        events = [{"date": "Jan 12", "title": "Test Event"}]
        self.extractor.loadEvents(events)
        
        # First export
        result1 = self.extractor.exportEvents(self.test_output)
        self.assertTrue(result1)
        
        # Second export to same file
        result2 = self.extractor.exportEvents(self.test_output)
        self.assertTrue(result2)
        
        # File should still exist and be valid
        self.assertTrue(os.path.exists(self.test_output))


if __name__ == "__main__":
    unittest.main()