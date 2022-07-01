# !/usr/bin/env python
# -*- encoding: utf-8 -*- 
'''
@File   : main.py
@Time   : 2022/06/30 13:27:10
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
'''

# IMPORT LIB


if __name__ == "__main__":

    print("Welcome to the management system!")
    print("please input a number to select and login in your User group")
    print("\t1. Custom\n\t2. Admin\n\t3. Owners")
    number = input(":\>")
    while number not in ['1', '2', '3', '4']:
        number = input(">")
