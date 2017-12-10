# -*- coding: UTF-8 -*-
"""
create date 20171210
author NorwegianForest
"""


class MyList:
    list = []

    def __init__(self, init_list):
        self.list = init_list

    def set(self, set_list):
        self.list = set_list

    def append(self, append_str):
        self.list.append(append_str)

    def getjoinvalue(self):
        return "".join(self.list)

    def print(self):
        print(self.list)