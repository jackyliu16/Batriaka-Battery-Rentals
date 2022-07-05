#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
"""
@File   : FeesAndOrder.py
@Time   : 2022/07/04 10:01:31
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
"""

#IMPORT LIB
import abc
from typing import *
import time
from Battery import _Battery
import datetime

class Fee(metaclass=abc.ABCMeta):
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
    rental_Dict: Dict[_Battery, int] 
    rental_start_time: time
    rental_end_time: time
    rental_theory_end_time: time
    order_fees_model: Fee

    def __init__(self, id:str, custom_id:str, admin_id:str, rental_list: Dict[str, int], tenancy_term) -> None:
        self.id = id
        self.custom_id = custom_id
        self.admin_id = admin_id
        self.rental_Dict = rental_list
        self.rental_start_time = datetime.datetime.now() 
        self.rental_end_time = None
        # TODO finish the calucate of tenancy to rental_end_time 
        self.rental_theory_end_time = self.rental_start_time + datetime.timedelta(days=tenancy_term) 
        
    def __str__(self):
        # it seem we chouldn't using \t here
        return str([f"{i.type}   {self.rental_Dict[i]}" for i in self.rental_Dict])
    
    def print_name_and_number(self):
        s = "{"
        for i in self.rental_Dict.keys():
            s += str(i.type)
            s += ":" + str(self.rental_Dict[i]) + ",  "
        return s + "}"