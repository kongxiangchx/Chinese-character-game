import threading 
import time
import queue
import socket
import json
import random
from mysql_op import *

class User:
    def __init__(self,conn):
        self.conn=conn
    def register(self,recv):
        op1=User_op()
        if op1.register(recv['acc'],recv['passwd'],recv['nickname'],recv['sex']):
            data={'result':'success'}
        else:
            data={'result':'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def login(self,recv):
        op1=User_op()
        if op1.login(recv['acc'],recv['passwd']):
            data={'result':'success'}
        else:
            data={'result':'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def poem_ques(self,recv):
        op1=User_op()
        ques_type=random.randint(1,4)
        sen_id=random.randint(0,1503)
        if ques_type==1:
            data=op1.poem_ques1(sen_id)
        elif ques_type==2:
            data=op1.poem_ques2(sen_id)
        elif ques_type==3:
            data=op1.poem_ques3(sen_id)
        else:
            data=op1.poem_ques4(sen_id)
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def poem_result(self,recv):
        op1=User_op()
        data=op1.poem_result(recv['acc'],recv['poem_score'])
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def idiom_ques(self,recv):
        op1=User_op()
        idiom_id=[i for i in range(209)]
        random.shuffle(idiom_id)
        data=op1.idiom_ques(idiom_id[:7])
        #print(idiom_id[:7])
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def idiom_result(self,recv):
        op1=User_op()
        data=op1.idiom_result(recv['acc'],recv['idiom_score'])
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def poem_rank(self):
        op1=User_op()
        data=op1.poem_rank()
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def idiom_rank(self):
        op1=User_op()
        data=op1.idiom_rank()
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def view_info(self,recv):
        op1=User_op()
        data=op1.view_info(recv['acc'])
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
    def update_info(self,recv):
        op1=User_op()
        if op1.update_info(recv['acc'],recv['passwd'],recv['nickname'],recv['sex']):
            data={'result':'success'}
        else:
            data={'result':'fail'}
        self.conn.send(json.dumps(data).encode())
        self.conn.close()
if __name__ == "__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',5000))
    s.listen(20)
    while True:
        conn,addr=s.accept()
        recv=json.loads(conn.recv(1024).decode())
        #print(json.dumps(recv))
        user1=User(conn)
        if recv['type']=='register':
            user1.register(recv)
        elif recv['type']=='login':
            user1.login(recv)
        elif recv['type']=='poem_ques':
            user1.poem_ques(recv)
        elif recv['type']=='poem_result':
            user1.poem_result(recv)
        elif recv['type']=='idiom_ques':
            user1.idiom_ques(recv)
        elif recv['type']=='idiom_result':
            user1.idiom_result(recv)
        elif recv['type']=='poem_rank':
            user1.poem_rank()
        elif recv['type']=='idiom_rank':
            user1.idiom_rank()
        elif recv['type']=='view_info':
            user1.view_info(recv)
        elif recv['type']=='update_info':
            user1.update_info(recv)
        
