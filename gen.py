from tkinter import *
import os
root = Tk()
root.geometry('600x400')
root.title("Генератор паролей")
root["bg"] = "LightBlue"
import random
from random import randrange

ex = None
password = Label(text='Пароль: ' + ex, bg='LightBlue')
password.grid(row=0, column=0)
inp=Text(root, bg='LightBlue')
inp.grid(row=2,column=0)
numbers = ['1','2','3','4','5','6','7','8','9']
special = [',','.','/','\'','{','}','`','~','@','№',';']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def passgen():
    try:
        ex = ''
        num = random.randint(1, 2)
        if num == 1:
            rand = randrange(len(lower_letters))
            ex += lower_letters[rand]
        if num == 2:
            rand = randrange(len(up_letters))
            ex += up_letters[rand]
        for i in range(int(inp.get('1.0', END)) - 1):
            num = random.randint(1, 4)
            if num == 1:
                rand = randrange(len(numbers))
                ex += numbers[rand]
            if num == 2:
                rand = randrange(len(special))
                ex += special[rand]
            if num == 3:
                rand = randrange(len(lower_letters))
                ex += lower_letters[rand]
            if num == 4:
                rand = randrange(len(up_letters))
                ex += up_letters[rand]
        password['text'] = 'Пароль: ' + ex
    except Exception:
        pass


gen = Button(text='Создать пароль', bg='White', command=passgen)
gen.grid(row=1,column=0)
root.mainloop()
# мин 6 символов, макс 1148486648
#tk.layout
# Сделать проверку на ожидание. os
