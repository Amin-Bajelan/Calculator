import math
import tkinter as tk

background_color = '#17161b'
color_btn_clear = '#FF6600'

result = []
result_calculator = []
first_point = int
second_point = int(-1)
flag_have_operation = bool(False)
flag_calculator = bool(False)
flag_radical = bool(False)

window = tk.Tk()
window.title('Calculator')
window.geometry('455x653')
window.maxsize(455, 653)
window.minsize(455, 653)
window.configure(background=background_color)




def show(value):
    global first_point
    global second_point
    global flag_radical
    global flag_have_operation
    global result_calculator



    if str(value) == '√':
        first_point = len(result)
        flag_radical = True
        flag_have_operation = True
        result_calculator.append('')

    else:
        result_calculator.append(value)
        if flag_radical:

            if str(value) == '+' or str(value) == '-' or str(value) == '*' or str(value) == '/' or str(value) == ')':
                second_point = len(result)
                flag_have_operation = True

    result.append(value)
    label_result.config(text=result)


def clear():
    global result
    result = []
    label_result.config(text=result)


def show_answer():
    global first_point
    global second_point
    global flag_have_operation
    global flag_calculator
    global flag_radical
    global result
    global result_calculator
    my_str = ''

    if flag_have_operation:
        empty_list = []
        if int(second_point) == -1:
            for i in range(int(first_point),len(result_calculator)):
                my_str +=  str(result_calculator[i])
            print()
            num = math.sqrt(float(my_str))
            for i in range(0,first_point):
                empty_list.append(result_calculator[i])
            empty_list.append(str(num))
            my_str = ''
            for i in empty_list:
                my_str += str(i)
            num = eval(my_str)
            if float(num).is_integer():
                num = int(num)
            else:
                num = float(num)
            label_result.config(text=num)
            result_calculator = []
            result_calculator.append(num)
            result = []
            result.append(num)
            flag_have_operation = False
            flag_radical = False
            flag_calculator = False

        else:
            my_num = ''
            for i in range(first_point, second_point):
                my_num += str(result_calculator[i])
                result_calculator[i] = ''
            result_calculator[first_point] = math.sqrt(float(my_num))
            for i in result_calculator:
                my_str += str(i)
            num = eval(my_str)
            if float(num).is_integer():
                num = int(num)
            else:
                num = float(num)
            label_result.config(text=num)
            result_calculator = []
            result_calculator.append(num)
            result = []
            result.append(num)
            flag_have_operation = False
            flag_radical = False
            flag_calculator = False


    else:
        for i in result:
            my_str = my_str + str(i)
        num = eval(my_str)
        if float(num).is_integer():
            num = int(num)
        else:
            num = float(num)
        label_result.config(text=str(num))
        result_calculator = []
        result_calculator.append(num)
        result = []
        result.append(num)
        flag_have_operation = False
        flag_radical = False
        flag_calculator = False


label_result = tk.Label(window, text='', width=22, height=2, font=('Arial', 30))
label_result.pack()

btn_clear = tk.Button(text=' C ', font=('Arial', 30, 'bold'), bg=color_btn_clear, fg='black', padx=10, pady=10,
                      command=clear)
btn_clear.place(x=10, y=105)
btn_plus = tk.Button(text=' + ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=10, pady=10,
                     command=lambda: show('+'))
btn_plus.place(x=125, y=105)
btn_minus = tk.Button(text=' - ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=15, pady=10,
                      command=lambda: show('-'))
btn_minus.place(x=235, y=105)
btn_multiplication = tk.Button(text=' × ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=12, pady=10,
                               command=lambda: show('*'))
btn_multiplication.place(x=345, y=105)
btn_7 = tk.Button(text=' 7 ', font=("Arial", 30, 'bold'), bg='gray', fg='black', padx=13, pady=10,
                  command=lambda: show('7'))
btn_7.place(x=10, y=215)
btn_8 = tk.Button(text=' 8 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('8'))
btn_8.place(x=125, y=215)
btn_9 = tk.Button(text=' 9 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('9'))
btn_9.place(x=235, y=215)
btn_division = tk.Button(text=' ÷ ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=12, pady=10,
                         command=lambda: show('/'))
btn_division.place(x=345, y=215)
btn_4 = tk.Button(text=' 4 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=13, pady=10,
                  command=lambda: show('4'))
btn_4.place(x=10, y=325)
btn_5 = tk.Button(text=' 5 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('5'))
btn_5.place(x=125, y=325)
btn_6 = tk.Button(text=' 6 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('6'))
btn_6.place(x=235, y=325)
btn_radical = tk.Button(text=' √ ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=12, pady=10,
                        command=lambda: show('√'))
btn_radical.place(x=345, y=325)
btn_1 = tk.Button(text=' 1 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=13, pady=10,
                  command=lambda: show('1'))
btn_1.place(x=10, y=435)
btn_2 = tk.Button(text=' 2 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('2'))
btn_2.place(x=125, y=435)
btn_3 = tk.Button(text=' 3 ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('3'))
btn_3.place(x=235, y=435)
btn_equal = tk.Button(text=' = ', font=('Arial', 30, 'bold'), bg='white', fg='black', padx=11, pady=10,
                      command=lambda: show_answer())
btn_equal.place(x=345, y=435)
btn_dot = tk.Button(text=' . ', font=('Arila', 30, 'bold'), bg='gray', fg='black', padx=18, pady=10,
                    command=lambda: show('.'))
btn_dot.place(x=10, y=545)
btn_0 = tk.Button(text=' 0 ', font=("Arila", 30, 'bold'), bg='gray', fg='black', padx=11, pady=10,
                  command=lambda: show('0'))
btn_0.place(x=125, y=545)
btn_Parenthesis_r = tk.Button(text=' ( ', font=('Arila', 30, 'bold'), bg='gray', fg='black', padx=15, pady=10,
                              command=lambda: show('('))
btn_Parenthesis_r.place(x=235, y=545)
btn_Parenthesis_l = tk.Button(text=' ) ', font=('Arial', 30, 'bold'), bg='gray', fg='black', padx=16, pady=10,
                              command=lambda: show(')'))
btn_Parenthesis_l.place(x=345, y=545)

window.mainloop()

#git pull shark