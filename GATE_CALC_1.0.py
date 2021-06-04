from tkinter import *
from tkinter import messagebox
import math
import numpy

win = Tk()
win.iconbitmap("Dakirby309-Simply-Styled-Calculator.ico")
win.geometry("701x330")
win.resizable(0, 0)
win.title("GATE_CALC_1.0")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


def back_space():
    global expression
    result = str(expression[:-1])
    input_text.set(result)
    expression = result


# --------------------------------------------------------------------------------------
# Calculation function:

def hypersine(n):
    global expression
    result = str(math.sinh(numpy.degrees(float(n))))
    input_text.set(result)


def hypercosine(n):
    global expression
    result = str(math.cosh(numpy.radians(float(n))))
    input_text.set(result)


def hypertan(n):
    global expression
    result = str(math.tanh(numpy.radians(float(n))))
    input_text.set(result)


def sine(n):
    global expression
    result = str(math.sin(numpy.radians(float(n))))
    input_text.set(result)


def cosine(n):
    global expression
    result = str(math.cos(numpy.radians(float(n))))
    input_text.set(result)


def tangent(n):
    global expression
    result = str(math.tan(numpy.radians(float(n))))
    input_text.set(result)


def archypersine(n):
    global expression
    result = str(numpy.degrees(math.asinh(float(n))))
    input_text.set(result)


def archypercosine(n):
    global expression
    result = str(numpy.degrees(math.acosh(float(n))))
    input_text.set(result)


def archypertan(n):
    global expression
    result = str(numpy.degrees(math.atanh(float(n))))
    input_text.set(result)


def arcsine(n):
    global expression
    result = str(numpy.degrees(math.asin(float(n))))
    input_text.set(result)


def arcosine(n):
    global expression
    result = str(numpy.degrees(math.acos(float(n))))
    input_text.set(result)


def arctan(n):
    global expression
    result = str(numpy.degrees(math.atan(float(n))))
    input_text.set(result)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main_fact(n):
    global expression
    result = str(factorial(int(n)))
    input_text.set(result)
    expression = result


def exponential(n):
    global expression
    result = str(math.exp(float(n)))
    input_text.set(result)


def cube(n):
    global expression
    result = str(math.pow(float(n), 3))
    input_text.set(result)
    expression = result


def square(n):
    global expression
    result = str(math.pow(float(n), 2))
    input_text.set(result)


def e():
    global expression
    result = expression + str(math.e)
    input_text.set(result)
    expression = result


def pi():
    global expression
    result = expression + str(math.pi)
    input_text.set(result)
    expression = result


def square_root(n):
    global expression
    result = str(math.sqrt(float(n)))
    input_text.set(result)


def inv(n):
    global expression
    result = str(1 / float(n))
    input_text.set(result)


def natural_log(n):
    global expression
    result = str(math.log(float(n)))
    input_text.set(result)


def log_base10(n):
    global expression
    result = str(math.log10(float(n)))
    input_text.set(result)


def log_base2(n):
    global expression
    result = str(math.log2(float(n)))
    input_text.set(result)


def absolute(n):
    global expression
    result = str(abs(float(n)))
    input_text.set(result)


def e_to_x(n):
    global expression
    result = str(math.e ** (int(n)))
    input_text.set(result)


def info_box():
    detail = """
        Specially designed GATE calculator 
        for GATE aspirants.
        
        
        Developer:-       DEBU PATRA 
                         (B.Tech in ECE from DTU)
                         
        Contact:-        +91 7291802159
        
        Email:-          patradebu1207@gmail.com
        
        
        Thank you for using our product.
    """
    messagebox.showinfo("Info", detail)


expression = ""
input_text = StringVar()

input_frame = Frame(win, width=690, height=50, bd=0, highlightbackground="black", highlightcolor="blue",
                    highlightthickness=1)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=47, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=1)
# input_field.pack(ipady=10)

btns_frame = Frame(win, width=700, height=250, bg="grey")
btns_frame.pack()

# Info button
info_btn = Button(input_frame, text="Info", fg="black", width=10, height=3, bd=0, bg="#348DAE",
                  activebackground="#AACEE9",
                  cursor="hand2",
                  command=lambda: info_box()).grid(row=0, column=0, padx=1, pady=1)

# row one

sinh = Button(btns_frame, text="sinh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: hypersine(expression)).grid(row=0, column=0, padx=1, pady=1)
cosh = Button(btns_frame, text="cosh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: hypercosine(expression)).grid(row=0, column=1, padx=1, pady=1)
tanh = Button(btns_frame, text="tanh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: hypertan(expression)).grid(row=0, column=2, padx=1, pady=1)
Exp = Button(btns_frame, text="Exp", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: exponential(expression)).grid(row=0, column=3, padx=1, pady=1)
cubed = Button(btns_frame, text="X^3", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: cube(expression)).grid(row=0, column=4, padx=1, pady=1)
log = Button(btns_frame, text="log10x", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: log_base10(expression)).grid(row=0, column=5, padx=1, pady=1)
back = Button(btns_frame, text="back", fg="black", width=10, height=3, bd=0, bg="#FA5931", activebackground="#CE2107",
              cursor="hand2",
              command=lambda: back_space()).grid(row=0, column=6, padx=1, pady=1)
clear = Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#FA5931", activebackground="#CE2107",
               cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=7, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=0, column=8, padx=1, pady=1)

# row second
asinh = Button(btns_frame, text="asinh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: archypersine(expression)).grid(row=1, column=0, padx=1, pady=1)
acosh = Button(btns_frame, text="acosh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: archypercosine(expression)).grid(row=1, column=1, padx=1, pady=1)
atanh = Button(btns_frame, text="atanh", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: archypertan(expression)).grid(row=1, column=2, padx=1, pady=1)
log2x = Button(btns_frame, text="log2x", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: log_base2(expression)).grid(row=1, column=3, padx=1, pady=1)
squared = Button(btns_frame, text="X^2", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
                 cursor="hand2",
                 command=lambda: square(expression)).grid(row=1, column=4, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=5, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=6, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=7, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click("-")).grid(row=1, column=8, padx=1, pady=1)

# row third
Pi = Button(btns_frame, text="pi", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
            cursor="hand2",
            command=lambda: pi()).grid(row=2, column=0, padx=1, pady=1)
exp = Button(btns_frame, text="e", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: e()).grid(row=2, column=1, padx=1, pady=1)
fact = Button(btns_frame, text="n!", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: main_fact(expression)).grid(row=2, column=2, padx=1, pady=1)
nlog = Button(btns_frame, text="ln", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: natural_log(expression)).grid(row=2, column=3, padx=1, pady=1)
ex = Button(btns_frame, text="e^x", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
            cursor="hand2",
            command=lambda: e_to_x(expression)).grid(row=2, column=4, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=5, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=6, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=7, padx=1, pady=1)
product = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
                 cursor="hand2",
                 command=lambda: btn_click("*")).grid(row=2, column=8, padx=1, pady=1)

# row fourth
sinet = Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: sine(expression)).grid(row=3, column=0, padx=1, pady=1)
cosi = Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: cosine(expression)).grid(row=3, column=1, padx=1, pady=1)
tang = Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: tangent(expression)).grid(row=3, column=2, padx=1, pady=1)
power = Button(btns_frame, text="x^y", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click("**")).grid(row=3, column=3, padx=1, pady=1)
inverse = Button(btns_frame, text="1/x", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
                 cursor="hand2",
                 command=lambda: inv(expression)).grid(row=3, column=4, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=5, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=6, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=7, padx=1, pady=1)
division = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
                  cursor="hand2",
                  command=lambda: btn_click("/")).grid(row=3, column=8, padx=1, pady=1)

# row fifth
asin = Button(btns_frame, text="asin", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: arcsine(expression)).grid(row=4, column=0, padx=1, pady=1)
acos = Button(btns_frame, text="acos", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: arcosine(expression)).grid(row=4, column=1, padx=1, pady=1)
atan = Button(btns_frame, text="atan", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: arctan(expression)).grid(row=4, column=2, padx=1, pady=1)
sroot = Button(btns_frame, text="sqrt", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: square_root(expression)).grid(row=4, column=3, padx=1, pady=1)
mod = Button(btns_frame, text="|x|", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
             cursor="hand2",
             command=lambda: absolute(expression)).grid(row=4, column=4, padx=1, pady=1)
percentile = Button(btns_frame, text="%", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
                    cursor="hand2",
                    command=lambda: btn_click("%")).grid(row=4, column=5, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", activebackground="#AACEE9",
              cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=6, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#BFC1C1", activebackground="#AACEE9",
               cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=7, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#5EEF54", activebackground="#299537",
                cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=8, padx=1, pady=1)

win.mainloop()
