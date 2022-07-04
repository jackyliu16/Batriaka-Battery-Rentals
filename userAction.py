#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
'''
@File   : userAction.py
@Time   : 2022/06/30 13:27:02
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1. how to using a variable in other module https://blog.csdn.net/weixin_42444172/article/details/124043875
    2.
'''


# IMPORT LIB
import abc
from typing import List
from FeesAndOrder import Order

class User(object):
    user_name: str
    __user_passwd: str

    def __init__(self, user_name: str, user_passwd: str) -> None:
        self.user_name = user_name
        self.__pass_word = user_passwd

    def login_in_check(self, passwd: str) -> bool:
        return self.__pass_word == passwd

    @staticmethod
    def check_inventory():
        return 1
        # global controller
        # because it couldn't been use so we using return value make it possibility
    
    @staticmethod
    def login_out():
        #TODO finish login out
        return 2
   
    @abc.abstractmethod
    def show_action(self):
        """
        show what kinds of action could they do
        """
        pass
    
    @abc.abstractmethod
    def perform_action(self, inp):
        #TODO finish perform action
        pass


    

class Custom(User):
    Current_Order: List[str] # the primary key of Order
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def appointment_for_they(self, inp):
        pass
    
    def perform_action(self, inp):
        if inp == "1":
            return 2
        elif inp == "2":
            return 1 # show inventory
        elif inp == "0":
            return -1
    
    def show_action(self):
        print("""
              \t1.appointment
              \t2.show inventory        
              \t0.login out
              """)
        pass

class Admin(User):
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def perform_action(self, inp):
        if inp == '1':
            inp = input("please input customer name: >")
            return user_name 
        elif inp == '2':return 1 
        elif inp == "3":return 3
        elif inp == "4":return 4
        elif inp == "5":return 5
        elif inp == "6":return 6
        elif inp == "7":return 7
        elif inp == "8":return 8
        elif inp == "9":return 9
        elif inp == "10":return 10
        elif inp == '0':return -1
              
    def show_action(self):
        print("""
              1. appointment
              2. show inventory 
              3. see message
              4. delete message
              5. transmit message
              6. add battery
              7. change battery information
              8. delete battery
              9. show Renting order
              10. checkout order
              0. quit ac count
              """)
    
class Owner(Admin):
    
    # he wasn't having any kind of password or other things, was the only things in the project
    
    def display_information():
        #TODO finish the detail of this battery rent enterprise
        pass

    def add_admin(name, passwd):
        #TODO create a admin user and add it to the list
        pass

    def appointment_for_they(self):
        #TODO give a appointment in system 
        pass
    
    def show_action(self):
        #TODO finish action show 
        pass


    
    