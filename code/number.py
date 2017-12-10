# -*- coding: UTF-8 -*-
"""
create date 20171210
author NorwegianForest
"""
from code import mylist


class Number(mylist.MyList):
    isnegative = 0

    def append(self, append_str):
        if append_str == ".":
            if "." in self.list:
                pass
            else:
                self.list.append(".")
        elif append_str == "±":
            if self.isnegative == 0:
                newlist = []
                newlist = ["-"] + self.list
                self.list = newlist
                self.isnegative = 1
            else:
                del self.list[0]
                self.isnegative = 0
        else:
            if len(self.list) == 1 and self.list[0] == "0":
                self.list.pop()
            self.list.append(append_str)

    def backspace(self):
        if len(self.list) == 1 and self.list[0] == "0":
            pass
        elif len(self.list) == 1:
            self.list = ["0"]
        else:
            self.list.pop()
