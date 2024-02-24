from sendLetterAttachedMail import sendPdfAttachmentMail
from createLetter import getLetter
from csvWriter import writeRecordsToCsv, readRecordsFromCsv

# enter full file path, use \\ to avoid escape sequences
unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"

unsentRecords = readRecordsFromCsv(unsentMailsCsvPath)
sentRecords = readRecordsFromCsv(sentMailsCsvPath)

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
