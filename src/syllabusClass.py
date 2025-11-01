from sqlDatabase import dbManager

#the syllabus class currently only has one function cause we are only coding the use case that we decided on for now, the rest of the use cases will be code in phase 5
#some of the unused variables are for future use cases

localManager = dbManager("syllabusDB", "syllabusFiles3")
class syllabus:
    #file size limit is 25mb
    fileName = ""
    format = "NULL"
    size = 0
    pages = 0

    #what this does is it gets the name, size, readilbility(determined by parser but parser not coded right now so default is yes), and file path then performs checks and uploads it to the db
    
    def uploadSyllabus(self, filename, fileSize, legible,pdfPath) -> bool:
        fileType = filename.split(".")[-1]
        if filename == "NULL"  or fileSize == "NULL" or legible == "NULL" or pdfPath == "NULL":
            return False

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

