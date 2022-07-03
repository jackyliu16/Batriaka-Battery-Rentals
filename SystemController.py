#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
"""
@File   : SystemController.py
@Time   : 2022/06/30 13:45:44
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
"""

#IMPORT LIB
from userAction import *
import abc
from abc import abstractclassmethod, abstractmethod
from typing import Dict, List
import time


# Fisrt version: only include a simple implement [No encapsulation]

class _Battery(object):
    id: str
    type: str
    detail: str
    price: float
    number_now: int

    def __init__(self, id:str, type:str, detail:str, price:float, nember_now:int=0) -> None:
        self.id = id
        self.type = type
        self.detail = detail
        self.price = price
        self.number_now = nember_now
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"type:{self.type}\ndetail:\t{self.detail}"

class Fee(metaclass=abc.ABCMeta):
    limitation: List[int] # was a list of int of each battery
    rate: float

    @abc.abstractmethod
    def calculate(self):
        pass

class default_Fee(Fee):
    def __init__(self) -> None:
        global controller
        self.limitation = [100 for _ in controller.Battery_List]
        self.rate = 1

class Order(object):
    id:str
    custom_id: str
    admin_id: str
    rental_list: Dict[str, int] # the first str is the id of battery
    rental_start_time: time
    rental_end_time: time
    rental_theory_end_time: time
    order_fees_model: Fee

    def __init__(self, id:str, custom_id:str, admin_id:str, rental_list: Dict[str, int], tenancy_term) -> None:
        self.id = id
        self.custom_id = custom_id
        self.admin_id = admin_id
        self.rental_list = rental_list
        self.rental_start_time = time.time()
        self.rental_end_time = None
        # TODO finish the calucate of tenancy to rental_end_time 
        # self.rental_theory_end_time = self.rental_start_time + 

class SysteController(object):
    Finished_Order: Dict[str, Order]
    Renting_Order: Dict[str, Order]
    Battery_Dict: List[_Battery]
    UserList: List[User]
    user_now: User
    def __init__(self) -> None:
        self.Finished_Order = {}
        self.Renting_Order = {}
        self.Battery_Dict = []
        self.UserList = []
        
        # add somthing default battery in system
        self.Battery_Dict.append(_Battery('0', 'BikeBattery', 'a bike battery', 10.0, 10))
        self.Battery_Dict.append(_Battery('1', 'CarBattery', 'a car battery', 20.0, 5))
        # add default user to userlist
        self.UserList.append(Owner('owner', '123456'))
        self.UserList.append(Admin('admin', '123456'))

        # for all kinds of user login in loop
        while True:        
            self.login()
            while True:
                assert self.user_now is not None
                self.user_now.show_action()
                action = self.user_now.perform_action(input("\:>"))
                
                # some of action will infact here so there is a kind of action return, and it will be change here
                                             
    
       
    def login(self):
        print("welcome using Batriaka Battery Rentals System")
        print("please input your name and your passwd, if you want to register(custom) just leave a blank")

        while True:
            user_name = input("user name:")
            user_passwd = input("user passwd:")
            if user_name is None or user_passwd is None:
                self.register(Custom)
            else:
                for user in self.UserList:
                    if user_name == user.user_name:
                        if user.login_in_check(user_passwd):
                            self.user_now = user
                            break
            if self.user_now is not None:
                break
                        
    def register(userType:User):
        print(f'how you are trying to register a new {"customer" if isinstance(userType, Custom) else "Admin"} account!')
        user_name = input("please input user name: ")
        user_password = input("please input password: ")
        user_create = userType(user_name, user_password)
        self.UserList.append(user_create)
    
        
if __name__ == "__main__":
    controller = SysteController()

    isinstance(obj, class_or_tuple)

