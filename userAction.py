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
from SystemController import SysteController


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

    #TODO improved coupling and module independence
    #TODO the ways of update need to be change
    @staticmethod        
    def appointment(self):
        print(f"you are now appointment for {self.user_name}") 
        print("please input the need of your battery type! (one's)")
        
        [print(f'{i}.{controller().Battery_List[i]}') for i in range(len(controller().Battery_List))]
        
        while input("do you want to end of your select?") :
            
            inp = input(":>")
            while inp not in [f'{i}' for i in range(0, len(controller().Battery_List))]:
                inp = input(":>")
            
            print(f"you have select {controller().Battery_Dict[int(inp)]}, how many did you want to pick? ")
            
            inp2 = input(":>")
            while not inp2.isdigit():
                inp2 = input(":>")
                
            inp2 = int(inp2)
            rental_list = {}
            
            if controller().Battery_List[int(inp)].number_now >= inp2:
                rental_list[controller().Battery_Dict[int(inp)]] = inp2
            else:
                print("you reserve too many modules and cannot meet them") 
        
            print
            inp3 = int(input("how many days you want to rent it ? a days == 1, a month == 30"))
            while inp3 < 0 and inp3 >= 30:
                inp3 = int(input("how many days you want to rent it ? a days == 1, a month == 30"))
        
        
        controller().messageBox.append(Order("1", self.id, None, rental_list, inp3))
    

class Custom(User):
    Current_Order: List[str] # the primary key of Order
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def appointment_for_they(self, inp):
        pass
    
    def perform_action(self, inp):
        if inp == "1":
            self.appointment(self)
        elif inp == "2":
            return 1 # show inventory
    
    def show_action(self):
        print("""
              \t1.appointment
              \t2.show inventory        
              """)
        pass

class Admin(User):
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def appointment_for_they(self):
        #TODO give a appointment in system 
        pass
    
    def show_action(self):
        #TODO finish action show 
        pass
    
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


    
    