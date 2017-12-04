#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import deque
from decimal import Decimal


def single_calculate(num1, num2, operator):
    # num1的格式为Decimal('num1')
    num1 = Decimal(num1)
    num2 = Decimal(num2)
    if operator == "+":
        return str(num2 + num1)  # 用str返回只有数字的字符串
    elif operator == "-":
        return str(num2 - num1)
    elif operator == "*":
        return str(num2 * num1)
    elif operator == "/":
        if str(num1) == "0":
            return "ERROR"
        return str(num2 / num1)


def formula_calculate(formula):
    formula = formula.split()  # 根据空格分开
    formula = deque(formula)  # 创建队列
    number_stack = []
    operator_stack = []

    while 1:
        if len(formula) != 0:
            unknow = formula.popleft()
            if unknow == "+" or unknow == "-" or unknow == "*" or unknow == "/":  # 队列输入的是运算符
                if len(operator_stack) == 0:  # 运算符堆栈为空
                    operator_stack.append(unknow)
                # 运算符优先级高于栈顶运算符
                elif (unknow == "*" or unknow == "/") and (operator_stack[-1] == "+" or operator_stack[-1] == "-"):
                    operator_stack.append(unknow)
                elif operator_stack[-1] == "(":  # 栈顶为左括号时，相当于运算符堆栈为空，一律入栈
                    operator_stack.append(unknow)
                else:  # 无需入栈，直接计算
                    formula.appendleft(unknow)  # 将运算符返回队列，以便下一次循环
                    number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_stack.pop()))
                    if number_stack[-1] == "ERROR":
                        break  # 错误检测
            elif unknow == "(":  # 左括号一律入栈
                operator_stack.append(unknow)
            elif unknow == ")":
                operator_top = operator_stack.pop()
                if operator_top != "(":  # 运算符栈顶非左括号则进行计算
                    number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_top))
                    if number_stack[-1] == "ERROR":
                        break
                    formula.appendleft(unknow)
            else:  # 非符号则为数字
                number_stack.append(unknow)
        else:  # 队列输入完毕，进行最后一次运算
            number_stack.append(single_calculate(number_stack.pop(), number_stack.pop(), operator_stack.pop()))
            if number_stack[-1] == "ERROR":
                break
            if len(operator_stack) == 0:  # 运算符堆栈清空，退出循环
                break
    return number_stack.pop()

