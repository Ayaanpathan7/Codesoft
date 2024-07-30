from tkinter import *

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def get_operator(op):
    global first_number, operator
    
    try:
        first_number = float(result_label['text'])
    except ValueError:
        first_number = 0
    operator = op
    result_label.config(text='')

def calculate():
    try:
        second_number = float(result_label['text'])
    except ValueError:
        result_label.config(text="Error")
        return

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            result_label.config(text="Error")
            return
        result = first_number / second_number
    elif operator == '%':
        if second_number == 0:
            result_label.config(text="Error")
            return
        result = first_number % second_number

    result_label.config(text=str(round(result, 2)))

def clear():
    result_label.config(text="")

root = Tk()
root.title("Calculator")
root.geometry('380x450')
root.resizable(0, 0)
root.config(background="black")

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

border_frame = Frame(root, bg='white', padx=3, pady=3)
border_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

result_label = Label(border_frame, text="", bg='#027566', fg='black', height=2)
result_label.pack(fill='both', expand=True)
result_label.config(font=('verdana', 30, 'bold'))

button_7 = Button(root, text='7', height=3, width=10, command=lambda: get_digit('7'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_8 = Button(root, text='8', height=3, width=10, command=lambda: get_digit('8'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_9 = Button(root, text='9', height=3, width=10, command=lambda: get_digit('9'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_div = Button(root, text='/', height=3, width=10, command=lambda: get_operator('/'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))

button_4 = Button(root, text='4', height=3, width=10, command=lambda: get_digit('4'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_5 = Button(root, text='5', height=3, width=10, command=lambda: get_digit('5'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_6 = Button(root, text='6', height=3, width=10, command=lambda: get_digit('6'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_mul = Button(root, text='*', height=3, width=10, command=lambda: get_operator('*'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))

button_1 = Button(root, text='1', height=3, width=10, command=lambda: get_digit('1'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_2 = Button(root, text='2', height=3, width=10, command=lambda: get_digit('2'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_3 = Button(root, text='3', height=3, width=10, command=lambda: get_digit('3'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_sub = Button(root, text='-', height=3, width=10, command=lambda: get_operator('-'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))

button_0 = Button(root, text='0', height=3, width=10, command=lambda: get_digit('0'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_dot = Button(root, text='.', height=3, width=10, command=lambda: get_digit('.'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_equal = Button(root, text='=', height=3, width=10, command=calculate, bg='#FFA500', fg='white', font=('verdana', 14, 'bold'))
button_add = Button(root, text='+', height=3, width=10, command=lambda: get_operator('+'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))
button_modulo = Button(root, text='%', height=3, width=10, command=lambda: get_operator('%'), bg='#4CAF50', fg='white', font=('verdana', 14, 'bold'))

button_clear = Button(root, text='C', height=3, width=10, command=clear, bg='#FF6F61', fg='white', font=('verdana', 14, 'bold'))

button_7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
button_div.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

button_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
button_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
button_mul.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button_1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button_2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button_3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
button_sub.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button_0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
button_dot.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
button_equal.grid(row=4, column=2, rowspan=2, padx=5, pady=5, sticky="nsew")
button_add.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
button_modulo.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")
button_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

root.mainloop()
