import smtplib
from Tkinter import *
from tkFileDialog import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
#fromaddr,toaddr,subject from diff textfields
fromaddr =""
password = ""
toaddr =""
subject =""
 
msg = MIMEMultipart()

def attach_text():
	"""
	Function to add text from text box
	
	"""
	body = text.get("1.0",'end-1c')
	msg.attach(MIMEText(body, 'plain'))
	
def attach_file(file_name):
	"""
	Function to include files,images,audio and video
	
	"""
	attachment = open(file_name, "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
	msg.attach(part)

def attach_html():
	"""
	Function to attach html
	
	"""
	html_file=html.get("1.0",'end-1c')
	msg.attach(MIMEText(html_file,'html'))
 
def attach_link(link,name):
	html = """\
	<html>
	<head></head>
	<body>
		<a href=%s>%s</a>
	</body>
	</html>
	"""%(link,name)
	msg.attach(MIMEText(html,'html'))

def select_file():
	"""
	Function to select a file
	
	"""
	file_path=askopenfilename()
	if(file_path):
		attach_file(file_path)
	
def send():

	fromaddr=fromaddress.get()
	toaddr=toaddress.get()
	password=getpassword.get()
	subject=getsub.get()
	
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('trishalainusa@gmail.com', 'inuyashausuisyaron')
	attach_text()
	attach_html()
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

top=Tk()
top.wm_title("Querry Mail")
From = StringVar()
label = Message( top, textvariable=From , width=100,justify=LEFT)
From.set("From: ")
label.grid(row=1,column=1,pady=20,sticky=E)

Password=StringVar()
label = Message( top, textvariable=Password , width=100)
Password.set("Password: ")
label.grid(row=2,column=1,pady=10,sticky=E)

To=StringVar()
label = Message( top, textvariable=To , width=100)
To.set("To: ")
label.grid(row=3,column=1,pady=10,sticky=E)

sub=StringVar()
label = Message( top, textvariable=sub , width=100)
sub.set("Subject: ")
label.grid(row=4,column=1,pady=10,sticky=E)

mssg=StringVar()
label = Message( top, textvariable=mssg , width=100)
mssg.set("Message: ")
label.grid(row=5,column=1,pady=10,sticky=E)

html=StringVar()
label = Message( top, textvariable=html , width=100)
html.set("HTML: ")
label.grid(row=6,column=1,pady=10,sticky=E)

fromaddress=StringVar()
getpassword=StringVar()
toaddress=StringVar()
getsub=StringVar()

E1 = Entry(top, textvariable=fromaddress,bd =5,width=100)
E1.grid(row=1,column=2,pady=10)

E2 = Entry(top, show="*",textvariable=getpassword,bd =5,width=100)
E2.grid(row=2,column=2,pady=10)

E3 = Entry(top, textvariable=toaddress,bd =5,width=100)
E3.grid(row=3,column=2,pady=10)

E4 = Entry(top, textvariable=getsub,bd =5,width=100)
E4.grid(row=4,column=2,pady=10)

text=Text(top,height=10)
text.grid(row=5,column=2,pady=10,padx=10)

html=Text(top,height=3)
html.grid(row=6,column=2,pady=10,padx=10)

B1 = Button(top, text ="Attach file", command = select_file)
B1.grid(row=7,column=1,pady=20,padx=5)
#B2 = Button(top, text ="Attach link", command = select_file)
#B2.grid(row=7,column=2,pady=20)
B3 = Button(top, text ="Send", command = send)
B3.grid(row=7,column=2,pady=20)

#send(msg,fromaddr,toaddr,password)
top.mainloop()
