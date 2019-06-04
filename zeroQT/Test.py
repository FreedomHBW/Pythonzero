'''
coder:Zero Net
date:2019/5/28
'''
import sys
import Form
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__== '__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Form.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())