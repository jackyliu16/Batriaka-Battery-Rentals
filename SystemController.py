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
from typing import Dict, List
import time
import pickle

class _Battery(object):
    _specification: str
    _price: int
    number: int

    def __init__(self, name:str, describes:str, price:int, number:int)->None:
        self._class_name = name
        self._specification = describes
        self._price = price
        self._number = number

    def __str__(self):
        #TODO make it as desc battery information
        pass

    def set_class_name(self, class_name:str)->None:
        self._class_name = class_name
    def set_specification(self, specification:str)->None:
        self._specification = specification

    def set_price(self, price:int)->None:
        self._price = price
    def set_number(self, number)->None:
        self._number = number

    def get_class_name(self)->str:
        return self._class_name
    def get_specification(self)->str:
        return self._specification
    def get_price(self)->int:
        return self._price
    def get_number(self)->int:
        return self._number


class Orders(object):
    id:str
    rental_list: Dict[_Battery, int]
    rental_start_time:time
    rental_end_time:time
    rental_theory_end_time:time
    order_fees:int


class Controller(object):
    Finished_Order: List[Orders]
    Renting_Order: List[Orders]

    def __init__(self):
        with open("Finish_Order.obj", 'w') as File:
            self.Finished_Order = pickle.load(File)
        with open("Renting_Order.obj", 'w') as File:
            self.Renting_Order  = pickle.load(File)

    def find_item(self, name:str) -> Orders:
        pass

    def change_item(self, item:Orders, attr_name:str, to):
        pass

