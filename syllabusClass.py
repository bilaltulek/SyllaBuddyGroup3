from sqlDatabase import dbManager
localManager = dbManager("syllabusDB", "syllabusFiles3")
class syllabus:
    #file size limit is 25mb
    fileName = ""
    format = "NULL"
    size = 0
    pages = 0
    #def __init__(self, format, size, pages):
    #    self.format = format
    #    self.size = size
    #    self.pages = pages
    def uploadSyllabus(self, filename, fileSize, legible,pdfPath) -> bool:
        fileType = filename.split(".")[-1]

        if fileType == "pdf" and fileSize <= 25 and legible:
            self.fileName = filename
            localManager.addRowToDatabase(self.fileName, fileSize, pdfPath)
            print("uploaded successfully ")
            return True

        elif fileType != "PDF":
            print("file type not supported")
            return False
        elif fileSize >= 25:
            print("file size too big")
            return False
        elif not legible:
            print("file could not be parsed")
            return False

    def getFormat(self):
        return self.format
    def getSize(self):
        return self.size
    def getPages(self):
        return self.pages