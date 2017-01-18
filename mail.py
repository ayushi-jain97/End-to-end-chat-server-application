import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
#from email import encoders

def mail_history(email_id,history):
    text=''
    fromaddr="ayushi.jain.cse15@itbhu.ac.in"
    toaddr=str(email_id)
    msg=MIMEMultipart()
    msg['Subject']='Test'
    msg['From']=fromaddr
    msg['To']=toaddr
    print history
    msg.attach(MIMEText(str(history),'plain'))
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(fromaddr,'seemaamit')
    mail.sendmail(fromaddr,toaddr,str(msg))
    mail.close()

#mail_history("ayushi.jain.cse15@itbhu.ac.in",['fdjkfj','fejwlik'])

