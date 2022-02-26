from math import *
from decimal import *
from tkinter import *
k, p, please = [False for _ in range(3)]
answer, answer1, something, count, lbl, lbl1, lbl2, lb3, sel, sel1, bt, bt1, btn2 = [0 for _ in range(13)]
window = Tk()


def method_of_iterations(n):
    def func_change(x):
        return 2 + exp(-x)

    def base_function(x):
        return exp(-x) - x + 2
    amount_iterations = n
    a, b, flag_right, flag_left, right_edge, left_edge = 0, 0, False, False, 0, 0
    while True:
        if not flag_right:
            if base_function(a) > 0:
                right_edge, flag_right = a, True
            if base_function(b) > 0:
                right_edge, flag_right = b, True
        if not flag_left:
            if base_function(a) < 0:
                left_edge, flag_left = a, True
            if base_function(b) < 0:
                left_edge, flag_left = b, True
        a += 1
        b -= 1
        if flag_right and flag_left:
            break
    a = (left_edge + right_edge) / 2
    b = func_change(a)
    for i in range(amount_iterations):
        b = func_change(b)
    return b


def method_of_bruteforce(n1):
    def equation(x):
        return exp(-x) - x + 2
    n, fla, flb, left, right = n1, False, False, 0, 0
    for i in range(-15, 50):#в цикле можно использовать только целые числа поэтому не 1,5 и 5
        if equation(i / 10) > 0 and not fla:
            right = i / 10
            fla = True
        if 0 < equation(i / 10) < equation(right) and fla:
            right = i / 10
        if equation(i / 10) < 0 and not flb:
            left = i / 10
            flb = True
        if equation(left) < equation(i / 10) < 0 and flb:
            left = i / 10

    lovely, counter = n, 0#распаковка lovely - сколько знаков, counter - глубина(0.1, 0.01, 0.001)
    while int(lovely) == 0:
        lovely *= 10
        counter += 1
    tool = 10
    for i in range(counter):#range - ряд рандомных чисел от 0 до counter
        a, b = right, left
        a, b = int(a * tool), int(b * tool)
        for w in range(a, b):
            if equation(left) < equation(w / tool) < 0:
                left = w / tool
            if 0 < equation(w / tool) < equation(right):
                right = w / tool
        tool *= 10
    return Decimal(left + right) / 2


def iterations():
    def destroyer():
        new.destroy()
        new1.destroy()
        answer.destroy()
        killjoy.destroy()
        ass.destroy()
        bi.destroy()
        angriest.destroy()
        if k:
            wer.destroy()
        comeback()

    def callback(event):
        global k, answer#ввод пользователя
        if answer.get().isdigit():
            if 0 < int(answer.get()) < 10000001:
                k = True
            else:
                angriest.place(x=85, y=67)
        else:
            angriest.place(x=85, y=67)

    def strange():
        global k, answer
        if answer.get().isdigit():#answer - поле для ввода, isdigit - вернёт false при проверке, если введено не число
            if 0 < int(answer.get()) < 10000001:
                k = True
            else:
                angriest.place(x=85, y=67)
        else:
            angriest.place(x=85, y=67)

    bi = Button(window, text="Рассчитать!", bg='black', fg='white', command=strange)
    bi.place(x=5, y=65)
    global k, answer
    window.geometry("310x110")
    lbl.destroy()
    lbl1.destroy()
    lbl2.destroy()
    bt.destroy()
    bt1.destroy()
    btn2.destroy()
    window.update()
    killjoy = Button(window, text='Вернуться', bg='black', fg='white', command=destroyer)
    killjoy.place(x=240, y=65)
    new = Label(window, text='Вы выбрали способ нахождения методом итераций.', bg='black', fg='white')
    new1 = Label(window, text='Укажите точность натуральным числом до 10000000:', bg='black', fg='white')
    ass = Label(window, text='(Для ввода нажмите Enter или кнопку под полем ввода)', bg='black', fg='white')
    angriest = Label(window, text='Введите требуемое число!', bg='black', fg='red')
    answer = Entry(window, bg='black', fg='white')#поле ввода
    ass.place(x=0, y=90)
    new.place(x=0, y=0)
    new1.place(x=0, y=20)
    answer.place(x=5, y=45)
    window.update()
    k = False#пользователь ничего не ввёл
    while not k:
        window.update()
        window.bind("<Return>", callback)#после нажатия enter вызываем функцию callback
    wer = Label(window, text=f'x = {method_of_iterations(int(answer.get()))}', bg='black', fg='white')#с помощью метода get получаем значение вводимое пользователем
    new.configure(text=f'Для указанного значения точности {answer.get()} (итераций)')
    new1.configure(text='Ответ к заданному уравнению: ')
    new1.place(x=0, y=20)
    wer.place(x=175, y=20)
    window.geometry('310x95')
    angriest.destroy()
    ass.destroy()


def brute():
    def destroyer():
        new.destroy()
        new1.destroy()
        new2.destroy()
        answer1.destroy()
        bi.destroy()
        limelighting.destroy()
        if p:
            wer.destroy()
        comeback()

    def callback(event):
        global answer1, p
        if answer1.get()[2:].isdigit() and answer1.get()[:2] == "0.":
            if 1 > float(answer1.get()) > 0:
                p = True
            else:
                new2.configure(text='Если разобрались со вводом,\n введите число согласно требованиям!', fg='red')
        else:
            new2.configure(text='Если разобрались со вводом,\n введите число согласно требованиям!', fg='red')

    def strange():
        global answer1, p
        if answer1.get()[2:].isdigit() and answer1.get()[:2] == "0.":#срезы
            if 1 > float(answer1.get()) > 0:
                p = True
            else:
                new2.configure(text='Если разобрались со вводом,\n введите число согласно требованиям!', fg='red')
        else:
            new2.configure(text='Если разобрались со вводом,\n введите число согласно требованиям!', fg='red')
    global answer1, p
    bi = Button(window, text="Рассчитать!", bg='black', fg='white', command=strange)
    bi.place(x=5, y=70)
    window.geometry("450x100")
    lbl.destroy()
    lbl1.destroy()
    lbl2.destroy()
    bt.destroy()
    bt1.destroy()
    btn2.destroy()
    window.update()
    limelighting = Button(window, text="Вернуться", bg='black', fg='white', command=destroyer)
    limelighting.place(x=380, y=70)
    new = Label(window, text='Вы выбрали способ нахождения методом прямого перебора значений.', bg='black', fg='white')
    new1 = Label(window, text='Укажите точность в размере от от 0.0000000000000000000001 до 1:', bg='black', fg='white')
    new2 = Label(window, text='(После ввода нажмите клавишу Enter)\n(Или кнопку под полем ввода)',
                 bg='black', fg='white')
    new2.place(x=150, y=45)
    answer1 = Entry(window, bg='black', fg='white')
    new.place(x=0, y=0)
    new1.place(x=0, y=20)
    answer1.place(x=5, y=50)
    window.update()
    p = False
    while not p:
        window.update()
        window.bind("<Return>", callback)
    wer = Label(window, text=f'x = {method_of_bruteforce(float(answer1.get()))}', bg='black', fg='white')
    new.configure(text=f'Для указанного значения точности {answer1.get()}')
    new1.configure(text='Ответ к заданному уравнению составляет')
    new2.destroy()
    new1.place(x=0)
    wer.place(x=240, y=20)


def special():
    def destroyer():
        avocado.destroy()
        bi.destroy()
        words.destroy()
        request.destroy()
        something.destroy()
        helped.destroy()
        if please:
            tr.destroy()
            tr1.destroy()
        comeback()

    def callback(event):
        global please, something
        if something.get().isdigit():
            if 0 < int(something.get()) < 10000001:
                please = True
            else:
                helped.configure(text='Что же, как вводить число, вы поняли.\n'
                                      'Но всё-таки следуйте требованиям по вводу, хорошо?', fg='red')
        else:
            helped.configure(text='Что же, как вводить число, вы поняли.\n'
                                  ' Но всё-таки следуйте требованиям по вводу, хорошо?', fg='red')

    def strange():
        global please, something
        if something.get().isdigit():
            if 0 < int(something.get()) < 10000001:
                please = True
            else:
                helped.configure(text='Что же, как вводить число, вы поняли.\n'
                                      'Но всё-таки следуйте требованиям по вводу, хорошо?', fg='red')
        else:
            helped.configure(text='Что же, как вводить число, вы поняли.\n'
                                  ' Но всё-таки следуйте требованиям по вводу, хорошо?', fg='red')
    global please, something
    bi = Button(window, text="Рассчитать!", bg='black', fg='white', command=strange)
    helped = Label(window, text='(Для ввода нажмите Enter, или кнопку под полем ввода)', bg='black', fg='white')
    something = Entry(window, width=15, fg='white', bg='black')
    window.geometry("500x110")
    lbl.destroy()
    lbl1.destroy()
    lbl2.destroy()
    bt.destroy()
    bt1.destroy()
    btn2.destroy()
    window.update()
    avocado = Button(window, text="Вернуться", bg='black', fg='white', command=destroyer)
    avocado.place(x=425, y=80)
    words = Label(window, text='Вы выбрали способ нахождения решения уравнениями обоими методами.',
                  bg='black', fg='white')
    words.place(x=5, y=2)
    request = Label(window, text='Пожалуйста, укажите точность натуральным числом, до 10000000!',
                    bg='black', fg='white')
    request.place(x=5, y=18)
    helped.place(x=110, y=40)
    something.place(x=10, y=47)
    bi.place(x=10, y=80)
    please = False
    while not please:
        window.update()
        window.bind('<Return>', callback)
    var = something.get()
    mot = Decimal(method_of_iterations(int(var)))
    mob = Decimal(method_of_bruteforce(1/int(var)))
    tr = Label(window, text=f'Методом итерации получено значение х = {round(mot, 22)}', bg='black', fg='white')
    tr1 = Label(window, text=f'Методом перебора получено значение х = {round(mob, 22)}', bg='black', fg='white')
    if count != 0:
        tr.configure(text=f'Методом итерации получено значение х = {mot}')
        tr1.configure(text=f'Методом итерации получено значение х = {mob}')
    tr.place(x=110, y=35)
    tr1.place(x=110, y=55)
    window.mainloop()


def clicked():
    f, g = sel.get(), sel1.get()
    if f == 1 and g == 1:
        special()
    elif g == 1 and f == 0:
        brute()
    elif g == 0 and f == 1:
        iterations()
    else:
        lb3.configure(text='Выберите хотя бы один вариант.')#если не выбрать не один вариант, меняется компаратор


def comeback():
    global lbl, lbl1, lbl2, lb3, sel, sel1, bt, bt1, btn2
    window.title("Solver Assistant")
    window['bg'] = ['black']
    lbl = Label(window, text="Задано иррациональное уравнение exp(-x) - x + 2 = 0", bg='black', fg='white')#label - строчка
    lbl1 = Label(window, text="на интервале от -1.5 до 5.0 включительно.", bg='black', fg='white')
    lbl2 = Label(window, text="Какой метод используем для вычисления переменной х?", bg='black', fg='white')
    lb3 = Label(window, text='', bg='black', fg='red')#нет текста
    lbl.place(x=17, y=0)#отсчёт ведётся всегда с левого верхнего угла(0;0) вправо положительный x вниз положительный y
    lbl1.place(x=45, y=20)
    lbl2.place(x=0, y=40)
    sel = IntVar()
    sel1 = IntVar()
    bt = Checkbutton(window, text='Метод итераций (последовательных приближений)', onvalue=1,#сам квадратик и то что можно поставить галочку
                     offvalue=0, variable=sel, bg='black', fg='white', selectcolor='red')
    bt1 = Checkbutton(window, text='Метод прямого перебора чисел в рамках отрезка', onvalue=1,
                      offvalue=0, variable=sel1, bg='black', fg='white', selectcolor='red')
    bt.place(x=0, y=60)
    bt1.place(x=0, y=80)
    btn2 = Button(window, text="Выбор сделан", command=clicked, width='15', bg='black', fg='white')
    btn2.place(x=5, y=110)
    lb3.place(x=130, y=115)
    window.resizable(0, 0)#окошко не растягиваемое из-за функции resizable
    window.geometry("335x140")#размер окошка
    window.mainloop()#зацикливание, чтобы окошко не убралось


comeback()

