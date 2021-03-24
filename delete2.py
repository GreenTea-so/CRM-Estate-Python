import web3
import json
import time
class Post():



    with open('abi.json', 'r') as f:
        abi=json.load(f)


    geth = None
    account = None
    passfrase = None
    cont = None
    address = web3.Web3.toChecksumAddress("0x39efeE9FFa6fCb589851024735998A5cB09F9175")

    srok_ex = []

    def __init__(self):
        self.geth = web3.Web3(web3.HTTPProvider("HTTP://26.200.208.237:7545"))
        self.geth.eth.defaultAccount = self.geth.eth.accounts[0]
        print(self.geth.eth.accounts)
        self.cont = self.geth.eth.contract(address = self.address, abi=self.abi)

        for i in range(len(self.accounts())):
            self.cont.functions.add_user(self.accounts()[i]).transact()



    def obnov(self, ui):

        ui.comboBox_2.clear()
        ui.comboBox_5.clear()
        ui.comboBox_3.clear()
        ui.comboBox.clear()
        ui.comboBox_4.clear()
        ui.comboBox_6.clear()



        for i in range(len(self.only_my_dom())):
            ui.comboBox_2.addItem(str(self.only_my_dom()[i][0]))

        for i in range(len(self.only_my_sell())):
            ui.comboBox_5.addItem(str(self.only_my_sell()[i][0]))

        for i in range(len(self.only_my_buy())):
            ui.comboBox_3.addItem(str(self.only_my_buy()[i][0]))

        for i in range(len(self.only_my_zalog())):
            ui.comboBox.addItem(str(self.only_my_zalog()[i][0]))

        for i in range(len(self.only_my_zalog_for_renter())):
            ui.comboBox_4.addItem(str(self.only_my_zalog_for_renter()[i][0]))

        for i in range(len(self.accounts())):
            if self.check_user(self.accounts()[i]):
                ui.comboBox_6.addItem(str(self.accounts()[i]))
                # print(i)



    def check_user(self, addr):


        return self.cont.functions.check_user(addr).call()


    def auth_check(self, addr):

        print("sdksdkjskd")
        print(addr)
        print(type(addr))
        self.cont.functions.auth_check(addr).transact()



    def accounts(self):

        return self.geth.eth.accounts


    def create_user(self, passfrase):

        self.cont.functions.admin_for().transact()
        self.geth.personal.newAccount(passfrase)
        addr = self.accounts()
        addr = addr[len(addr) - 1]
        print(addr)
        self.cont.functions.add_user(addr).transact()





    def delete_user(self, addr):

        self.cont.functions.delete_user(addr).transact();


    def autorization(self, address, passfrase, ui):



        if self.cont.functions.check_user(address).call()==True:
            self.geth.personal.unlockAccount(address, passfrase)
            self.geth.eth.defaultAccount = self.poisk(address)

            ui.label_79.setText(str(self.geth.eth.defaultAccount))

            # ui.label_79.setText(self.geth.eth.defaultAccount)
            print(self.poisk(address))
            print(self.geth.eth.defaultAccount)

        else:
            self.geth.personal.unlockAccount("111",231)



    def autorization_console(self, address, passfrase):

        print("1")
        print(address)
        print(passfrase)
        self.geth.personal.unlockAccount(address, passfrase)
        print("2")
        self.geth.eth.defaultAccount = self.poisk(address)
        print("3")

        print(self.poisk(address))
        print(self.geth.eth.defaultAccount)



    def create_dom(self, addr, plob, type_obj, srok):

        srok = time.time() - srok * 24 * 60 *60

        print("zdes")
        #print(srok)
        self.cont.functions.create_dom(addr, int(plob), str(type_obj), int(srok)).transact()

    def check_dom(self, id_home):



        #print(srok)
        return self.cont.functions.check_dom(int(id_home)).call()

    def set_srok(self, id_dom, srok):


        self.cont.functions.set_srok(id_dom, srok).transact()


    def only_my_dom(self):

        str_my_dom = []

        for i in range(self.dom_number()):

            str_my_dom.append(self.check_dom(i))


        str2_my_dom = []

        for i in range(len(str_my_dom)):

            if str_my_dom[i][1] == self.geth.eth.defaultAccount:
                str2_my_dom.append(str_my_dom[i])

        return str2_my_dom;







    def dom_number(self):
        return self.cont.functions.dom_number().call()

    def create_dar(self, id_dom, renter, time):

        self.cont.functions.create_dar(id_dom, renter, time).transact()



    def delete_dar(self, _dar_id):

        self.cont.functions.delete_dar(_dar_id).transact()


    def get_dar(self, id_dar):

        self.cont.functions.get_dar(id_dar, int(time.time())).transact()

    def stop_dar(self, id_dar):

        self.cont.functions.stop_dar(id_dar).transact()


    def dar_cancel(self, id_dar):

        self.cont.functions.dar_cancel(id_dar).transact()

    def dar_number(self):


        return self.cont.functions.dar_number().call()

    def get_users(self):
        users = self.geth.eth.accounts
        return users

###########################################################################
###########################################################################
###########################################################################
###########################################################################

    def create_sell(self, _dom_id, _amount, _srok):

        print("дошло")
        self.cont.functions.create_sell( _dom_id, _amount, int(_srok)).transact()




    def delete_sell(self, _sell_id):

        self.cont.functions.delete_sell( _sell_id).transact()


    def buy(self, _sell_id, cost):

        self.cont.functions.buy(_sell_id).transact({'value': cost})

    def stop_sell(self, _sell_id):

        self.cont.functions.stop_sell(_sell_id).transact()


    def cancel_sell(self, _sell_id):  # вызывает покупаель

        self.cont.functions.cancel_sell(_sell_id).transact()

    def take_money(self, _sell_id):

        self.cont.functions.take_money(_sell_id, int(time.time())).transact()


    def sell_number(self):


        return self.cont.functions.sell_number().call()




    def check_sell(self, id_sell):


        #print(id_sell)
        return self.cont.functions.check_sell(int(id_sell)).call()



    def only_my_sell(self):

        str_my_sell = []

        for i in range(self.sell_number()):


            str_my_sell.append(self.check_sell(i))


        str2_my_sell = []


        for i in range(len(str_my_sell)):


            if str_my_sell[i][2] == self.geth.eth.defaultAccount:

                str2_my_sell.append(str_my_sell[i])


        return str2_my_sell;



    def only_my_buy(self):

        str_my_buy = []

        for i in range(self.sell_number()):


            str_my_buy.append(self.check_sell(i))


        str2_my_buy = []


        for i in range(len(str_my_buy)):


            if str_my_buy[i][3] == self.geth.eth.defaultAccount:

                str2_my_buy.append(str_my_buy[i])


        return str2_my_buy;


###########################################################################
###########################################################################
###########################################################################
###########################################################################

    def create_zalog(self, dom_id, amount, srok, srok_zalog):


        self.cont.functions.create_zalog(dom_id, amount, srok, srok_zalog).transact()


    def buy_zalog(self, id_zalog, cost):

        self.cont.functions.buy_zalog(id_zalog).transact({'value': cost})



    def take_money_for_zalog(self, id_zalog):

        print(id_zalog)
        self.cont.functions.take_money_for_zalog(id_zalog).transact()



    def return_money_for_zalog(self, id_zalog, cost):


        self.cont.functions.return_money_for_zalog(id_zalog).transact({'value': cost})



    def stop_zalog(self, id_zalog):


        self.cont.functions.stop_zalog(id_zalog).transact()



    def money_back_for_zalog(self, id_zalog):

        self.cont.functions.money_back_for_zalog(id_zalog).transact()



    def zalog_number(self):

        return self.cont.functions.zalog_number().call()


    def delete_zalog(self,id_zalog):

        self.cont.functions.delete_zalog(id_zalog).transact()


    def check_zalog(self, id_zalog):

        return self.cont.functions.check_zalog(id_zalog).call()



    def only_my_zalog(self):

        str_my_zalog = []

        for i in range(self.zalog_number()):


            str_my_zalog.append(self.check_zalog(i))


        str2_my_zalog = []


        for i in range(len(str_my_zalog)):


            if str_my_zalog[i][2] == self.geth.eth.defaultAccount:

                str2_my_zalog.append(str_my_zalog[i])


        return str2_my_zalog;




    def only_my_zalog_for_renter(self):

        str_my_zalog_for_renter = []

        for i in range(self.zalog_number()):


            str_my_zalog_for_renter.append(self.check_zalog(i))


        str2_my_zalog_for_renter = []


        for i in range(len(str_my_zalog_for_renter)):


            if str_my_zalog_for_renter[i][3] == self.geth.eth.defaultAccount:

                str2_my_zalog_for_renter.append(str_my_zalog_for_renter[i])

        #print(str2_my_zalog_for_renter)
        return str2_my_zalog_for_renter;



###########################################################################
###########################################################################
###########################################################################
###########################################################################


    def get_balance(self, user_address):


        balance = self.geth.eth.getBalance(user_address)
        print(self.geth.fromWei(balance, "ether"))

        #balance = web3.Web3.fromWei(self.geth.eth.getBalance(user_address), "ether")
        #return balance


    def auth(self, user_address, passfrase):
        user_address = web3.Web3.toChecksumAddress(str(user_address))
        log = self.geth.personal.unlockAccount(user_address, passfrase)

        return log

    def get_user(self, user_address):
        self.geth.eth.accounts.val
        user = self.cont.functions.Registration(user_address).call()
        return user
    def accounts_coin(self):
        user_address = web3.Web3.toChecksumAddress("0x15c5715f20a60ee4cb5e611e63df3c80f157a0c9")
        address_pol = web3.Web3.toChecksumAddress("0xe8842cacb018731b421d876cd57b5be67efc9f0c")
        #kol= web3.toWei(1, "ether")
        kol = 100
        #transfer = self.geth.eth.sendTransaction({from:user_address, to:address_pol, value: kol})
        # return transfer


    def poisk(self, address):
        for i in range(len(self.geth.eth.accounts)):
            if self.geth.eth.accounts[i] == address:
                return self.geth.eth.accounts[i]




post=Post()
#post.auth_check("0x59fC8D79140D5992843FFcFBd6362800d2A96e6B")
#post.autorization("0x1cc05978B0c3b0F4099F50999060FF49e40d4B39", "321")