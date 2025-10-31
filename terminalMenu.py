from sqlDatabase import *
from syllabusClass import *
import os
import tempfile
import subprocess
instance = syllabus()
localManager = dbManager("syllabusDB", "syllabusFiles3")
#instance.uploadSyllabus("example.pdf", 23, True)
while True:
    print("\n choose options\n 1: uploadSyllabus\n 2: edit syllabus name\n 3:delete row\n 4:display all syllabus\n 5:query\n 6:displaypdf\n 7:exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("enter name")
            nameInput = input()
            print("enter value")
            valueInput = input()
            print("enter filepath")
            path = input()
            instance.uploadSyllabus(nameInput, int(valueInput), True, path)
            #localManager.store_pdf(path, 'examplepdf')

        case 2:



                print("enter ID")
                IDInput = input()
                print("enter new name")
                nameInput = input()
                localManager.editUserName(IDInput, nameInput)


                #localManager.editUserValue(IDInput, valueInput)

        case 3:
            print("Enter ID of row to delete")
            IDInput = input()
            localManager.removeRowFromDatabase(IDInput)

        case 4:
            localManager.displayAll()
            #localManager.retrieve_and_open_pdf('examplepdf')
        case 5:
            print("Enter ID of row to get")
            IDInput = input()
            localManager.query(IDInput)

        case 6:
            print("which pdf do you want to open?")
            userPdfOpen = input()
            localManager.retrieve_and_open_pdf(userPdfOpen)
            break
        case 7:
            break