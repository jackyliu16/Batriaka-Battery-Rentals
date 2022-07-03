#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
'''
@File   : userAction.py
@Time   : 2022/06/30 13:27:02
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
'''


# IMPORT LIB
import abc
from typing import List

class User(object):
    user_name: str
    __user_passwd: str

    def __init__(self, user_name: str, user_passwd: str) -> None:
        self.user_name = user_name
        self.__pass_word = user_passwd

    def login_in_check(self, passwd: str) -> bool:
        return self.__pass_word == passwd

    def check_inventory():
        # TODO finish inventory show 
        pass
    
    def login_out():
        #TODO finish login out
        pass
   
    @abc.abstractmethod
    def show_action(self):
        """
        show what kinds of action could they do
        """
        # TODO show_and_action
        pass
    
    @abc.abstractmethod
    def perform_action(self, inp):
        #TODO finish perform action
        pass


class Custom(User):
    Current_Order: List[str] # the primary key of Order
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def appointment_for_they(self):
        #TODO give a appointment in system 
        pass

class Admin(User):
    
    def __init__(self, user_name, user_passwd):
        super().__init__(user_name, user_passwd)
    
    def appointment(custom_id: str):
        #TODO finish appointment
        pass
    
class Owner(Admin):
    
    # he wasn't having any kind of password or other things, was the only things in the project
    
    def display_information():
        #TODO finish the detail of this battery rent enterprise
        pass

    def add_admin(name, passwd):
        #TODO create a admin user and add it to the list
        pass

    

        


