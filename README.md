# Chinese-character-game
基于Python的汉字游戏

## 简介
- 本项目使用Python语言编写，实现了诗词问答和成语消消看两种玩法。

## 功能
- 用户可以注册并登录。
- 用户登录之后可以玩诗词问答和成语消消看两款游戏。
- 用户可以查看游戏规则和排行榜。
- 用户可以查看并修改个人信息。

## 实现思路
- 诗词问答：从数据库中的名句表里，随机拿出一个名句，按照四种出题风格（猜上句、猜下局、猜作者、猜出处）将题目发送给用户进行作答，用户答对即可加分。
- 成语消消看：从数据库中的成语表里，随机拿出7个成语，将它们拆开，随机放在28个方格中，用户依次点击一个成语的四个汉字即可将它消掉，全部消掉获得胜利。

## 数据采集部分
- get_poem.py：爬取名句
- deal_poem.py：处理名句数据
- deal_idiom.py：处理成语数据

## 服务端
- server.py：服务端基本代码
- mysql_op.py：mysql基本操作

## 客户端
- Main.py：客户端基本代码
- send_data.py：客户端向服务端发送消息，并接受返回消息
- ui文件夹：客户端界面的ui文件
- window文件夹：客户端界面的py文件

## 数据库设计
- 用户（账号，密码，昵称，性别，诗词成绩，成语成绩）
- 名句（名句id，上句，下句，诗词作者，诗词名）
- 成语（成语id，成语）
- **具体可见chinese.sql**

## 包安装
- pyqt5安装：
pip install pyqt5 -i https://pypi.douban.com/simple
- pyqt5-designer安装：
pip install pyqt5-tools -i https://pypi.douban.com/simple

## 项目运行

1. 通过chinese.sql文件创建数据库、相关数据表。
2. 运行server.py文件，即开启服务器。
3. 运行Main.py文件，即运行客户端，玩家就可以愉快的玩游戏了。

## 界面展示

- 注册

<img src="pic\图片1.jpg" alt="图片1" style="zoom:25%;" />

- 登录

<img src="pic\图片2.jpg" alt="图片2" style="zoom:25%;" />

- 主界面

<img src="pic\图片3.jpg" alt="图片3" style="zoom:25%;" />

- 诗词问答

<img src="pic\图片4.jpg" alt="图片4" style="zoom:25%;" />

<img src="pic\图片5.jpg" alt="图片5" style="zoom:25%;" />

- 成语消消看

<img src="pic\图片6.jpg" alt="图片6" style="zoom:25%;" />

<img src="pic\图片7.jpg" alt="图片7" style="zoom:25%;" />

- 规则解说

<img src="pic\图片8.jpg" alt="图片8" style="zoom:25%;" />

- 排行榜

<img src="pic\图片9.jpg" alt="图片9" style="zoom:25%;" />

<img src="pic\图片10.jpg" alt="图片10" style="zoom:25%;" />

<img src="pic\图片11.jpg" alt="图片11" style="zoom:25%;" />

<img src="pic\图片12.jpg" alt="图片12" style="zoom:25%;" />

- 个人信息

<img src="pic\图片13.jpg" alt="图片13" style="zoom:25%;" />

