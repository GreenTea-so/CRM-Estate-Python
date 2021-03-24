import fire
from delete2 import Post
import dar

post=Post()

def help():
    print("create_dom(адрес владельца, общая площадь, тип объекта, срок эксплатации) - Позволяет создать дом")




def create_user(passfrase):

    try:
        post.create_user(str(passfrase))
        print("Аккаунт успешно создан")


    except:

        print("Ошибка регистрации аккаунта")


def delete_user(addr):

    try:
        post.delete_user(str(addr))
        print("Аккаунт успешно удален")

    except:

        print("Ошибка удаления аккаунта")

def auth(address, passfrase):

    try:
        post.autorization_console(address, passfrase)



        print("Авторизация прошла успешно")

    except:

        print("Ошибка авторизации")




def create_dom(owner, plob, type_obj, srok):  # вызывает админ

    try:
        post.create_dom(owner, plob, type_obj, srok)

        print("Дошло")
        dar.create_threads(1, 1, "Срок", int(post.dom_number() - 1), int(srok))

        print("Дом " + "№" + str(int(post.dom_number() - 1)) + " создан" )

    except:

        print("Ошибка создания дома")



def check_dom(dom_id):

    try:
        print(str(post.check_dom(dom_id)[0]))
        print(str(post.check_dom(dom_id)[1]))
        print(str(post.check_dom(dom_id)[2]))
        print(str(post.check_dom(dom_id)[3]))
        print(str(post.check_dom(dom_id)[4]))
        print(str(int(post.check_dom(dom_id)[5])))


    except:

        print("Ошибка просмотра дома")


###########################################################################
###########################################################################
###########################################################################
###########################################################################


def create_dar(id_dom, renter, time):  # вызывает владелец

    try:

        post.create_dar(int(id_dom), renter, 5)
        dar.create_threads(int(time), 1, "дарения", post.dar_number())
        print("Дарение " + "№" + str(int(post.dar_number() - 1)) + " создано")


    except:

        print("Ошибка создания дарения")

def get_dar(id_dar):  # вызывает владелец

    try:

        post.get_dar(int(id_dar))


    except:

        print("Ошибка подтверждения дарения")


def stop_dar(id_dar):  # вызывает владелец

    try:
        post.stop_dar(int(id_dar))

    except:
        print("Ошибка отмены дарения")

def dar_cancel(id_dar):  # вызывает получатель

    try:

        post.dar_cancel(int(id_dar))

    except:

        print("Ошибка отмены дарения")

###########################################################################
###########################################################################
###########################################################################
###########################################################################


def create_sell(dom_id, amount, srok):  # вызывает владелец

    try:

        post.create_sell(int(dom_id), int(amount), int(srok))

        dar.create_threads(int(srok), 1, "продажи", post.sell_number())

        print("Продажа " + "№" + str(int(post.sell_number() - 1)) + " создана")

    except:

        print("Ошибка создания продажи")

def buy(id_sell, amount):  # вызывает покупатель


    try:
        post.buy(int(id_sell), int(amount))



    except:

        print("Ошибка подтверждения покупки")


def stop_sell(id_sell):  # вызывает владелец

    try:
        post.stop_sell(int(id_sell))


    except:

        print("Ошибка отмены покупки")

def cancel_sell(id_sell):  # вызывает покупаель

    try:

        post.cancel_sell(int(id_sell))


    except:

        print("Ошибка отмены покупки")


def take_money(id_sell):  # вызывает владелец

    try:
        post.take_money(int(id_sell))


    except:

        print("Ошибка подтверждения покупки")

def check_sell(id_sell):


    try:
        print(str(post.check_sell(id_sell)[1]))
        print(str(post.check_sell(id_sell)[2]))
        print(str(post.check_sell(id_sell)[3]))
        print(str(post.check_sell(id_sell)[4]))

        print(str(int(post.check_sell(id_sell)[5])))

    except:

        print("Ошибка просмотра покупки")

def check_sell_for_renter(id_sell):


    try:

        print(str(post.check_sell(id_sell)[1]))
        print(str(post.check_sell(id_sell)[2]))
        print(str(post.check_sell(id_sell)[3]))
        print(str(post.check_sell(id_sell)[4]))

        print(str(int(post.check_sell(id_sell)[5] / (24 * 60 * 60))))

    except:

        print("Ошибка просмотра покупки")



############################################
############################################
############################################
############################################

def create_zalog(dom_id, amount, srok, srok_zalog):

    try:
        post.create_zalog(int(dom_id),int(amount),int(srok),int(srok_zalog))
        print(post.zalog_number())
        dar.create_threads(int(srok), 1, "залога", post.zalog_number())


        print("Залог " + "№" + str(int(post.zalog_number() - 1)) + " создан")

    except:

        print("Ошибка создания залога")

def buy_zalog(id_zalog, amount):


    try:
        post.buy_zalog(int(id_zalog), int(amount))


    except:

        print("Ошибка подтверждения залога")

def take_money_for_zalog(id_zalog):


    try:

        post.take_money_for_zalog(int(id_zalog))



        dar.create_threads(int(post.check_zalog(int(id_zalog))[5]), 1, "залог", int(id_zalog))


    except:

        print("Ошибка подтверждения залога")

def return_money_for_zalog(id_zalog, amount):

    try:
        post.return_money_for_zalog(int(id_zalog), int(amount))


    except:

        print("Ошибка возврата средст с залога")


def stop_zalog(id_zalog):

    try:

        post.stop_zalog(int(id_zalog))


    except:

        print("Ошибка отмены залога")


def money_back_for_zalog(id_zalog):

    try:
        post.money_back_for_zalog(int(id_zalog))


    except:

        print("Ошибка отмены залога")

def check_zalog_for_owner(id_zalog):

    try:

        print(str(post.check_zalog(int(id_zalog))[1]))
        print(str(post.check_zalog(int(id_zalog))[2]))
        print(str(post.check_zalog(int(id_zalog))[3]))
        print(str(post.check_zalog(int(id_zalog))[4]))
        print(str(post.check_zalog(int(id_zalog))[5]))

    except:

        print("Ошибка просмотра залога")

def check_zalog_for_renter(id_zalog):


    try:

        print(str(post.check_zalog(int(id_zalog))[1]))
        print(str(post.check_zalog(int(id_zalog))[2]))
        print(str(post.check_zalog(int(id_zalog))[3]))
        print(str(post.check_zalog(int(id_zalog))[4]))
        print(str(post.check_zalog(int(id_zalog))[5]))

    except:

        print("Ошибка просмотра залога")





fire.Fire()