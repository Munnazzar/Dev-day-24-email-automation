import os
import csv
import datetime
from sendLetterAttachedMail import sendPdfAttachmentMail
from createLetter import getLetter
from csvWriter import writeRecordsToCsv, readRecordsFromCsv
import shutil

# enter full file path, use \\ to avoid escape sequences
unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"

unsentRecords = readRecordsFromCsv(unsentMailsCsvPath)
sentRecords = readRecordsFromCsv(sentMailsCsvPath)

print("Unsent Records:")
for member in unsentRecords:
    print(member["Email Address"])

print("Sent Records:")
for member in sentRecords:
    print(member["Email Address"])

unsentLength = len(unsentRecords)
i = 0

while i < unsentLength:
    memberData = unsentRecords[i]

    letter = getLetter(
        memberData["FULL NAME"],
        memberData["SELECT ON-DAY TEAM"],
        memberData["SELECT POSITION"],
    )
    # sort the data according to if the mail was sent or not
    if sendPdfAttachmentMail(memberData["Email Address"], letter) == False:
        pass
    else:
        unsentRecords.remove(memberData)
        sentRecords.append(memberData)
        i -= 1
        unsentLength -= 1

    i += 1


writeRecordsToCsv(unsentRecords, unsentMailsCsvPath)
writeRecordsToCsv(sentRecords, sentMailsCsvPath)
