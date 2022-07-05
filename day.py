#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
"""
@File   : Day.py
@Time   : 2022/07/05 10:16:38
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1. https://www.w3school.com.cn/python/python_datetime.asp
    2.
"""

#IMPORT LIB

from typing import *
import datetime
class Day(object):
    distinguish: str
    record: List[str]
    
    def __init__(self):
        self.distinguish = datetime.datetime.now().strftime("%x")
        self.fullinformation = []
        self.record = []
    
    def get_today(self) -> str:
        return self.distinguish
    
    def add_log(self, information:str):
        self.fullinformation.append(datetime.datetime.now())
        self.record.append(information)
    
    def check_if_is_today(self):
        return datetime.datetime.now().strftime("%x") == self.distinguish
    
    def __str__(self):
        print("="*48+"-LOG-"+"="*47)
        [print("\t", self.fullinformation[i], self.record[i]) for i in range(len(self.record))]
        print("="*100)
        return ""
        # return f"[log of {self.distinguish}]" + str([print("\t", self.fullinformation[i], self.record[i]) for i in range(len(self.record)) ])
    
if __name__ == "__main__":
    Day1 = Day()
    print(type(Day1.distinguish))
    Day1.add_log("information")
    Day1.add_log("information2")
    print(Day1)