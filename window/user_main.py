# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/user_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_main(object):
    def setupUi(self, user_main):
        user_main.setObjectName("user_main")
        user_main.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(user_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 110, 321, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.poem_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.poem_bt.setFont(font)
        self.poem_bt.setObjectName("poem_bt")
        self.verticalLayout.addWidget(self.poem_bt)
        self.idiom_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.idiom_bt.setFont(font)
        self.idiom_bt.setObjectName("idiom_bt")
        self.verticalLayout.addWidget(self.idiom_bt)
        self.rule_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rule_bt.setFont(font)
        self.rule_bt.setObjectName("rule_bt")
        self.verticalLayout.addWidget(self.rule_bt)
        self.rank_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rank_bt.setFont(font)
        self.rank_bt.setObjectName("rank_bt")
        self.verticalLayout.addWidget(self.rank_bt)
        self.info_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.info_bt.setFont(font)
        self.info_bt.setObjectName("info_bt")
        self.verticalLayout.addWidget(self.info_bt)
        user_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        user_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user_main)
        self.statusbar.setObjectName("statusbar")
        user_main.setStatusBar(self.statusbar)

        self.retranslateUi(user_main)
        QtCore.QMetaObject.connectSlotsByName(user_main)

    def retranslateUi(self, user_main):
        _translate = QtCore.QCoreApplication.translate
        user_main.setWindowTitle(_translate("user_main", "汉字天地"))
        self.label.setText(_translate("user_main", "汉字天地"))
        self.poem_bt.setText(_translate("user_main", "诗词问答"))
        self.idiom_bt.setText(_translate("user_main", "成语消消看"))
        self.rule_bt.setText(_translate("user_main", "规则解说"))
        self.rank_bt.setText(_translate("user_main", "排行榜"))
        self.info_bt.setText(_translate("user_main", "个人信息"))
