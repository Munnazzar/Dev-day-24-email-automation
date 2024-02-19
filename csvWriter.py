import csv

def writeUnsuccessfullySentMail(row, logFilePath):                                
    with open(logFilePath, mode = 'a', newline='') as csvFile:                         # opening with newline='' to avoid printing extra lines because the csv.writer 
                                                                                       # module directly controls line endings and writes \r\n into the file directly.
        writer = csv.writer(csvFile, delimiter=',') 
        fields = ['Timestamp','Email Address','NU-ID','FULL NAME','PHONE NUMBER','SELECT ON-DAY TEAM','SELECT OFF-DAY TEAM','SELECT POSITION','Past EXPERIENCE']
        if(writeUnsuccessfullySentMail.counter == 0):                               # if log file is empty, write the column names first
            writer.writerow(fields)
            writeUnsuccessfullySentMail.counter = 1
            
        writer.writerow(row)

writeUnsuccessfullySentMail.counter = 0                                             # to check whether the file is empty or not, 0 = empty