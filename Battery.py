#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
"""
@File   : Battery.py
@Time   : 2022/07/04 10:01:45
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
"""

#IMPORT LIB

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
        return f"type:{self.type}  \tprice:{self.price}\tnumber:{self.number_now}\ndetail:\t{self.detail}"

    def information_print():
        return f"type:{self.type}\tprice:{self.price}\tnumber:{self.number_now}"