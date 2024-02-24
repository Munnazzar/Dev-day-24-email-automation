from sendLetterAttachedMail import sendPdfAttachmentMail
from createLetter import getLetter
from csvWriter import writeRecordsToCsv, readRecordsFromCsv, readRecordsFromExcel
from emailHtmlContent import getHtmlContent

print("================================================")
print("         DEV DAY MEMBER MAILS MANAGER")
print("================================================\n")

# someway to add group links
groupLink = "www.google.com"

unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"

unsentRecords = readRecordsFromCsv(unsentMailsCsvPath)
sentRecords = readRecordsFromCsv(sentMailsCsvPath)

totalRecords = len(unsentRecords)
unsentLength = totalRecords

try:

    i = 0

    while i < unsentLength:
        memberData = unsentRecords[i]

        letter = getLetter(
            memberData["FULL NAME"],
            memberData["SELECT ON-DAY TEAM"],
            memberData["SELECT POSITION"],
        )

        htmlContent = getHtmlContent(groupLink)

        # sort the data according to if the mail was sent or not
        if (
            sendPdfAttachmentMail(memberData["Email Address"], letter, htmlContent)
            == True
        ):
            unsentRecords.remove(memberData)
            sentRecords.append(memberData)
            i -= 1
            unsentLength -= 1

        i += 1


except Exception as ex:
    print("[!] AN ERROR OCCOURED:-")
    print(ex)

finally:
    print("[+] Writing data to files before exiting...")

    if writeRecordsToCsv(sentRecords, sentMailsCsvPath):
        print("   [+] Sent records written to file")
    else:
        print("   [+] No sent records to write.")

    if writeRecordsToCsv(unsentRecords, unsentMailsCsvPath):
       print("   [+] Unsent records written to file")
    else:
        print("   [+] No unsent records to write.")


print("\n\n======== OPERATION SUMMARY ========")
print(f"\nTotal records to send: {totalRecords}")
print(f"\nSuccessful mails: {totalRecords - unsentLength}")
print(f"--> Saved in: {sentMailsCsvPath}")

print(f"\nUnsuccessful mails: {unsentLength}")
print(f"--> Saved in: {unsentMailsCsvPath}")
