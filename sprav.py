# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sprav.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon("scrin\wopros.jpg"))

        Form.resize(430, 423)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);r")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 431, 421))
        self.textBrowser.setObjectName("textBrowser")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Справка"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Данное приложение позволяет производить несколько оппераций над недвижимостью, а именно: дарение, продажа и залог.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Перед началом использования необходимо авторизоваться в системе. Для этого перейдите в раздел </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Авторизация </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">и введите свой логин и пароль от аккаунта. Нажав на кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Войти</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> произойдет авторизация.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"scrin\\auth.png\" width=\"250\" height=\"200\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Чтобы просмотреть всю информацию о недвижимости, продажах или залогах необходимо перейти во вкладку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Личный кабинет. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Указав идентификатор объекта, нажмите кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Просмотреть</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"scrin\\kabinet.png\" width=\"400\" height=\"250\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Чтобы создать предложение о дарении, перейдите во вкладку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Дарение</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">. Введя данные в поля, нажмите на кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Создать дарение</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"scrin\\dar.png\" width=\"300\" height=\"350\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Чтобы создать предложение о продаже, перейдите во вкладку Продажа. Введя данные в поля, нажмите на кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Создать предложение.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"scrin\\sell.png\" width=\"300\" height=\"350\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Чтобы создать предложение о залоге, перейдите во вкладку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Залог</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">. Введя данные в поля, нажмите на кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Создать залог</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"scrin\\zalog.png\" width=\"300\" height=\"350\" /></p></body></html>"))
