from sendLetterAttachedMail import sendPdfAttachmentMail
from createLetter import getLetter
from csvWriter import writeRecordsToCsv, readRecordsFromCsv
from emailHtmlContent import getHtmlContent

# someway to add group links
groupLink= "www.google.com"

unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"

unsentRecords = readRecordsFromCsv(unsentMailsCsvPath)
sentRecords = readRecordsFromCsv(sentMailsCsvPath)

totalRecords= len(unsentRecords)
unsentLength = totalRecords
i = 0

while i < unsentLength:
    memberData = unsentRecords[i]

    letter = getLetter(
        memberData["FULL NAME"],
        memberData["SELECT ON-DAY TEAM"],
        memberData["SELECT POSITION"],
    )
    
    htmlContent= getHtmlContent(groupLink)

    # sort the data according to if the mail was sent or not
    if sendPdfAttachmentMail(memberData["Email Address"], letter,htmlContent) == True:
        unsentRecords.remove(memberData)
        sentRecords.append(memberData)
        i -= 1
        unsentLength -= 1

    i += 1


if writeRecordsToCsv(sentRecords, sentMailsCsvPath):
    print("Sent records written to file")
else:
    print("No sent records")

if writeRecordsToCsv(unsentRecords, unsentMailsCsvPath):
    print("Unsent records written to file")
else:
    print("No unsent records")


print("=======================================================")
print(f"Total records: {totalRecords}")
print(f"Successful mails: {totalRecords - unsentLength}")
print(f"Unsuccessful mails: {unsentLength}")