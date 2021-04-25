import sys
import random
import threading
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from window.register_window import *
from window.login_window import *
from window.user_main import *
from window.poem_game import *
from window.idiom_game import *
from window.game_rule import *
from window.game_rank import *
from window.per_info import *
from send_data import *

class Register(QMainWindow, Ui_register_window):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.reg_bt.clicked.connect(self.click1)
        self.tologin.clicked.connect(self.click2)
    def click1(self):
        acc=self.username.text()
        pass1=self.pass1.text()
        pass2=self.pass2.text()
        nickname=self.nickname.text()
        sex=self.sex.currentText()
        if acc=='' or pass1=='' or nickname=='':
            QMessageBox.information(self,"注册","个人信息不能为空",QMessageBox.Yes)
            return
        if acc!=''.join(acc.split()) or pass1!=''.join(pass1.split()) or nickname!=''.join(nickname.split()):
            QMessageBox.information(self,"注册","个人信息不能包含空白字符",QMessageBox.Yes)
            return
        if pass1!=pass2:
            QMessageBox.information(self,"注册","两次输入的密码必须相同",QMessageBox.Yes)
            return
        data={'type':'register','acc':acc,'passwd':pass1,'nickname':nickname,'sex':sex}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"注册","注册成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"注册","注册失败",QMessageBox.Yes)
    def click2(self):
        self.hide()
        myWin2.show()
        
class Login(QMainWindow, Ui_login_window):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.login_bt.clicked.connect(self.click1)
        self.toreg.clicked.connect(self.click2)
    def click1(self):
        global user
        acc=self.username.text()
        passwd=self.password.text()
        if acc=='' or passwd=='':
            QMessageBox.information(self,"登录","账号或密码不能为空",QMessageBox.Yes)
            return
        data={'type':'login','acc':acc,'passwd':passwd}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            user=acc
            QMessageBox.information(self,"登录","登录成功",QMessageBox.Yes)
            self.hide()
            myWin3.show()
        else:
            QMessageBox.information(self,"登录","登录失败",QMessageBox.Yes)
    def click2(self):
        self.hide()
        myWin1.show()

class MainWin(QMainWindow,Ui_user_main):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)
        self.poem_bt.clicked.connect(self.click1)
        self.idiom_bt.clicked.connect(self.click2)
        self.rule_bt.clicked.connect(self.click3)
        self.rank_bt.clicked.connect(self.click4)
        self.info_bt.clicked.connect(self.click5)
    def click1(self):
        myWin4.first_load()
        myWin4.show()
    def click2(self):
        myWin5.load()
        myWin5.show()
    def click3(self):
        myWin6.show()
    def click4(self):
        myWin7.click2()
        myWin7.show()
    def click5(self):
        myWin8.load()
        myWin8.show()
    
class PoemGame(QMainWindow,Ui_poem_game):
    def __init__(self,parent=None):
        super(PoemGame,self).__init__(parent)
        self.setupUi(self)
        self.ok_bt.clicked.connect(self.click1)
        self.tip_bt.clicked.connect(self.click2)
        self.exit_bt.clicked.connect(self.click3)
    def send_result(self):
        data={'type':'poem_result','acc':user,'poem_score':self.ans_num.intValue()}
        s=Send_data()
        recv=s.message(data)
        s.close()
        QMessageBox.information(self,"答题结束","共作答"+str(self.ans_num.intValue())+'道题，打败全国'+recv['rate']+'的用户',QMessageBox.Yes)
        self.hide()
    def click1(self):
        flag=0
        if self.option1.isChecked():
            if self.option1.text()==self.ans:
                flag=1
            else:
                flag=2
        elif self.option2.isChecked():
            if self.option2.text()==self.ans:
                flag=1
            else:
                flag=2
        elif self.option3.isChecked():
            if self.option3.text()==self.ans:
                flag=1
            else:
                flag=2
        elif self.option4.isChecked():
            if self.option4.text()==self.ans:
                flag=1
            else:
                flag=2
        if flag==0:
            QMessageBox.information(self,"答题","请选择一个选项",QMessageBox.Yes)
        elif flag==1:
            self.load()
            self.ans_num.display(self.ans_num.intValue()+1)
        else:
            QMessageBox.information(self,"答题结果","答案错误，正确答案是"+self.ans,QMessageBox.Yes)
            self.life_num.display(self.life_num.intValue()-1)
            if self.life_num.intValue()==0:
                self.send_result()
                return
            self.load()
        self.option1.setCheckable(False)
        self.option2.setCheckable(False)
        self.option3.setCheckable(False)
        self.option4.setCheckable(False)
        self.option1.setCheckable(True)
        self.option2.setCheckable(True)
        self.option3.setCheckable(True)
        self.option4.setCheckable(True)
    def click2(self):
        if self.tip_num.intValue()==0:
            QMessageBox.information(self,"提示","提示机会已用完",QMessageBox.Yes)
            return
        self.tip_num.display(self.tip_num.intValue()-1)
        QMessageBox.information(self,"提示","正确答案是"+self.ans,QMessageBox.Yes)
    def click3(self):
        reply = QMessageBox.question(self, '退出答题', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
        if reply == QMessageBox.Yes:  
             self.send_result()
        else:  
            return
    def setoption(self,opt1,opt2,opt3,opt4):
        self.option1.setText(opt1)
        self.option2.setText(opt2)
        self.option3.setText(opt3)
        self.option4.setText(opt4)
    def first_load(self):
        self.ans_num.display(0)
        self.life_num.display(3)
        self.tip_num.display(3)
        self.option1.setCheckable(False)
        self.option2.setCheckable(False)
        self.option3.setCheckable(False)
        self.option4.setCheckable(False)
        self.option1.setCheckable(True)
        self.option2.setCheckable(True)
        self.option3.setCheckable(True)
        self.option4.setCheckable(True)
        self.load()
    def load(self):
        data={'type':'poem_ques'}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.ans=recv['correct']
        self.question.setText(recv['question'])
        opt=[recv['correct']]+recv['wrong']
        random.shuffle(opt)
        self.setoption(opt[0],opt[1],opt[2],opt[3])
    
class IdiomGame(QMainWindow,Ui_idiom_game):
    def __init__(self,parent=None):
        super(IdiomGame,self).__init__(parent)
        self.setupUi(self)
        self.bt_list=[self.bt1,self.bt2,self.bt3,self.bt4,self.bt5,self.bt6,self.bt7,self.bt8,self.bt9,self.bt10,self.bt11,self.bt12,self.bt13,self.bt14,self.bt15,self.bt16,self.bt17,self.bt18,self.bt19,self.bt20,self.bt21,self.bt22,self.bt23,self.bt24,self.bt25,self.bt26,self.bt27,self.bt28]
        for i in range(28):
            self.listen(self.bt_list[i],i)
        self.fi_lb=[self.fi_lb1,self.fi_lb2,self.fi_lb3,self.fi_lb4,self.fi_lb5,self.fi_lb6,self.fi_lb7]
        self.tip_bt.clicked.connect(self.click2)
        self.exit_bt.clicked.connect(self.click3)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cnt_time)
    def cnt_time(self):
        self.time_cnt+=1
        self.time_lb.setText(str(self.time_cnt)+'s')
    def listen(self,bt,num):
        bt.clicked.connect(lambda : self.click1(bt,num))
    def send_result(self):
        data={'type':'idiom_result','acc':user,'idiom_score':self.time_cnt}
        s=Send_data()
        recv=s.message(data)
        s.close()
        QMessageBox.information(self,"答题结束","共作答"+str(self.time_cnt)+'s，打败全国'+recv['rate']+'的用户',QMessageBox.Yes)
        self.hide()
    def click1(self,bt,num):
        if self.bt_status[num]==False:
            bt.setStyleSheet("background: rgb(255,99,71)")
            self.bt_status[num]=True
            self.ans.append(num)
        else:
            while True:
                num1=self.ans.pop()
                bt1=self.bt_list[num1]
                self.bt_status[num1]=False
                if bt1==bt:
                    bt1.setStyleSheet("background: rgb(211,211,211)")
                    break
                else:
                    bt1.setStyleSheet("background: rgb(211,211,211)")
        if len(self.ans)==4:
            s1=''
            for i in self.ans:
                s1+=self.bt_list[i].text()
            if s1 in self.question:
                self.question.remove(s1)
                for i in self.fi_lb:
                    if i.text()=='':
                        i.setText(s1)
                        break
                for i in self.ans:
                    self.bt_list[i].hide()
            else:
                for i in self.ans:
                    self.bt_status[i]=False
                    self.bt_list[i].setStyleSheet("background: rgb(211,211,211)")
            self.ans=[]
        if len(self.question)==0:
            self.timer.stop()
            self.send_result()
    def click2(self):
        self.time_cnt+=self.time_add
        self.time_add+=10
        QMessageBox.information(self,"提示",self.question[0],QMessageBox.Yes)
    def click3(self):
        self.timer.stop()
        reply = QMessageBox.question(self, '退出游戏', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
        if reply == QMessageBox.Yes:  
             self.hide()
        else:  
            self.timer.start(1000)
    def load(self):
        data={'type':'idiom_ques'}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.question=recv['question']
        self.ans=[]
        self.word_list=[]
        self.bt_status=[False for i in range(28)]
        #print(recv['question'])
        for i in recv['question']:
            for j in i:
                self.word_list.append(j)
        random.shuffle(self.word_list)
        for i in range(28):
            self.bt_list[i].setText(self.word_list[i])
            self.bt_list[i].setStyleSheet("background: rgb(211,211,211)")
            self.bt_list[i].show()
        for i in self.fi_lb:
            i.setText('')
        self.time_cnt=0
        self.time_add=10
        self.time_lb.setText('0s') 
        self.timer.start(1000)

class GameRule(QMainWindow,Ui_game_rule):
    def __init__(self,parent=None):
        super(GameRule,self).__init__(parent)
        self.setupUi(self)
        self.exit_bt.clicked.connect(self.click1)
    def click1(self):
        self.hide()
class GameRank(QMainWindow,Ui_game_rank):
    def __init__(self,parent=None):
        super(GameRank,self).__init__(parent)
        self.setupUi(self)
        self.exit_bt.clicked.connect(self.click1)
        self.sel.currentIndexChanged.connect(self.click2)
        self.create_shan.clicked.connect(self.click3)
    def click1(self):
        self.hide()
    def click2(self):
        if self.sel.currentIndex()==0:
            data={'type':'poem_rank'}
            headlb=['昵称','性别','成绩（个）']
        else:
            data={'type':'idiom_rank'}
            headlb=['昵称','性别','成绩（秒）']
        s=Send_data()
        recv=s.message(data)
        s.close()
        l1=len(recv['rank'])
        self.data=recv['rank']
        self.model=QStandardItemModel(l1,3)
        self.model.setHorizontalHeaderLabels(headlb)
        for i in range(l1):
            for j in range(3):
                if j==2 and recv['rank'][i][j] in [0,0x3f3f3f3f]:
                    item=QStandardItem('无成绩')
                else:
                    item=QStandardItem('%s'%(recv['rank'][i][j]))
                self.model.setItem(i,j,item)
        self.rank_view.setModel(self.model)
    def draw1(self,title,a,b):
        matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
        matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
        labels = '公子','姑娘'
        fracs = [a, b]
        explode = [0,0.05]
        plt.axes(aspect=1)
        plt.title(title)
        plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
        plt.show()
    def click3(self):
        title=''
        a=b=0
        if self.sel.currentIndex()==0:
            title='诗词问答排名前100男女比例'
        else:
            title='成语消消看排名前100男女比例'
        for i in self.data:
            if i[1]=='公子':
                a+=1
            else:
                b+=1
        self.draw1(title,a,b)
class PerInfo(QMainWindow,Ui_per_info):
    def __init__(self,parent=None):
        super(PerInfo,self).__init__(parent)
        self.setupUi(self)
        self.exit_bt.clicked.connect(self.click1)
        self.change_bt.clicked.connect(self.click2)
    def click1(self):
        self.hide()
    def click2(self):
        acc=self.username.text()
        pass1=self.pass1.text()
        pass2=self.pass2.text()
        nickname=self.nickname.text()
        sex=self.sex.currentText()
        if pass1=='' or nickname=='':
            QMessageBox.information(self,"修改个人信息","个人信息不能为空",QMessageBox.Yes)
            return
        if pass1!=''.join(pass1.split()) or nickname!=''.join(nickname.split()):
            QMessageBox.information(self,"修改个人信息","个人信息不能包含空白字符",QMessageBox.Yes)
            return
        if pass1!=pass2:
            QMessageBox.information(self,"修改个人信息","两次输入的密码必须相同",QMessageBox.Yes)
            return
        data={'type':'update_info','acc':acc,'passwd':pass1,'nickname':nickname,'sex':sex}
        s=Send_data()
        recv=s.message(data)
        s.close()
        if recv['result']=='success':
            QMessageBox.information(self,"修改","修改成功",QMessageBox.Yes)
        else:
            QMessageBox.information(self,"修改","修改失败",QMessageBox.Yes)
    def load(self):
        data={'type':'view_info','acc':user}
        s=Send_data()
        recv=s.message(data)
        s.close()
        self.username.setText(recv['result'][0])
        self.username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pass1.setText(recv['result'][1])
        self.pass2.setText(recv['result'][1])
        self.nickname.setText(recv['result'][2])
        self.sex.setCurrentText(recv['result'][3])
        if recv['result'][4]==0:
            self.poem_score.setText('无成绩')
        else:
            self.poem_score.setText(str(recv['result'][4])+'个')
        self.poem_score.setFocusPolicy(QtCore.Qt.NoFocus)
        if recv['result'][5]==0x3f3f3f3f:
            self.idiom_score.setText('无成绩')
        else:
            self.idiom_score.setText(str(recv['result'][5])+'秒')
        self.idiom_score.setFocusPolicy(QtCore.Qt.NoFocus)

if __name__ == '__main__':
    user=''
    app = QApplication(sys.argv)
    myWin1=Register()
    myWin1.show()
    myWin2=Login()
    myWin3=MainWin()
    myWin4=PoemGame()
    myWin5=IdiomGame()
    myWin6=GameRule()
    myWin7=GameRank()
    myWin8=PerInfo()
    if app.exec_()==0:
        sys.exit(0)