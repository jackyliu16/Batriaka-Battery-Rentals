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
    messageBox: List[Order]
    def __init__(self) -> None:
        self.user_now = None
        self.Finished_Order = []
        self.Renting_Order = []
        self.Battery_List = []
        self.UserList = []
        self.messageBox = [Order]
        
        # add somthing default battery in system
        self.Battery_List.append(_Battery('0', 'BikeBattery', 'a bike battery', 10.0, 10))
        self.Battery_List.append(_Battery('1', 'CarBattery', 'a car battery', 20.0, 5))
        # add default user to userlist
        self.UserList.append(Owner('owner', '123456'))
        self.UserList.append(Admin('admin', '123456'))
        self.UserList.append(Custom("customer", "111"))
        self.messageBox.append(Order('1', 'custom_id', "d", {self.Battery_List[0]:4, self.Battery_List[1]:5}, 23))

        # for all kinds of user login in loop
        while True:        
            print("Loop 1")
            self.login()
            while True:
                print("LOOP 2")
                assert self.user_now is not None
                self.user_now.show_action()
                inp = input("please input your choice:>")
                action = self.user_now.perform_action(inp)
                # action = self.user_now.perform_action(input("\:>"))
                
                # some of action will infact here so there is a kind of action return, and it will be change here
                if action == 1:
                    self.show_inventory()
                elif action == 2:
                    assert self.user_now is not None
                    self.appointment(self.user_now)
                elif action == -1:
                    print("you are now quit this account !!!")
                    self.user_now = None
                    break
                elif action == 3:
                    # show message
                    [print(i, self.messageBox[i]) for i in range(len(self.messageBox))]
                    # [print(f"{i}:\t", [f"{j.type} \t {self.messageBox[i].rental_Dict[j]}"for j in self.messageBox[i].rental_Dict]) for i in range(len(self.messageBox))]
                elif action == 4:
                    # delete message
                    inp = int(input("please input the message number you want to delete: "))
                    if inp < len(self.messageBox):
                        self.messageBox.pop(int(inp))
                    else:
                        print("the index not existed so it couldn't been delete! ")
                elif action == 5:
                    inp = int(input("please input the number of order you want to transmit!:>"))
                    if inp < 0 or inp > len(self.messageBox):
                        print("ERROR: index out of bround!!!")
                    else:
                        order:Order = self.messageBox[inp]
                        for i, v in order.rental_Dict.items():
                            if i.number_now < v:
                                # if there is one things will not match
                                print("Error: because out of inventory! ")
                                break
                        # if all need could be satisfy
                        for key in order.rental_Dict:
                            key.number_now -= order.rental_Dict[key]
                            print(key.number_now)
                        self.messageBox.remove(order)
                        self.Renting_Order.append(order)
                else:
                    # if action not in [user.user_name for user in self.UserList]:
                    #     pass
                    # else:
                    for user in self.UserList:
                        if user.user_name == action:
                            self.appointment(action)
                
    def show_inventory(self):
        [print(i) for i in self.Battery_List]
        
       
    def login(self):
        print("welcome using Batriaka Battery Rentals System")
        print("please input your name and your passwd, if you want to register(custom) just leave a blank")

        while True:
            user_name = input("user name:")
            user_passwd = input("user passwd:")
            if user_name == "" and user_passwd == "":
                self.register("customer")
            else:
                for user in self.UserList:
                    if user_name == user.user_name:
                        if user.login_in_check(user_passwd):
                            self.user_now = user
                            break
            if self.user_now is not None:
                break
                        
    def register(self, userType:str):
        print(f"how you are trying to register a new {userType} account!")
        # print(f'how you are trying to register a new {"customer" if isinstance(userType, Custom) else "Admin"} account!')
        user_name = input("please input user name: ")
        user_password = input("please input password: ")
        # user_create = userType(user_name, user_password)
        if userType == "customer":
            user_create = Custom(user_name, user_password)
        elif userType == "admin":
            user_create = Admin(user_name, user_password)
        self.UserList.append(user_create)
        
    #TODO improved coupling and module independence
    #TODO the ways of update need to be change
    def appointment(self, user:User):
        print(f"you are now appointment for {user.user_name}") 
        print("please input the need of your battery type! (one's at the time)")
        
        [print(f'{i}:\t{self.Battery_List[i]}') for i in range(len(self.Battery_List))]
        
        rental_Dict = {}
        
        while input("do you want to end of your select?('y')").upper() != 'Y' :
            
            inp = input("please input your select of battery:>")
            while inp not in [f'{i}' for i in range(0, len(self.Battery_List))]:
                inp = input("please input your select of battery:>")
            
            print(f"you are now select \n{self.Battery_List[int(inp)]}, \nhow many did you want to pick? ")
            inp2 = input("please input how many you want to select:>")
            while not inp2.isdigit():
                inp2 = input("please input how many you want to select:>")
                
            inp2 = int(inp2)
            
            
            if self.Battery_List[int(inp)].number_now >= inp2:
                rental_Dict[self.Battery_List[int(inp)]] = inp2
                print("record")
            else:
                print("you reserve too many modules and cannot meet them") 
        
        print("lead me recheck your appointment:")
        print("="*30)
        [print(i.type, rental_Dict[i]) for i in rental_Dict]
        print("="*30)


        inp3 = int(input("how many days you want to rent it ? (a days == 1)"))
        while inp3 < 0 and inp3 >= 30:
            inp3 = int(input("how many days you want to rent it ? (a days == 1)"))
        
        print("your message is allready been sent!!! please wait for admin")
        self.messageBox.append(Order("1", user, None, rental_Dict, inp3))
    
if __name__ == "__main__":
    controller = SysteController()

    

