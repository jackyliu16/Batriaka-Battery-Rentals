#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
'''
@File   : userAction.py
@Time   : 2022/06/30 13:27:02
@Author : jackyLiu
@version: 1.0
@Contact: 18922251299@163.com
@reference: 
    1.
    2.
'''


# IMPORT LIB

class User(object):
    user_name: str
    __user_passwd: str

    def __init__(self, user_name: str, user_passwd: str) -> None:
        self.user_name = user_name
        self.__pass_word = user_passwd

    def login_in_check(self, passwd: str) -> bool:
        return self.__pass_word == passwd


class Custom(User):



