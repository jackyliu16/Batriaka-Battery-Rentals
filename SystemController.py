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
import sys
from userAction import User, Custom, Admin, Owner
from typing import Dict, List
import time
from FeesAndOrder import Fee, Order
from Battery import _Battery
import datetime
from day import Day



# Fisrt version: only include a simple implement [No encapsulation]



class SysteController(object):
    Finished_Order: Dict[str, Order]
    Renting_Order: Dict[str, Order]
    Battery_List: List[_Battery]
    UserList: List[User]
    user_now: User
    messageBox: List[Order]
    log = Dict[str, Day]
    
    def __init__(self) -> None:
        self.user_now = None
        self.Finished_Order = []
        self.Renting_Order = []
        self.Battery_List = []
        self.UserList = []
        self.log = {}
        self.messageBox = [Order]
        
        # add somthing default battery in system
        self.Battery_List.append(_Battery('0', 'BikeBattery', 'a bike battery', 10.0, 10))
        self.Battery_List.append(_Battery('1', 'CarBattery', 'a car battery', 20.0, 5))
        # add default user to userlist
        self.UserList.append(Owner('owner', '123456'))
        self.UserList.append(Admin('admin', '123456'))
        self.UserList.append(Custom("customer", "111"))
        self.messageBox.append(Order('1', 'custom_id', "d", {self.Battery_List[0]:4, self.Battery_List[1]:5}, 23))
        self.day = Day() # init a new day ( today: it will adding to log until change to another day )

        # for all kinds of user login in loop
        while True:        
            
            # print("Loop 1")
            self.login()
            while True:
                
                # print(self.day)
                
                # check if today is a new day
                if self.day.check_if_is_today():
                    pass
                else:
                    print("innn")
                    self.log[self.day.get_today()] = self.day
                    self.day = Day() # create a new day and set it as today 
                    # self.log[self.day.get_today()] = self.day
        
                # print("LOOP 2")
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
                    
                    # log will be add in appointment
                elif action == -1:
                    # login out
                    print("you are now quit this account !!!")
                    self.user_now = None
                    break
                elif action == 3:
                    # show message
                    [print(i, self.messageBox[i]) for i in range(len(self.messageBox))]
                    # [print(f"{i}:\t", [f"{j.type} \t {self.messageBox[i].rental_Dict[j]}"for j in self.messageBox[i].rental_Dict]) for i in range(len(self.messageBox))]
                elif action == 4:
                    # delete message
                    inp = input("please input the message number you want to delete: ")
                    if inp.isdigit():
                        inp = int(inp)
                        if inp < len(self.messageBox) and inp >= 0:
                            self.day.add_log(f"{self.user_now.user_name} delete {self.messageBox[inp]}")
                            self.messageBox.pop(int(inp))
                        else:
                            print("the index not existed so it couldn't been delete! ")
                    else:
                        print("you should input a number !!!")
                elif action == 5:
                    # transmit message to order
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
                        # if all need could be satisfy (delete inventory)
                        for key in order.rental_Dict:
                            key.number_now -= order.rental_Dict[key]
                            # print(key.number_now)
                        self.day.add_log(f"{self.user_now.user_name} transimt message {inp} : {order.print_name_and_number()} to order")
                        self.messageBox.remove(order)
                        self.Renting_Order.append(order)
                elif action == 6:
                    print("you are now go into a process which will adding a battery inside to list!")
                    print("there are 3 things you have to input\n\tthe type of battery,\n\tthe detail inforamtionof it, \n\tthe price, and also the number(default=0)")
                    # _Battery(id, type, detail, price)
                    
                    type_in = input("please input type of the battery:\t" )
                    while type_in == "" :
                        type_in = input("please input type of the battery:\t" )
                    
                    detail = input("please input the detail information of battery:\t")
                    while detail == "":
                        detail = input("please input the detail information of battery:\t")

                    price = input("please input the price of battery:\t")
                    while not price.isdigit() :
                        price = input("please reinput price, which is because you input error message!!!:\t")
                        
                    print("if you want to input number of the battery now, you can just do it(only one changes)")
                    number = input("please input the number of battery: ")
                    
                    self.day.add_log(f"{self.user_now.user_name} add Battery {type_in},{detail}, {price}, {number}")
                    self.Battery_List.append(_Battery("1", type_in, detail, price, number))
                elif action == 7:
                    # basicalon pricinple we believe that number of battery only could change by owner 
                    print("you are now changing the information of battery")
                    print("""
                          please select a Battery you want to change
                          """)    
                    for index in range(len(self.Battery_List)):
                        print("\t", index, self.Battery_List[index].type, end="\n")
                    
                    inp = int(input("select a number of Battery: "))
                    while inp < 0 or inp > len(self.Battery_List):
                        inp = int(input("select a number of Battery: "))

                    print("""\t\tselect a attribute:
            \t1.type
            \t2.detail
            \t3.price
                          """)

                    inp2 = int(input("select a attriabute you want to change: "))
                    while inp2 not in [1,2,3]:
                        inp2 = int(input("select a attriabute you want to change: "))

                    inp3 = input("please input what you want to change to: ")
                    while inp2 == 3 and not inp3.isdigit():
                        inp3 = input("please input what you want to change to: ")
                    if inp2 == 3 :
                        inp3 = int(inp3)

                    type_map = {1: "type", 2: 'detail', 3:'price'}
                    self.day.add_log(f"{self.user_now.user_name} repleace {self.Battery_List[inp].print_name()}'s {type_map[inp2]} from '{self.Battery_List[index].__getattribute__(type_map[inp2])}' to '{inp3}'")
                    battery = self.Battery_List[inp]
                    if inp2 == 1:
                        battery.__setattr__('type', inp3)
                    elif inp2 == 2:
                        battery.__setattr__('detail', inp3)
                    elif inp2 == 3:
                        battery.__setattr__('price', inp3)
                    # elif inp2 == 4:
                    #     battery.__setattr__('number_now', inp3)                                            
                elif action == 8:
                    print("you are now deleting battery")
                    print("""
                          please select a Battery you want to change
                          """)    
                    for index in range(len(self.Battery_List)):
                        print("\t", index, self.Battery_List[index].type, end="\n")
                    
                    inp = input("please input a battery you want to delete: (if you don't want to detect everything just blanked it):")    
                    while not inp == "" and not inp.isdigit():
                        inp = input("please input a battery you want to delete: (if you don't want to detect everything just blanked it):")    
                    inp = int(inp)
                    
                    
                    # log information
                    self.day.add_log(f"{self.user_now} remove {self.Battery_List[inp].print_name()}")
                    self.Battery_List.pop(inp)
                    print("finish remove battery!")
                elif action == 9:
                    for i in range(len(self.Renting_Order)):
                        print(i, self.Renting_Order[i])
                elif action == 10:
                    # checkout order
        
                    for item in self.Renting_Order:
                        print(item)
                    
                    inp = int(input("please input the number of order you want to transmit!:>"))
                    if inp < 0 or inp >= len(self.Renting_Order):
                        print("ERROR: index out of bround!!!")
                    else:
                        order:Order = self.Renting_Order[inp]
                        # if all need could be satisfy
                        for key in order.rental_Dict:
                            key.number_now += order.rental_Dict[key]
                        print(order)
                        order.rental_end_time = datetime.datetime.now()
                        self.Renting_Order.remove(order)
                        self.Finished_Order.append(order)
                elif action == 11:
                    # show log information
                    for day in self.log:
                        print(day)
                    print(self.day)
                elif action == 12:
                    self.register('admin')
                elif action == 13:
                    print(self.day)
                elif action == 14:
                    # see staff information
                    for user in self.UserList:
                        if isinstance(user, Admin) and not isinstance(user, Owner):
                            print(user.user_name, end=" ")
                elif action == 15:
                    # make request of new battries
                    # this part is basical as same as change information 
                    print("which kind of battery will be add? ")
                    inp = input("please input a number: >")
                    while not inp.isdigit() or (int(inp) < 0 or int(inp) >= len(self.Battery_List)):
                        inp = input("please input a number again: >")
                    inp = int(inp)
                
                    inp2 = input("please input how many battery you want to add:")
                    while not inp2.isdigit():
                        inp2 = input("please input how many battery you want to add:")
                    
                    self.Battery_List[int(inp)].__setattr__("number_now", self.Battery_List[int(inp)].number_now+int(inp2))
                else:
                    # if action not in [user.user_name for user in self.UserList]:
                    #     pass
                    # else:
                    # [print(user.usee_name) for user in self.UserList]
                    for user in self.UserList:
                        if user.user_name == action:
                            self.appointment(user)
                
    def show_inventory(self):
        print("="*30)
        [print(i) for i in self.Battery_List]
        print("="*30)
        
       
    def login(self):
        print("welcome using Batriaka Battery Rentals System")
        print("please input your name and your passwd, if you want to register(custom) just leave a blank")

        while True:
            user_name = input("user name:")
            user_passwd = input("user passwd:")
            if user_name.upper() == 'QUIT' or user_passwd.upper() == "QUIT":
                sys.exit(0)  
            elif user_name == "" and user_passwd == "":
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
       
    # def get_num():
        
     
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
                 
        if inp == "" or inp2 == "":
            return 
        
        print("lead me recheck your appointment:")
        print("="*30)
        [print(i.type, rental_Dict[i]) for i in rental_Dict]
        print("="*30)


        inp3 = input("how many days you want to rent it ? (a days == 1)")
        while ( int(inp3) < 0 and int(inp3) >= 30 ) or not inp3.isdigit() :
            inp3 = input("how many days you want to rent it ? (a days == 1)")
        
        inp3 = int(inp3)
        print("your message is allready been sent!!! please wait for admin")
        self.messageBox.append(Order("1", user, None, rental_Dict, inp3))
    
if __name__ == "__main__":
    controller = SysteController()

    

