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

for memberData in unsentRecords:

    letter = getLetter(
        memberData["FULL NAME"],
        memberData["SELECT ON-DAY TEAM"],
        memberData["SELECT POSITION"],
    )
    # write to log file incase of unsuccesful email
    if sendPdfAttachmentMail(memberData["Email Address"], letter) == False:
        pass
    else:
        unsentRecords.remove(memberData)
        sentRecords.append(memberData)


writeRecordsToCsv(unsentRecords, unsentMailsCsvPath)
writeRecordsToCsv(sentRecords, sentMailsCsvPath)

# # Creating history folder if doesnt exist
# if not os.path.exists(os.getcwd() + "/" + historyFolderName):
#     os.makedirs(os.getcwd() + "/" + historyFolderName, exist_ok=True)

# # Copying the old csv data to history with timestamp
# shutil.copy2(
#     unsentMailsCsvPath,
#     f"{os.curdir}/{historyFolderName}/",
# )

# now = datetime.datetime.now()
# os.rename(
#     f"{os.curdir}/{historyFolderName}/{os.path.basename(unsentMailsCsvPath)}",
#     f"{os.curdir}/{historyFolderName}/{os.path.basename(unsentMailsCsvPath)[:-4]}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.csv",
# )

# # renaming last unsent mails to main csv
# os.remove(unsentMailsCsvPath)

# # check if unsentMails file exsist then rename it to csv file
# if os.path.exists(sentMailsCsvPath):
#     os.rename(sentMailsCsvPath, unsentMailsCsvPath)

# print("=======================================================")
# print(f"Total records: {lineCount}")
# print(f"Successful mails: {lineCount- unsuccesfulCount}")
# print(f"Unsuccessful mails: {unsuccesfulCount}")
