# -*- coding: utf-8 -*-
import time
import sys
from threading import Thread
from delete2 import Post


from PyQt5 import QtCore, QtGui, QtWidgets

post = Post()



class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, srok, ui, type, id, ex):
        """Инициализация потока"""
        Thread.__init__(self)
        self.srok = srok
        self.ui = ui
        self.id = id
        self.type = type
        self.ex = ex

    def run(self):


        if self.type == "Оповещение":

            print("sdjsjs")
            time.sleep(5)
            self.ui.label_48.clear()

        if self.type == "Обновление":

            while 1:

                print(self.ui.label_79.text())
                post.geth.eth.defaultAccount = self.ui.label_79.text()
                print(post.geth.eth.defaultAccount)
                time.sleep(10)
                post.obnov(self.ui)
                print("Обновление прошло")


        if self.type == "Срок":
            i = self.ex
            while 1:

                post.set_srok(self.id, i)
                time.sleep(10)
                i = i + 1




        if self.type=="залог":
            time.sleep(self.srok * 10)
            self.ui.label_48.setText("Срок залога №" + str(self.id) + " " + "истек")
            post.delete_zalog(self.id)
            time.sleep(10)
            self.ui.label_48.clear()


        if self.type=="залога":
            time.sleep(self.srok * 10)



            if str(post.check_dom(int(post.check_zalog(self.id - 1)[1]))[2]) == "False":

                self.ui.label_48.setText("Срок предложения " + self.type + " №" + str(self.id - 1) + " " + "истек")
                post.delete_zalog(self.id - 1 )
                time.sleep(10)
                self.ui.label_48.clear()


        if self.type=="продажи":
            time.sleep(self.srok * 10)
            self.ui.label_48.setText("Срок предложения " + self.type +" №" + str(self.id - 1 ) + " " + "истек")
            post.delete_sell(self.id - 1 )
            time.sleep(10)
            self.ui.label_48.clear()


        if self.type=="дарения":
            time.sleep(self.srok * 10)
            self.ui.label_48.setText("Срок предложения " + self.type +" №" + str(self.id -1 ) + " " + "истек")
            post.delete_dar(self.id -1 )
            time.sleep(10)
            self.ui.label_48.clear()

        print("kkkk")





def create_threads(srok, ui, type, id, ex=1):
    """
    Создаем группу потоков
    """

    print("pered_start")
    my_thread = MyThread(srok, ui, type, id, ex)
    print("start")
    my_thread.start()






