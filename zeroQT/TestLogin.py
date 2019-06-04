'''
coder:Zero Net
date:2019/5/30
'''
import sys
import Login
from PyQt5.QtWidgets import QApplication,QFrame,QMessageBox
from PyQt5.QtCore import QCoreApplication

if __name__ == '__main__':
    def usr_login():
        usr_name = ui.lineEdit.text()
        usr_pwd = ui.lineEdit_2.text()
        if usr_name == '1024' and usr_pwd == '1234':
            QMessageBox.information(Frame, '消息',
                                    "登录成功")

        else:
            QMessageBox.warning(Frame, '消息',
                                "用户名或密码错误")
        print()


    app = QApplication(sys.argv)
    Frame = QFrame()
    ui = Login.Ui_Frame()
    # 调用setupUi方法动态创建控件
    ui.setupUi(Frame)
    ui.pushButton.clicked[bool].connect(usr_login)
    ui.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
    # 显示窗口
    Frame.show()

    # 当窗口关闭后会退出程序
    sys.exit(app.exec_())