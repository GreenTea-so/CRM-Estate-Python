from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from kurs2 import Ui_MainWindow
from delete2 import Post
import dar
from sprav import Ui_Form
import razrab
import time




app = QtWidgets.QApplication(sys.argv)
Main = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Main)
ui.tabWidget.removeTab(0)
ui.tabWidget.removeTab(2)
Main.show()


Main_2 = QtWidgets.QMainWindow()
ui_2 = Ui_Form()
ui_2.setupUi(Main_2)


Main_3 = QtWidgets.QMainWindow()
ui_3 = razrab.Ui_Form()
ui_3.setupUi(Main_3)


post = Post()
srok=None


for i in range(len(post.only_my_dom())):
    ui.comboBox_2.addItem(str(post.only_my_dom()[i][0]))
    #print(i)


for i in range(len(post.only_my_sell())):
    ui.comboBox_5.addItem(str(post.only_my_sell()[i][0]))
    #print(i)


for i in range(len(post.only_my_buy())):
    ui.comboBox_3.addItem(str(post.only_my_buy()[i][0]))
    #print(i)


for i in range(len(post.only_my_zalog())):
    ui.comboBox.addItem(str(post.only_my_zalog()[i][0]))
    #print(i)



for i in range(len(post.only_my_zalog_for_renter())):
    ui.comboBox_4.addItem(str(post.only_my_zalog_for_renter()[i][0]))
    #print(i)



for i in range(len(post.accounts())):
    if post.check_user(post.accounts()[i]):
        ui.comboBox_6.addItem(str(post.accounts()[i]))
        #print(i)


dar.create_threads(10, ui, "Обновление", 100)


def clear_str():

    ui.label_13.clear()
    ui.label_14.clear()
    ui.label_15.clear()
    ui.label_16.clear()
    ui.label_17.clear()
    ui.label_18.clear()

    ui.label_19.clear()
    ui.label_20.clear()
    ui.label_21.clear()
    ui.label_22.clear()
    ui.label_23.clear()

    ui.label_24.clear()
    ui.label_25.clear()
    ui.label_26.clear()
    ui.label_27.clear()
    ui.label_28.clear()

    ui.label_29.clear()
    ui.label_30.clear()
    ui.label_31.clear()
    ui.label_32.clear()
    ui.label_33.clear()

    ui.label_34.clear()
    ui.label_35.clear()
    ui.label_36.clear()
    ui.label_37.clear()
    ui.label_38.clear()

    ui.lineEdit_17.clear()
    ui.lineEdit_10.clear()
    ui.lineEdit_15.clear()
    ui.lineEdit_16.clear()

    ui.lineEdit_7.clear()
    ui.lineEdit_8.clear()
    ui.lineEdit_18.clear()
    ui.lineEdit_19.clear()
    ui.lineEdit_25.clear()
    ui.lineEdit_11.clear()
    ui.lineEdit_20.clear()
    ui.lineEdit_30.clear()
    ui.lineEdit_21.clear()

    ui.lineEdit.clear()
    ui.lineEdit_2.clear()
    ui.lineEdit_31.clear()
    ui.lineEdit_22.clear()

    ui.lineEdit_3.clear()
    ui.lineEdit_5.clear()

    ui.lineEdit_12.clear()
    ui.lineEdit_13.clear()
    ui.lineEdit_14.clear()
    ui.lineEdit_32.clear()
    ui.lineEdit_26.clear()
    ui.lineEdit_35.clear()
    ui.lineEdit_34.clear()
    ui.lineEdit_27.clear()

    ui.lineEdit_23.clear()
    ui.lineEdit_24.clear()
    ui.lineEdit_33.clear()

    ui.lineEdit_28.clear()
    ui.lineEdit_29.clear()


    ui.lineEdit_36.clear()

    ui.label_48.clear()


def obnov():


    ui.comboBox_2.clear()
    ui.comboBox_5.clear()
    ui.comboBox_3.clear()
    ui.comboBox.clear()
    ui.comboBox_4.clear()
    ui.comboBox_6.clear()



    for i in range(len(post.only_my_dom())):
        ui.comboBox_2.addItem(str(post.only_my_dom()[i][0]))


    for i in range(len(post.only_my_sell())):
        ui.comboBox_5.addItem(str(post.only_my_sell()[i][0]))


    for i in range(len(post.only_my_buy())):
        ui.comboBox_3.addItem(str(post.only_my_buy()[i][0]))



    for i in range(len(post.only_my_zalog())):

        ui.comboBox.addItem(str(post.only_my_zalog()[i][0]))



    for i in range(len(post.only_my_zalog_for_renter())):
        ui.comboBox_4.addItem(str(post.only_my_zalog_for_renter()[i][0]))



    for i in range(len(post.accounts())):
        if post.check_user(post.accounts()[i]):
            ui.comboBox_6.addItem(str(post.accounts()[i]))
            # print(i)


def accounts():

    ui.lineEdit_37.setText(ui.comboBox_6.currentText())


def create_user():

    try:
        post.create_user(ui.lineEdit_36.text())
        post.obnov(ui)
        ui.label_48.setText("Аккаунт успешно создан")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка регистрации аккаунта")
        dar.create_threads(1, ui, "Оповещение", 0)


def delete_user():

    try:
        post.delete_user(ui.lineEdit_38.text())
        ui.label_48.setText("Аккаунт успешно удален")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка удаления аккаунта")
        dar.create_threads(1, ui, "Оповещение", 0)


def auth():

    try:

        str = ui.lineEdit_28.text()

        post.autorization(str, ui.lineEdit_29.text(), ui)

        ui.comboBox_2.clear()
        ui.comboBox_5.clear()
        ui.comboBox_3.clear()
        ui.comboBox.clear()
        ui.comboBox_4.clear()
        ui.comboBox_6.clear()

        obnov()
        clear_str()

        if str == post.geth.eth.accounts[0]:
            ui.label_81.setText("Вы зашли с аккаунта администратора:" + str)

        else:
            ui.label_81.setText("Вы зашли с аккаунта пользователя:" + str)


        try:
            post.auth_check(str)

            print("Не дошла")

            print("Не дошла")
            Main.close()
            ui.setupUi(Main)
            Main.show()

            if str == post.geth.eth.accounts[0]:
                ui.label_81.setText("Вы зашли с аккаунта администратора:" + str)

            else:
                ui.label_81.setText("Вы зашли с аккаунта пользователя:" + str)

            ui.exitAction.triggered.connect(spravka)
            ui.exitAction_2.triggered.connect(razrab)


            ui.pushButton_19.clicked.connect(auth)
            ui.pushButton_2.clicked.connect(create_user)
            ui.pushButton_12.clicked.connect(delete_user)
            ui.pushButton_5.clicked.connect(accounts)

            ui.pushButton_3.clicked.connect(create_dom)
            ui.pushButton_20.clicked.connect(check_dom)
            ui.pushButton_23.clicked.connect(only_my_dom)

            ui.pushButton.clicked.connect(create_dar)
            ui.pushButton_6.clicked.connect(get_dar)
            ui.pushButton_8.clicked.connect(stop_dar)
            ui.pushButton_9.clicked.connect(dar_cancel)

            ui.pushButton_4.clicked.connect(create_sell)
            ui.pushButton_10.clicked.connect(buy)
            ui.pushButton_7.clicked.connect(stop_sell)
            ui.pushButton_11.clicked.connect(cancel_sell)
            ui.pushButton_16.clicked.connect(take_money)
            ui.pushButton_21.clicked.connect(check_sell)
            ui.pushButton_23.clicked.connect(check_sell_for_renter)

            ui.pushButton_13.clicked.connect(create_zalog)
            ui.pushButton_14.clicked.connect(buy_zalog)
            ui.pushButton_17.clicked.connect(take_money_for_zalog)
            ui.pushButton_25.clicked.connect(return_money_for_zalog)
            ui.pushButton_18.clicked.connect(stop_zalog)
            ui.pushButton_15.clicked.connect(money_back_for_zalog)
            ui.pushButton_24.clicked.connect(check_zalog_for_owner)
            ui.pushButton_22.clicked.connect(check_zalog_for_renter)



        except:

            if ui.tabWidget.tabText(0)=="Регистрация":
                ui.tabWidget.removeTab(0)
                ui.tabWidget.removeTab(2)


        ui.label_49.setText("Авторизация прошла успешно")



    except:

        ui.label_49.setText("Ошибка авторизации")

def create_dom():  # вызывает админ

    try:
        post.create_dom(ui.lineEdit_17.text(), ui.lineEdit_15.text(), ui.lineEdit_16.text(), int(ui.lineEdit_10.text()))
        obnov()



        dar.create_threads(1, ui, "Срок", int(post.dom_number() - 1), int(ui.lineEdit_10.text()))

        ui.label_48.setText("Дом " + "№" + str(int(post.dom_number() - 1)) + " создан" )
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка создания дома")
        dar.create_threads(1, ui, "Оповещение", 0)



def delete_dom():
    ui.label_19.setText("123")


def check_dom():

    try:

        ui.label_13.setText(str(post.check_dom(ui.comboBox_2.currentText())[0]))
        ui.label_14.setText(str(post.check_dom(ui.comboBox_2.currentText())[1]))
        ui.label_15.setText(str(post.check_dom(ui.comboBox_2.currentText())[2]))
        ui.label_16.setText(str(post.check_dom(ui.comboBox_2.currentText())[3]))
        ui.label_17.setText(str(post.check_dom(ui.comboBox_2.currentText())[4]))
        ui.label_18.setText(str(int(post.check_dom(ui.comboBox_2.currentText())[5])))


    except:

        ui.label_48.setText("Ошибка просмотра дома")
        dar.create_threads(1, ui, "Оповещение", 0)


def only_my_dom():

    #print("Вызвалась")
    print(post.only_my_dom())



def create_dar():  # вызывает владелец

    try:

        post.create_dar(int(ui.lineEdit.text()), ui.lineEdit_2.text(), 5)
        dar.create_threads(int(ui.lineEdit_31.text()), ui, "дарения", post.dar_number())
        ui.label_48.setText("Дарение " + "№" + str(int(post.dar_number() - 1)) + " создано")
        dar.create_threads(1, ui, "Оповещение", 0)



    except:

        ui.label_48.setText("Ошибка создания дарения")
        dar.create_threads(1, ui, "Оповещение", 0)

def get_dar():  # вызывает владелец

    try:

        post.get_dar(int(ui.lineEdit_3.text()))
        obnov()
        ui.label_48.setText("Дарение успешно подтверждено")

    except:

        ui.label_48.setText("Ошибка подтверждения дарения")
        dar.create_threads(1, ui, "Оповещение", 0)


def stop_dar():  # вызывает владелец

    try:


        post.stop_dar(int(ui.lineEdit_22.text()))
        ui.label_48.setText("Дарение отменено")
        dar.create_threads(1, ui, "Оповещение", 0)



    except:

        ui.label_48.setText("Ошибка отмены дарения")
        dar.create_threads(1, ui, "Оповещение", 0)

def dar_cancel():  # вызывает получатель

    try:

        post.dar_cancel(int(ui.lineEdit_5.text()))
        ui.label_48.setText("Дарение отменено")
        dar.create_threads(1, ui, "Оповещение", 0)


    except:

        ui.label_48.setText("Ошибка отмены дарения")
        dar.create_threads(1, ui, "Оповещение", 0)

###########################################################################
###########################################################################
###########################################################################
###########################################################################

def create_sell():  # вызывает владелец

    try:

        post.create_sell(int(ui.lineEdit_7.text()), int(ui.lineEdit_8.text()), int(ui.lineEdit_19.text()))

        dar.create_threads(int(ui.lineEdit_19.text()), ui, "продажи", post.sell_number())
        obnov()
        ui.label_48.setText("Продажа " + "№" + str(int(post.sell_number() - 1)) + " создана")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка создания продажи")
        dar.create_threads(1, ui, "Оповещение", 0)

def buy():  # вызывает покупатель


    try:
        post.buy(int(ui.lineEdit_20.text()), int(ui.lineEdit_30.text()))

        obnov()
        ui.label_48.setText("Деньги успешно переведены")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка подтверждения покупки")
        dar.create_threads(1, ui, "Оповещение", 0)


def stop_sell():  # вызывает владелец

    try:
        post.stop_sell(int(ui.lineEdit_11.text()))
        obnov()
        ui.label_48.setText("Покупка отменена")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка отмены покупки")
        dar.create_threads(1, ui, "Оповещение", 0)

def cancel_sell():  # вызывает покупаель

    try:

        post.cancel_sell(int(ui.lineEdit_21.text()))
        obnov()
        ui.label_48.setText("Покупка отменена")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка отмены покупки")
        dar.create_threads(1, ui, "Оповещение", 0)


def take_money():  # вызывает владелец

    try:
        post.take_money(int(ui.lineEdit_25.text()))
        obnov()
        ui.label_48.setText("Покупка была успешно произведена")

    except:

        ui.label_48.setText("Ошибка подтверждения покупки")
        dar.create_threads(1, ui, "Оповещение", 0)

def check_sell():


    try:
        ui.label_19.setText(str(post.check_sell(ui.comboBox_5.currentText())[1]))
        ui.label_20.setText(str(post.check_sell(ui.comboBox_5.currentText())[2]))
        ui.label_21.setText(str(post.check_sell(ui.comboBox_5.currentText())[3]))
        ui.label_23.setText(str(post.check_sell(ui.comboBox_5.currentText())[4]))

        ui.label_22.setText(str(int(post.check_sell(ui.comboBox_5.currentText())[5] )))

    except:

        ui.label_48.setText("Ошибка просмотра покупки")
        dar.create_threads(1, ui, "Оповещение", 0)

def check_sell_for_renter():


    try:

        ui.label_24.setText(str(post.check_sell(int(ui.comboBox_3.currentText()))[1]))
        ui.label_25.setText(str(post.check_sell(int(ui.comboBox_3.currentText()))[2]))
        ui.label_26.setText(str(post.check_sell(int(ui.comboBox_3.currentText()))[3]))
        ui.label_27.setText(str(post.check_sell(int(ui.comboBox_3.currentText()))[4]))

        ui.label_28.setText(str(int(post.check_sell(int(ui.comboBox_3.currentText()))[5] / (24 * 60 * 60))))

    except:

        ui.label_48.setText("Ошибка просмотра покупки")
        dar.create_threads(1, ui, "Оповещение", 0)

############################################
############################################
############################################
############################################

def create_zalog():

    try:
        post.create_zalog(int(ui.lineEdit_12.text()),int(ui.lineEdit_13.text()),int(ui.lineEdit_14.text()),int(ui.lineEdit_32.text()))
        print(post.zalog_number())
        dar.create_threads(int(ui.lineEdit_14.text()), ui, "залога", post.zalog_number())

        obnov()
        ui.label_48.setText("Залог " + "№" + str(int(post.zalog_number() - 1)) + " создан")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка создания залога")
        dar.create_threads(1, ui, "Оповещение", 0)

def buy_zalog():


    try:
        post.buy_zalog(int(ui.lineEdit_23.text()), int(ui.lineEdit_33.text()))
        obnov()
        ui.label_48.setText("Деньги успешно переведены")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка подтверждения залога")
        dar.create_threads(1, ui, "Оповещение", 0)

def take_money_for_zalog():


    try:

        post.take_money_for_zalog(int(ui.lineEdit_26.text()))



        dar.create_threads(int(post.check_zalog(int(ui.lineEdit_26.text()))[5]), ui, "залог", int(ui.lineEdit_26.text()))
        obnov()
        ui.label_48.setText("Залог успешно произведен")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка подтверждения залога")
        dar.create_threads(1, ui, "Оповещение", 0)

def return_money_for_zalog():

    try:
        post.return_money_for_zalog(int(ui.lineEdit_35.text()), int(ui.lineEdit_34.text()))
        obnov()
        ui.label_48.setText("Деньги с залога были успешно возвращены")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка возврата средст с залога")
        dar.create_threads(1, ui, "Оповещение", 0)


def stop_zalog():

    try:

        post.stop_zalog(int(ui.lineEdit_27.text()))
        obnov()
        ui.label_48.setText("Залог отменен")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка отмены залога")
        dar.create_threads(1, ui, "Оповещение", 0)


def money_back_for_zalog():

    try:
        post.money_back_for_zalog(int(ui.lineEdit_24.text()))
        obnov()
        ui.label_48.setText("Залог отменен")
        dar.create_threads(1, ui, "Оповещение", 0)

    except:

        ui.label_48.setText("Ошибка отмены залога")
        dar.create_threads(1, ui, "Оповещение", 0)

def check_zalog_for_owner():

    try:

        ui.label_34.setText(str(post.check_zalog(int(ui.comboBox.currentText()))[1]))
        ui.label_35.setText(str(post.check_zalog(int(ui.comboBox.currentText()))[2]))
        ui.label_36.setText(str(post.check_zalog(int(ui.comboBox.currentText()))[3]))
        ui.label_37.setText(str(post.check_zalog(int(ui.comboBox.currentText()))[4]))
        ui.label_38.setText(str(post.check_zalog(int(ui.comboBox.currentText()))[5]))

    except:

        ui.label_48.setText("Ошибка просмотра залога")
        dar.create_threads(1, ui, "Оповещение", 0)

def check_zalog_for_renter():


    try:

        ui.label_29.setText(str(post.check_zalog(int(ui.comboBox_4.currentText()))[1]))
        ui.label_30.setText(str(post.check_zalog(int(ui.comboBox_4.currentText()))[2]))
        ui.label_31.setText(str(post.check_zalog(int(ui.comboBox_4.currentText()))[3]))
        ui.label_32.setText(str(post.check_zalog(int(ui.comboBox_4.currentText()))[4]))
        ui.label_33.setText(str(post.check_zalog(int(ui.comboBox_4.currentText()))[5]))

    except:

        ui.label_48.setText("Ошибка просмотра залога")
        dar.create_threads(1, ui, "Оповещение", 0)


def spravka():

    Main_2.show()

def razrab():

    Main_3.show()


ui.exitAction.triggered.connect ( spravka )
ui.exitAction_2.triggered.connect ( razrab )


ui.pushButton_19.clicked.connect( auth )
ui.pushButton_2.clicked.connect( create_user )
ui.pushButton_12.clicked.connect( delete_user )
ui.pushButton_5.clicked.connect ( accounts )


ui.pushButton_3.clicked.connect( create_dom )
ui.pushButton_20.clicked.connect( check_dom )
ui.pushButton_23.clicked.connect ( only_my_dom )


ui.pushButton.clicked.connect( create_dar )
ui.pushButton_6.clicked.connect( get_dar )
ui.pushButton_8.clicked.connect( stop_dar )
ui.pushButton_9.clicked.connect( dar_cancel )


ui.pushButton_4.clicked.connect( create_sell )
ui.pushButton_10.clicked.connect( buy )
ui.pushButton_7.clicked.connect( stop_sell )
ui.pushButton_11.clicked.connect( cancel_sell )
ui.pushButton_16.clicked.connect( take_money )
ui.pushButton_21.clicked.connect( check_sell )
ui.pushButton_23.clicked.connect( check_sell_for_renter )


ui.pushButton_13.clicked.connect( create_zalog )
ui.pushButton_14.clicked.connect( buy_zalog )
ui.pushButton_17.clicked.connect( take_money_for_zalog )
ui.pushButton_25.clicked.connect( return_money_for_zalog )
ui.pushButton_18.clicked.connect( stop_zalog )
ui.pushButton_15.clicked.connect( money_back_for_zalog )
ui.pushButton_24.clicked.connect( check_zalog_for_owner )
ui.pushButton_22.clicked.connect( check_zalog_for_renter )



sys.exit(app.exec_())