# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/game_rule.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_rule(object):
    def setupUi(self, game_rule):
        game_rule.setObjectName("game_rule")
        game_rule.resize(800, 600)
        game_rule.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(game_rule)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 80, 601, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 280, 601, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.exit_bt = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit_bt.setGeometry(QtCore.QRect(670, 0, 131, 48))
        self.exit_bt.setObjectName("exit_bt")
        game_rule.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(game_rule)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        game_rule.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(game_rule)
        self.statusbar.setObjectName("statusbar")
        game_rule.setStatusBar(self.statusbar)

        self.retranslateUi(game_rule)
        QtCore.QMetaObject.connectSlotsByName(game_rule)

    def retranslateUi(self, game_rule):
        _translate = QtCore.QCoreApplication.translate
        game_rule.setWindowTitle(_translate("game_rule", "规则解说"))
        self.textBrowser.setHtml(_translate("game_rule", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">诗词填空游戏规则</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    </span><span style=\" font-size:14pt;\">玩家通过回答与诗词有关的问题来得分，并且有三次作答机会和三次提示机会。玩家每答错一题，作答机会减一。当玩家的作答机会用完之后，游戏结束。</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("game_rule", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">成语消消看游戏规则</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    </span><span style=\" font-size:14pt;\">开局会有28个汉字，对应着7组成语。玩家通过按顺序点击成语的每一个字来消除成语，最后玩家的成绩是通关时间。玩家可以点击提示来获取成语内容，但是点击提示会增加游戏时间（依次增加10、20、30...）。</span></p></body></html>"))
        self.exit_bt.setText(_translate("game_rule", "返回主页"))
