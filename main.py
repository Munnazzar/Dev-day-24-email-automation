import os
import csv
import datetime
from sendLetterAttachedMail import sendPdfAttachmentMail
from createLetter import getLetter
from csvWriter import writeUnsuccessfullySentMail
import shutil

csvFilePath = "csvTest.csv"  # enter full file path, use \\ to avoid escape sequences
unsentRecordsFilePath = "unsentMails.csv"  # log file path
historyFolderName = "csvFile_history"  # history folder name

with open(csvFilePath, mode="r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    lineCount = -1
    unsuccesfulCount = 0
    memberData = {}
    for (
        record
    ) in csv_reader:  # here 'record' is the lines??? or the individual member data
        if (
            lineCount == -1
        ):  # line_count = -1 would be the column names, so we skip those (unless needed)
            lineCount += 1
            continue

        memberData["email"] = record[1]
        memberData["fullName"] = record[3]
        memberData["OnDayTeam"] = record[5]
        memberData["OffDayTeam"] = record[6]
        memberData["Position"] = record[7]

        letter = getLetter(
            memberData["fullName"], memberData["OnDayTeam"], memberData["Position"]
        )
        # write to log file incase of unsuccesful email
        if sendPdfAttachmentMail(memberData["email"], letter) == False:
            unsuccesfulCount += 1
            writeUnsuccessfullySentMail(record, unsentRecordsFilePath)

        lineCount += 1
    file.close()

# Creating history folder if doesnt exist
if not os.path.exists(os.getcwd() + "/" + historyFolderName):
    os.makedirs(os.getcwd() + "/" + historyFolderName, exist_ok=True)

# Copying the old csv data to history with timestamp
shutil.copy2(
    csvFilePath,
    f"{os.curdir}/{historyFolderName}/",
)

now = datetime.datetime.now()
os.rename(
    f"{os.curdir}/{historyFolderName}/{os.path.basename(csvFilePath)}",
    f"{os.curdir}/{historyFolderName}/{os.path.basename(csvFilePath)[:-4]}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.csv",
)

# renaming last unsent mails to main csv
os.remove(csvFilePath)

# check if unsentMails file exsist then rename it to csv file
if os.path.exists(unsentRecordsFilePath):
    os.rename(unsentRecordsFilePath, csvFilePath)

print("=======================================================")
print(f"Total records: {lineCount}")
print(f"Successful mails: {lineCount- unsuccesfulCount}")
print(f"Unsuccessful mails: {unsuccesfulCount}")
