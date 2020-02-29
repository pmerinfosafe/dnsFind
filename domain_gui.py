# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'domain_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from PyQt5Demo.lib.datatype import AttribDict
from dnsFind.core.dnsfind import DnsFind
from dnsFind.core.config import init_option


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 10, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 51, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 10, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 51, 21))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(470, 10, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(330, 60, 111, 131))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 60, 111, 131))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget = QtWidgets.tableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 311, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "domain:"))
        self.lineEdit.setText(_translate("MainWindow", "baidu.com"))
        self.comboBox.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox.setItemText(1, _translate("MainWindow", "15"))
        self.comboBox.setItemText(2, _translate("MainWindow", "25"))
        self.comboBox.setItemText(3, _translate("MainWindow", "30"))
        self.label_2.setText(_translate("MainWindow", "threads:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "25"))
        self.label_3.setText(_translate("MainWindow", "timeout:"))
        self.checkBox.setText(_translate("MainWindow", "finger"))
        self.pushButton_add.setText(_translate("MainWindow", "添加"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "keyword"))
        self.pushButton_add.clicked.connect(self.add_line)
        self.pushButton.clicked.connect(self.generate)
        # self.pushButton.connect()
    def add_line(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        # id = str(self.id)
        # name = self.faker.name()
        # add = self.faker.address()
        value = ''

        self.tableWidget.setItem(row, 0, QTableWidgetItem(value))
        # self.rule.append([comboBox.currentData(),value])
        # self.id += 1

    def generate(self):
        options = AttribDict()
        options.target = self.lineEdit.text()
        options.threads_count = self.comboBox.currentText()
        options.timeout = self.comboBox_2.currentText()
        finger_checked = self.checkBox.isChecked()
        if finger_checked :
            options.finger = 'finger'
        count = self.tableWidget.rowCount()
        keywords_list = []
        for rows_index in range(count):
            widget_item = self.tableWidget.item(rows_index, 0)
            text = widget_item.text()
            if text.strip()=='':
                continue
            keywords_list.append(text)
            pass

        options.keywords = ".".join(keywords_list)
        self.pushButton.setText("进行中。。")
        DnsFind(init_option(options)).run()
        self.pushButton.setText("搞定")
        # reply = self.QMessageBox.information(self,"对话框","查询完成，报先生成在对应文件夹内",self.QMessageBox.Yes)
        pass