import pymysql
import random
import json


class User_op:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = ''
        self.port = 3306

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host, user=self.user, passwd=self.passwd, port=self.port, charset='utf8')
        self.conn.select_db('Chinese')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def register(self, acc, passwd, nickname, sex):
        self.connect()
        self.cur.execute(
            'select account from user where account=%s or nickname=%s', [acc, nickname])
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return False
        value = [acc, passwd, nickname, sex, 0, 0x3f3f3f3f]
        self.cur.execute(
            'insert into user(account,password,nickname,sex,poem_score,idiom_score) values(%s,%s,%s,%s,%s,%s)', value)
        self.conn.commit()
        self.close()
        return True

    def login(self, acc, passwd):
        self.connect()
        value = [acc, passwd]
        self.cur.execute(
            'select account,password from user where account=%s and password=%s', value)
        data = self.cur.fetchone()
        if data is not None:
            self.close()
            return True
        self.close()
        return False

    def poem_ques1(self, sen_id):
        self.connect()
        self.cur.execute(
            'select sen_up,sen_next from sentence where sen_id=%s', [sen_id])
        ans = self.cur.fetchone()
        self.cur.execute('select sen_next from sentence where length(sen_next)=%s and sen_id!=%s', [
                         len(ans[1])*3, sen_id])
        option = self.cur.fetchall()
        if len(option) <= 3:
            self.cur.execute(
                'select sen_next from sentence where sen_id!=%s', [sen_id])
            option = self.cur.fetchall()
        l = [i for i in range(0, len(option)-1)]
        l1 = random.sample(l, 3)
        for i in range(3):
            l1[i] = option[l1[i]][0]
        data = {'question': '“'+ans[0]+'”的下句是？',
                'correct': ans[1], 'wrong': l1}
        self.close()
        return data

    def poem_ques2(self, sen_id):
        self.connect()
        self.cur.execute(
            'select sen_up,sen_next from sentence where sen_id=%s', [sen_id])
        ans = self.cur.fetchone()
        self.cur.execute('select sen_up from sentence where length(sen_up)=%s and sen_id!=%s', [
                         len(ans[1])*3, sen_id])
        option = self.cur.fetchall()
        if len(option) <= 3:
            self.cur.execute(
                'select sen_up from sentence where sen_id!=%s', [sen_id])
            option = self.cur.fetchall()
        l = [i for i in range(0, len(option)-1)]
        l1 = random.sample(l, 3)
        for i in range(3):
            l1[i] = option[l1[i]][0]
        data = {'question': '“'+ans[1]+'”的上句是？',
                'correct': ans[0], 'wrong': l1}
        self.close()
        return data

    def poem_ques3(self, sen_id):
        self.connect()
        self.cur.execute(
            'select sen_up,sen_next,sen_author from sentence where sen_id=%s', [sen_id])
        ans = self.cur.fetchone()
        self.cur.execute(
            'select sen_author from sentence group by sen_author having sen_author!=%s', [ans[2]])
        option = self.cur.fetchall()
        l = [i for i in range(0, len(option)-1)]
        l1 = random.sample(l, 3)
        for i in range(3):
            l1[i] = option[l1[i]][0]
        data = {'question': '“'+ans[0]+'，'+ans[1] +
                '”的作者是？', 'correct': ans[2], 'wrong': l1}
        self.close()
        return data

    def poem_ques4(self, sen_id):
        self.connect()
        self.cur.execute(
            'select sen_up,sen_next,sen_name from sentence where sen_id=%s', [sen_id])
        ans = self.cur.fetchone()
        self.cur.execute(
            'select sen_name from sentence group by sen_name having sen_name!=%s', [ans[2]])
        option = self.cur.fetchall()
        l = [i for i in range(0, len(option)-1)]
        l1 = random.sample(l, 3)
        for i in range(3):
            l1[i] = '《'+option[l1[i]][0]+'》'
        data = {'question': '“'+ans[0]+'，'+ans[1] +
                '”出自？', 'correct': '《'+ans[2]+'》', 'wrong': l1}
        self.close()
        return data

    def poem_result(self, acc, poem_score):
        self.connect()
        self.cur.execute(
            'select count(*) from user where poem_score<%s', [poem_score])
        num1 = self.cur.fetchone()
        self.cur.execute('select count(*) from user')
        num2 = self.cur.fetchone()
        rate = "%.2f%%" % (num1[0]/num2[0]*100)
        self.cur.execute('select poem_score from user where account=%s and poem_score<%s', [
                         acc, poem_score])
        data = self.cur.fetchone()
        if data is not None:
            self.cur.execute('update user set poem_score=%s where account=%s', [
                             poem_score, acc])
            self.conn.commit()
        data = {'rate': rate}
        self.close()
        return data

    def idiom_ques(self, idiom_id):
        self.connect()
        self.cur.execute(
            'select idiom_text from idiom where idiom_id in (%s,%s,%s,%s,%s,%s,%s)', idiom_id)
        data1 = self.cur.fetchall()
        self.close()
        l1 = []
        for i in data1:
            l1.append(i[0])
        data = {'question': l1}
        return data

    def idiom_result(self, acc, idiom_score):
        self.connect()
        self.cur.execute(
            'select count(*) from user where idiom_score>%s', [idiom_score])
        num1 = self.cur.fetchone()
        self.cur.execute('select count(*) from user')
        num2 = self.cur.fetchone()
        rate = "%.2f%%" % (num1[0]/num2[0]*100)
        self.cur.execute('select idiom_score from user where account=%s and idiom_score>%s', [
                         acc, idiom_score])
        data = self.cur.fetchone()
        if data is not None:
            self.cur.execute('update user set idiom_score=%s where account=%s', [
                             idiom_score, acc])
            self.conn.commit()
        data = {'rate': rate}
        self.close()
        return data

    def poem_rank(self):
        self.connect()
        self.cur.execute(
            'select nickname,sex,poem_score from user order by poem_score desc limit 100')
        data = self.cur.fetchall()
        self.close()
        return {'rank': data}

    def idiom_rank(self):
        self.connect()
        self.cur.execute(
            'select nickname,sex,idiom_score from user order by idiom_score limit 100')
        data = self.cur.fetchall()
        self.close()
        return {'rank': data}

    def view_info(self, acc):
        self.connect()
        self.cur.execute(
            'select account,password,nickname,sex,poem_score,idiom_score from user where account=%s', [acc])
        data = self.cur.fetchone()
        self.close()
        return {'result': data}

    def update_info(self, acc, passwd, nickname, sex):
        self.connect()
        try:
            self.cur.execute('update user set password=%s,nickname=%s,sex=%s where account=%s', [
                             passwd, nickname, sex, acc])
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.close()
            return False
        self.close()
        return True


if __name__ == "__main__":
    u1 = User_op()
