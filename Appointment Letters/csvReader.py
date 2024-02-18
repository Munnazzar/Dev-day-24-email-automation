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


path = 'D:\\automation\\email\\Dev-day-24-email-automation\\Appointment Letters\\csvTest.csv'  # enter full file path, use \\ to avoid escape sequences
logFile = 'D:\\automation\\email\\Dev-day-24-email-automation\\Appointment Letters\\log.csv'     # log file path

def readDataFromCSVfile(filePath, logFilePath):
    with open(filePath, mode ='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        for record in csv_reader:                      # here 'record' is the lines??? or the individual member data
            if(line_count != 0):                       # line_count = 0 would be the column names, so we skip those (unless needed)
                memberEmail = record[1]
                fullName = record[3]
                memberOnDayTeam = record[5]
                memberOffDayTeam = record[6]
                memberPosition = record[7]
            
                #replace this print statement with the html to letter code
                print("send mail to "+ memberEmail + " name = " + fullName + " team = "+ memberOnDayTeam + " and "+ memberOffDayTeam + " position = "+ memberPosition)
            line_count+=1
    
# calling the function here        
readDataFromCSVfile(path, logFile)