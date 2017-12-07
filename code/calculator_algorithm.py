# -*- coding: UTF-8 -*-
"""
author NorwegianForest
计算器算法
输入一串运算式，运算符前后由空格隔开
返回运算结果
支持加减乘除和括号运算
"""

from collections import deque
from decimal import Decimal


def single_calculate(num1, num2, operator):
    """
    单次运算
    :param num1: 操作数1
    :param num2: 操作数2
    :param operator: 运算符
    :return: 运算结果
    """
    # num1的格式为Decimal('num1')
    num1 = Decimal(num1)
    num2 = Decimal(num2)
    # 用str返回只有数字的字符串
    if operator == "+":
        return str(num2 + num1)
    elif operator == "-":
        return str(num2 - num1)
    elif operator == "*":
        return str(num2 * num1)
    elif operator == "/":
        if str(num1) == "0":
            return "ERROR"
        return str(num2 / num1)


def formula_calculate(formula):
    """
    算式运算
    :param formula: 算式字符串，运算符前后由空格隔开
    :return: 运算结果
    """
    formula = formula.split()
    formula = deque(formula)
    number_stack = []
    operator_stack = []

    while 1:
        if len(formula) != 0:
            unknow = formula.popleft()
            # 队列输入的是运算符
            if unknow == "+" or unknow == "-" or unknow == "*" or unknow == "/":
                # 运算符堆栈为空
                if len(operator_stack) == 0:
                    operator_stack.append(unknow)
                # 运算符优先级高于栈顶运算符
                elif (unknow == "*" or unknow == "/") and (operator_stack[-1] == "+" or operator_stack[-1] == "-"):
                    operator_stack.append(unknow)
                # 栈顶为左括号时，相当于运算符堆栈为空，一律入栈
                elif operator_stack[-1] == "(":
                    operator_stack.append(unknow)
                # 无需入栈，直接计算
                else:
                    # 将运算符返回队列，以便下一次循环
                    formula.appendleft(unknow)
                    number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_stack.pop()))
                    if number_stack[-1] == "ERROR":
                        break
            # 左括号一律入栈
            elif unknow == "(":
                operator_stack.append(unknow)
            elif unknow == ")":
                operator_top = operator_stack.pop()
                # 运算符栈顶非左括号则进行计算
                if operator_top != "(":
                    number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_top))
                    if number_stack[-1] == "ERROR":
                        break
                    formula.appendleft(unknow)
            # 非符号则为数字
            else:
                number_stack.append(unknow)
        # 队列输入完毕，进行最后一次运算
        else:
            number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_stack.pop()))
            if number_stack[-1] == "ERROR":
                break
            # 运算符堆栈清空，退出循环
            if len(operator_stack) == 0:
                break
    return number_stack.pop()

