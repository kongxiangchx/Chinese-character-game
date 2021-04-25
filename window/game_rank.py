# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/game_rank.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_game_rank(object):
    def setupUi(self, game_rank):
        game_rank.setObjectName("game_rank")
        game_rank.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(game_rank)
        self.centralwidget.setObjectName("centralwidget")
        self.rank_view = QtWidgets.QTableView(self.centralwidget)
        self.rank_view.setGeometry(QtCore.QRect(160, 100, 411, 371))
        self.rank_view.setObjectName("rank_view")
        self.sel = QtWidgets.QComboBox(self.centralwidget)
        self.sel.setGeometry(QtCore.QRect(220, 30, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sel.setFont(font)
        self.sel.setObjectName("sel")
        self.sel.addItem("")
        self.sel.addItem("")
        self.exit_bt = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit_bt.setGeometry(QtCore.QRect(670, 0, 131, 48))
        self.exit_bt.setObjectName("exit_bt")
        self.create_shan = QtWidgets.QPushButton(self.centralwidget)
        self.create_shan.setGeometry(QtCore.QRect(670, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.create_shan.setFont(font)
        self.create_shan.setObjectName("create_shan")
        game_rank.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(game_rank)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        game_rank.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(game_rank)
        self.statusbar.setObjectName("statusbar")
        game_rank.setStatusBar(self.statusbar)

        self.retranslateUi(game_rank)
        QtCore.QMetaObject.connectSlotsByName(game_rank)

    def retranslateUi(self, game_rank):
        _translate = QtCore.QCoreApplication.translate
        game_rank.setWindowTitle(_translate("game_rank", "排行榜"))
        self.sel.setItemText(0, _translate("game_rank", "诗词问答排名前100"))
        self.sel.setItemText(1, _translate("game_rank", "成语消消看排名前100"))
        self.exit_bt.setText(_translate("game_rank", "返回主页"))
        self.create_shan.setText(_translate("game_rank", "男女比例扇形图"))
