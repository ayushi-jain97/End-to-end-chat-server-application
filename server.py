import socket
import select
from Tkinter import *

history=[]

def print_history():
        print history


def send_to_all(message,sock,s_l,server):
        for s in s_l:
                if s is not server and s is not sock:
                        s.send(str(message))

def start_server_window(ip):
    root=Tk()
    M="Server running on "+ip+"\n"
    chat=Label(root,text=M)
    chat.pack()
    start_server_thread(root,ip,M,chat)
    root.mainloop()

def send_history(client):
        print history
        client.send("Discussion so far..\n")
        for j in history:
                client.send(str(j)+'\n')


def start_server_thread(root,ip,M,chat):
        server=socket.socket()
        server.bind((str(ip),10003))
        server.listen(5)
        s_l=[]
        s_l.append(server)
        c={}

        
        while 1:
        
                r,w,z=select.select(s_l,[],[],0)
                for i in r:
                    if i==server:
                        try:
                            client,addr=server.accept()
                            name=client.recv(4096)
                            c[name]=client
                            msg="%s connected \n"%name
                            print msg
                            M+=msg
                            send_history(client)
                            #client.send(str(history))
                            s_l.append(client)
                            #print M
                            chat.config(text=M)
                            send_to_all(msg,client,s_l,server)
                            history.append(msg)
                            
                        except:
                            break
                    else:
                        try:
                            m=i.recv(4096)
                            print m
                            if len(m):
                                    for j in c.keys():
                                        if c[j]==i:
                                            break
                                    t="message from %s: %s"%(j,m)
                                    send_to_all(t,i,s_l,server)
                                    history.append(t)
                        except:
                            for j in c.keys():
                                if c[j]==i:
                                    break;
                            m="%s disconnected \n"%j
                            M+=m
                            chat.config(text=M)
                            send_to_all(m,i,s_l,server)
                            history.append(m)
                            del c[j]
                            s_l.remove(i)
            

