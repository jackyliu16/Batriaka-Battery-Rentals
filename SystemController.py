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
from abc import abstractclassmethod, abstractmethod
from typing import Dict, List
import time
import abc
import pickle

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

    def __init__(self) -> None:
        self.Finished_Order = {}
        self.Renting_Order = {}
        self.Battery_Dict = []

        # adding something inside 
        self.Battery_Dict.append(_Battery('0', 'BikeBattery', 'a bike battery', 10.0, 10))
        self.Battery_Dict.append(_Battery('1', 'CarBattery', 'a car battery', 20.0, 5))

        [print(i) for i in self.Battery_Dict]

if __name__ == "__main__":
    controller = SysteController()


