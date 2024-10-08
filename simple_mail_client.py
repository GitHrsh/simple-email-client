import smtplib
from email.message import EmailMessage
from email import encoders

sender_email="" #sender's email address here
sender_pass="" #password here

rec_email="" #receiver's address
cc_emails=[]
bcc_emails=[]

message=EmailMessage()
message['From'] = sender_email
message['To'] = rec_email
message['Cc'] = ', '.join(cc_emails)
message['Subject'] = "Test mail"
message.set_content("Attachment trial run")

with open("",'rb') as fp:    #path to attachment
        attach_data = fp.read()
        message.add_attachment(attach_data, maintype='image',subtype="jpg") #can omit subtype
recipients=[rec_email]+cc_emails+bcc_emails
server=smtplib.SMTP("",25)   #enter email service provider server
server.starttls()
server.login(sender_email,sender_pass)
server.sendmail(sender_email,rec_email,message.as_string())
print("sent")
server.quit()

