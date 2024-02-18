import datetime
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

# TODO Implement correct way of fetching the sender's password
# Temporary method of getting the sender's password
passFile = open("/home/c41f0n/Desktop/pass.txt", "r")
password = passFile.readlines()[0].lstrip().rstrip()


def sendPdfAttachmentMail(emailAddress, attachment):

    # TODO Set global variable for sender
    sender = "k230703@nu.edu.pk"

    senderPassword = password
    recieverMail = emailAddress
    msg = EmailMessage()
    msg["Subject"] = "Test Email With Attachment"
    msg["From"] = sender
    msg["To"] = recieverMail

    # Attach the pdf
    with open(attachment, "rb") as content_file:
        content = content_file.read()
        msg.add_attachment(
            content, maintype="application", subtype="pdf", filename=attachment
        )

    # Enter body conteny here....
    emailBody = MIMEText("hee hee", "plain")

    msg.attach(emailBody)

    # Sending Messages...
    print(f"[+] Sending attachment mail to {recieverMail}")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:

            # Raised a test exception to test exception handling
            # raise smtplib.SMTPResponseException(12, "nahi hora bhai")

            smtp.starttls()
            smtp.login(sender, senderPassword)
            smtp.send_message(msg)

            print(f"[+] Successfully sent mail to {recieverMail}")

            # A last minute check to see if the sent mail is correct
            if recieverMail == sender:
                check = input("All set? (y/n):")

                if check.lower() != "y":
                    return 0

        except smtplib.SMTPResponseException as e:
            print(f"\n[-] Could not send mail to {recieverMail}: Error: {e.smtp_error}")

            # Logging the mail as not sent with error message and timestamp
            unsuccessfulMailLog = open("notSentToEmails.log", "a")
            unsuccessfulMailLog.write(
                f"{recieverMail} | Error: {e.smtp_error} | {datetime.datetime.now()}\n"
            )
            unsuccessfulMailLog.close()


# sendPdfAttachmentMail("k230703@nu.edu.pk", "test.pdf")
