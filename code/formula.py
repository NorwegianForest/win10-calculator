# -*- coding: UTF-8 -*-
"""
create date 20171210
author NorwegianForest
"""
from code import mylist


class Formula(mylist.MyList):
    def getspacevalue(self):
        return " ".join(self.list)
