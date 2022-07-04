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
from userAction import User, Custom, Admin, Owner
from typing import Dict, List
import time
from FeesAndOrder import Fee, Order
from Battery import _Battery



# Fisrt version: only include a simple implement [No encapsulation]



class SysteController(object):
    Finished_Order: Dict[str, Order]
    Renting_Order: Dict[str, Order]
    Battery_List: List[_Battery]
    UserList: List[User]
    user_now: User
    def __init__(self) -> None:
        self.user_now = None
        self.Finished_Order = {}
        self.Renting_Order = {}
        self.Battery_List = []
        self.UserList = []
        self.messageBox = []
        
        # add somthing default battery in system
        self.Battery_List.append(_Battery('0', 'BikeBattery', 'a bike battery', 10.0, 10))
        self.Battery_List.append(_Battery('1', 'CarBattery', 'a car battery', 20.0, 5))
        # add default user to userlist
        self.UserList.append(Owner('owner', '123456'))
        self.UserList.append(Admin('admin', '123456'))
        self.UserList.append(Custom("customer", "111"))

        # for all kinds of user login in loop
        while True:        
            self.login()
            while True:
                assert self.user_now is not None
                self.user_now.show_action()
                action = self.user_now.perform_action(input("\:>"))
                
                # some of action will infact here so there is a kind of action return, and it will be change here
                if action == 1:
                    self.show_inventory()
                elif action == 2:
                    # login out
                    self.user_now = None
                    break
                
    def get_Battery_List(self):
        return self.Battery_List            
                                             
    def show_inventory(self):
        [print(i) for i in self.Battery_List]
        
       
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
    
def global_var():
    global controller
    return controller
        
if __name__ == "__main__":
    controller = SysteController()

    

