import csv


# def writeUnsuccessfullySentMail(row, logFilePath):
#     with open(
#         logFilePath, mode="a", newline=""
#     ) as csvFile:  # opening with newline='' to avoid printing extra lines because the csv.writer
#         # module directly controls line endings and writes \r\n into the file directly.
#         writer = csv.writer(csvFile, delimiter=",")
#         fields = [
#             "Timestamp",
#             "Email Address",
#             "NU-ID",
#             "FULL NAME",
#             "PHONE NUMBER",
#             "SELECT ON-DAY TEAM",
#             "SELECT OFF-DAY TEAM",
#             "SELECT POSITION",
#             "Past EXPERIENCE",
#         ]
#         if (
#             writeUnsuccessfullySentMail.counter == 0
#         ):  # if log file is empty, write the column names first
#             writer.writerow(fields)
#             writeUnsuccessfullySentMail.counter = 1

#         writer.writerow(row)
#     csvFile.close()


# writeUnsuccessfullySentMail.counter = (
#     0  # to check whether the file is empty or not, 0 = empty
# )


def writeRecordsToCsv(records, logFilePath):

    with open(logFilePath, mode="w", newline="") as csvFile:
        writer = csv.writer(csvFile, delimiter=",")

        # Write the fields, which are the keys of the dictionary
        fields = list(records.keys())
        writer.writerow(fields)

        totalRecords = len(records[fields[0]])

        for i in range(0, totalRecords):
            row = []
            for field in fields:
                row.append(records[field][i])

            writer.writerow(row)

    csvFile.close()


def readRecordsFromCsv(logFilePath):

    records = {}

    with open(logFilePath, mode="r", newline="") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        lineCount = 0
        fields = []

        for row in csvReader:

            # If first row, initialize the dictionary keys as field values with arrays
            if lineCount == 0:
                fields = row
                for field in fields:
                    records[field] = []

            # For the next rows, write each row's field data to the respective array
            else:

                fieldIndex = 0
                for field in fields:
                    records[field].append(row[fieldIndex])
                    fieldIndex += 1

            lineCount += 1

    return records
