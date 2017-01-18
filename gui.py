from Tkinter import *
from threading import Thread
import server,client
root=Tk()

def start_server():
    ip=text.get('1.0','end-1c')
    th=Thread(target=server.start_server_window,args=(ip,))
    th.start()
    print "Server started on "+ip
    root.destroy()

def start_client():
    ip=ct.get('1.0','end-1c')
    th2=Thread(target=client.t,args=(str(ip),))
    th2.start()
    print "client connected to "+ip
    root.destroy()
    
serve=Label(root,text="Server")
text=Text(root,height=1,width=30)
sb=Button(root,text="Start",command=start_server)

clien=Label(root,text="Client")
ct=Text(root,height=1,width=30)
cb=Button(root,text="Start",command=start_client)

serve.grid(row=0,column=0)
text.grid(row=0,column=1)
sb.grid(row=1,columnspan=2)

clien.grid(row=2,column=0)
ct.grid(row=2,column=1)
cb.grid(row=3,columnspan=2)


root.mainloop()
