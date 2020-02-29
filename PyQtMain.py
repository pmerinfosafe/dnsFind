# FileName : PyQtDemo.py
# Author   : pmer_infosafe
# DateTime : 2020/2/28 11:07
# SoftWare : PyCharm

import sys
import domain_gui
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget


class MyMain(QMainWindow, domain_gui.Ui_MainWindow):  # 继承主窗口函数的类, 继承编写的主函数

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = domain_gui.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())