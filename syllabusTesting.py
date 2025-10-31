import unittest
from syllabusClass import syllabus
syllabusInstance = syllabus()
class TestBase(unittest.TestCase):

    def test_Base(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 12, True, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, True, 'correctly uploaded syllabus')

class TestFile(unittest.TestCase):

    def test_File(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.DOCX", 21, True, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects DOCX')
class TestSize(unittest.TestCase):

    def test_Size(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 31, True, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats too big')
class TestParsing(unittest.TestCase):

    def test_Parsing(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 2, False, "V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats it not parseable')
if __name__ == '__main__':
    unittest.main()