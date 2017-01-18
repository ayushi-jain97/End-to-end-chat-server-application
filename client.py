import socket
from threading import Thread
from Tkinter import *

M=""

def read(inp,s,chat):
    global M
    x=inp.get('1.0','end-1c')
    M=M+"You: "+x+'\n'
    inp.delete('1.0',END)
    chat.config(text=M)
    s.send(x)
    
def write(s,chat):
    global M
    while 1:
        color='black'
        x=s.recv(4096)
        M+=x+'\n'
        chat.config(text=M,fg=color)
def t(ip):
    s=socket.socket()
    s.connect((str(ip),10003))
    x=Thread(target=start_client_window,args=(s,ip,))
    x.start()
    
def start_client_window(s,ip):
    
    global M
    M="Connected to "+str(ip)+'\nPlease enter your name \n'
    root=Tk()
    chat=Label(root,text=M,fg="black")
    inp=Text(root,height=1,width=50)
    send=Button(root,text="send",command=lambda: read(inp,s,chat))
    
    mailid=Text(root,height=1,width=20)
    email=Button(root,text="Email",command=lambda: mail_history(mailid))
    
    chat.grid(row=0)
    inp.grid(row=1,column=0)
    send.grid(row=1,column=1)
    mailid.grid(row=2,column=0)
    email.grid(row=2,column=1)
    y=Thread(target=write,args=(s,chat,))
    y.start()
    root.mainloop()
    

def mail_history(mailid):
    
    email_id=mailid.get('1.0','end-1c')
    import server
    history=server.history
    server.print_history()
    #server.send_mail(email_id)


