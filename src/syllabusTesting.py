import unittest
from syllabusClass import syllabus
syllabusInstance = syllabus()
class TestBase(unittest.TestCase):

    def test_Base(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 12, True, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, True, 'correctly uploaded syllabus')

class TestFile(unittest.TestCase):

    def test_File(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.DOCX", 21, True, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects DOCX')
class TestSize(unittest.TestCase):

    def test_Size(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 31, True, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats too big')
class TestParsing(unittest.TestCase):

    def test_Parsing(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 2, False, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats it not parseable')
#dont know how these would get NULL values but my homework 7 was deducted for not checking null so im going to be cautious
class TestNullName(unittest.TestCase):

    def test_nName(self):
        testCase = syllabusInstance.uploadSyllabus("NULL", 2, False, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'Correctly rejects file thats it not parseable')
class TestNullSize(unittest.TestCase):

    def test_nSize(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", "NULL", True, "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'correctly uploaded syllabus')
class TestNullLegible(unittest.TestCase):

    def test_Base(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 12, "NULL", "src/V01_Students_F25 - V01_Students_F25.pdf")
        self.assertEqual(testCase, False, 'correctly uploaded syllabus')
class TestNullPath(unittest.TestCase):

    def test_Base(self):
        testCase = syllabusInstance.uploadSyllabus("syllabus.pdf", 12, True, "NULL")
        self.assertEqual(testCase, False, 'correctly uploaded syllabus')
