# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/per_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_per_info(object):
    def setupUi(self, per_info):
        per_info.setObjectName("per_info")
        per_info.resize(800, 578)
        self.centralwidget = QtWidgets.QWidget(per_info)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 40, 441, 287))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.pass1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass1.setFont(font)
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass1.setObjectName("pass1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass1)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.pass2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass2.setFont(font)
        self.pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2.setObjectName("pass2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pass2)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.nickname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nickname.setFont(font)
        self.nickname.setObjectName("nickname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nickname)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.sex = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex.sizePolicy().hasHeightForWidth())
        self.sex.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sex)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.poem_score = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.poem_score.setFont(font)
        self.poem_score.setText("")
        self.poem_score.setObjectName("poem_score")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.poem_score)
        self.idiom_score = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.idiom_score.setFont(font)
        self.idiom_score.setObjectName("idiom_score")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.idiom_score)
        self.change_bt = QtWidgets.QPushButton(self.centralwidget)
        self.change_bt.setGeometry(QtCore.QRect(310, 380, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.change_bt.setFont(font)
        self.change_bt.setObjectName("change_bt")
        self.exit_bt = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit_bt.setGeometry(QtCore.QRect(670, 0, 131, 48))
        self.exit_bt.setObjectName("exit_bt")
        per_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(per_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        per_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(per_info)
        self.statusbar.setObjectName("statusbar")
        per_info.setStatusBar(self.statusbar)

        self.retranslateUi(per_info)
        QtCore.QMetaObject.connectSlotsByName(per_info)

    def retranslateUi(self, per_info):
        _translate = QtCore.QCoreApplication.translate
        per_info.setWindowTitle(_translate("per_info", "个人信息"))
        self.label.setText(_translate("per_info", "账号"))
        self.label_7.setText(_translate("per_info", "密码"))
        self.label_8.setText(_translate("per_info", "确认密码"))
        self.label_11.setText(_translate("per_info", "昵称"))
        self.label_9.setText(_translate("per_info", "性别"))
        self.sex.setItemText(0, _translate("per_info", "公子"))
        self.sex.setItemText(1, _translate("per_info", "姑娘"))
        self.label_12.setText(_translate("per_info", "诗词问答成绩"))
        self.label_13.setText(_translate("per_info", "成语消消看成绩"))
        self.change_bt.setText(_translate("per_info", "修改个人信息"))
        self.exit_bt.setText(_translate("per_info", "返回主页"))