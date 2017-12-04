from PythonApplication1 import calculator_algorithm
from tkinter import *


class MainWindow:
    formula_list = []
    number_list = ["0"]

    def persent_listener(self):
        pass

    def radical_listener(self):
        pass

    def sqrt_listener(self):
        pass

    def reciprocal_listener(self):
        pass

    def ce_listener_listener(self):
        pass

    def operator_listener(self, operator):
        self.formula_list.append("".join(self.number_list))
        self.formula_list.append(operator)
        self.formula_var.set("".join(self.formula_list))
        self.number_list = ["0"]
        self.number_var.set("".join(self.number_list))

    def add_listener(self):
        self.operator_listener(" + ")

    def subtract_listener(self):
        self.operator_listener(" - ")

    def multiply_listener(self):
        self.operator_listener(" * ")

    def devide_listener(self):
        self.operator_listener(" / ")

    def equal_listener(self):
        self.formula_list.append("".join(self.number_list))
        self.formula_var.set("".join(self.formula_list))
        self.number_list = [calculator_algorithm.formula_calculate(self.formula_var.get())]
        self.number_var.set("".join(self.number_list))
        self.formula_list = []
        self.formula_var.set("".join(self.formula_list))

    def number_listener(self, number):
        if len(self.number_list) == 1 and self.number_list[0] == "0":
            self.number_list.pop()
        self.number_list.append(number)
        self.number_var.set("".join(self.number_list))

    def point_listener(self):
        if "." in self.number_list:
            pass
        else:
            self.number_list.append(".")
            self.number_var.set("".join(self.number_list))

    def clear_listener(self):
        self.number_list = ["0"]
        self.number_var.set("".join(self.number_list))
        self.formula_list = []
        self.formula_var.set("".join(self.formula_list))

    def backspace_listener(self):
        if len(self.number_list) == 1 and self.number_list[0] == "0":
            pass
        elif len(self.number_list) == 1:
            self.number_list = ["0"]
            self.number_var.set("".join(self.number_list))
        else:
            self.number_list.pop()
            self.number_var.set("".join(self.number_list))

    def negative_listener(self):
        pass

    def zero_listener(self):
        pass

    def one_listener(self):
        self.number_listener("1")

    def two_listener(self):
        self.number_listener("2")

    def three_listener(self):
        self.number_listener("3")

    def four_listener(self):
        self.number_listener("4")

    def five_listener(self):
        self.number_listener("5")

    def six_listener(self):
        self.number_listener("6")

    def seven_listener(self):
        self.number_listener("7")

    def eight_listener(self):
        self.number_listener("8")

    def nine_listener(self):
        self.number_listener("9")

    def init_formula(self):
        formula = Label(self.frame, justify=CENTER, textvariable=self.formula_var, font=("Arial", 12), height=2)
        formula.grid(row=0, column=0, columnspan=4, sticky=N+S+E, padx=5,  pady=5)

    def init_number(self):
        number = Label(self.frame, justify=CENTER, textvariable=self.number_var, font=("Arial", 18), height=1)
        number.grid(row=1, column=0, columnspan=4, sticky=N+S+E, padx=5,  pady=5)

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Calculator")
        self.formula_var = StringVar()
        self.number_var = StringVar()
        self.number_var.set("".join(self.number_list))
        self.init_formula()
        self.init_number()

        b_persent = Button(self.frame, text="%", width=10, height=2, command=self.persent_listener)
        b_radical = Button(self.frame, text="√", width=10, height=2, command=self.radical_listener)
        b_sqrt = Button(self.frame, text="sqrt(x)", width=10, height=2, command=self.sqrt_listener)
        b_reciprocal = Button(self.frame, text="1/x", width=10, height=2, command=self.reciprocal_listener)
        b_ce = Button(self.frame, text="ce", width=10, height=2, command=self.ce_listener)
        b_clear = Button(self.frame, text="c", width=10, height=2, command=self.clear_listener)
        b_backspace = Button(self.frame, text="<", width=10, height=2, command=self.backspace_listener)
        b_devide = Button(self.frame, text="÷", width=10, height=2, command=self.devide_listener)
        b_seven = Button(self.frame, text="7", width=10, height=2, command=self.seven_listener)
        b_eight = Button(self.frame, text="8", width=10, height=2, command=self.eight_listener)
        b_nine = Button(self.frame, text="9", width=10, height=2, command=self.nine_listener)
        b_multiply = Button(self.frame, text="X", width=10, height=2, command=self.multiply_listener)
        b_four = Button(self.frame, text="4", width=10, height=2, command=self.four_listener)
        b_five = Button(self.frame, text="5", width=10, height=2, command=self.five_listener)
        b_six = Button(self.frame, text="6", width=10, height=2, command=self.six_listener)
        b_subtract = Button(self.frame, text="-", width=10, height=2, command=self.subtract_listener)
        b_one = Button(self.frame, text="1", width=10, height=2, command=self.one_listener)
        b_two = Button(self.frame, text="2", width=10, height=2, command=self.two_listener)
        b_three = Button(self.frame, text="3", width=10, height=2, command=self.three_listener)
        b_add = Button(self.frame, text="+", width=10, height=2, command=self.add_listener)
        b_negative = Button(self.frame, text="±", width=10, height=2, command=self.negative_listener)
        b_zero = Button(self.frame, text="0", width=10, height=2, command=self.zero_listener)
        b_point = Button(self.frame, text=".", width=10, height=2, command=self.point_listener)
        b_equal = Button(self.frame, text="=", width=10, height=2, command=self.equal_listener)

        b_persent.grid(row=2, column=0, padx=2, pady=2)
        b_radical.grid(row=2, column=1, padx=2, pady=2)
        b_sqrt.grid(row=2, column=2, padx=2, pady=2)
        b_reciprocal.grid(row=2, column=3, padx=2, pady=2)
        b_ce.grid(row=3, column=0, padx=2, pady=2)
        b_clear.grid(row=3, column=1, padx=2, pady=2)
        b_backspace.grid(row=3, column=2, padx=2, pady=2)
        b_devide.grid(row=3, column=3, padx=2, pady=2)
        b_seven.grid(row=4, column=0, padx=2, pady=2)
        b_eight.grid(row=4, column=1, padx=2, pady=2)
        b_nine.grid(row=4, column=2, padx=2, pady=2)
        b_multiply.grid(row=4, column=3, padx=2, pady=2)
        b_four.grid(row=5, column=0, padx=2, pady=2)
        b_five.grid(row=5, column=1, padx=2, pady=2)
        b_six.grid(row=5, column=2, padx=2, pady=2)
        b_subtract.grid(row=5, column=3, padx=2, pady=2)
        b_one.grid(row=6, column=0, padx=2, pady=2)
        b_two.grid(row=6, column=1, padx=2, pady=2)
        b_three.grid(row=6, column=2, padx=2, pady=2)
        b_add.grid(row=6, column=3, padx=2, pady=2)
        b_negative.grid(row=7, column=0, padx=2, pady=2)
        b_zero.grid(row=7, column=1, padx=2, pady=2)
        b_point.grid(row=7, column=2, padx=2, pady=2)
        b_equal.grid(row=7, column=3, padx=2, pady=2)

        self.frame.mainloop()


window = MainWindow()
