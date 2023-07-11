# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# today = datetime.today().strftime('%d/%m/%Y')
# url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'


# response = requests.get(url)

# xml = BeautifulSoup(response.content, 'html.parser')

# def get_course(id, k):
#     rez = xml.find('valute', {'id': id})
#     val = float(rez.value.text.replace(',', '.'))
#     file.write(f'{k} {rez.charcode.text} = {round(val * k, 2)} RUB\n')
#     print(f'{k} {rez.charcode.text} = {round(val * k, 2)} RUB')  

# file = open('urok_6.txt', 'w')
# file.write(f'Курс валют на {today}\n')

# k = int(input('Введите кол-во валюты: '))
# print(f'Курс валют на {today}')
# get_course('R01235', k)
# get_course('R01239', k)
# get_course('R01035', k)
# get_course('R01210', k)
# get_course('R01370', k)

# file.write('-'*100 + '\n')
# file.close()
 


# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# today = datetime.today().strftime('%d/%m/%Y')
# url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'

# response = requests.get(url)
# xml = BeautifulSoup(response.content, 'html.parser')

# EUR = int(xml.find('valute', {'id': 'R01239'}))
# RUB = 1
# USD = int(xml.find('valute', {'id': 'R01235'}))

# def get_course(valute_from, valute_to, amount):
#     EUR = xml.find('valute', {'id': 'R01239'})
#     RUB = 1
#     USD = xml.find('valute', {'id': 'R01235'})
#     result = amount * valute_from
#     print(result)

    

# valute_inp = input('Введите EUR, RUB или USD: ')
# valute_to_inp = input("Введите валюту, в котороую вы хотите конвертировать другую валюту(EUR, RUB или USD): ")
# amount_inp = input('Введите количество количество денег, которое вы хотите перевести: ')
# if valute_inp == 'RUB':
#     if valute_to_inp == 'RUB':
#         get_course(valute_inp, 1, amount_inp)
# if valute_inp == 'EUR':
#     if valute_to_inp == 'RUB':
#         get_course(EUR, valute_to_inp, amount_inp)
# if valute_inp == 'USD':
#     if valute_to_inp == 'RUB':
#         get_course(USD, valute_to_inp, amount_inp)




from tkinter import *
from bs4 import BeautifulSoup
import requests
import random

def menu():
    clear()
    label_title = Label(text='Что вы хотите сделать?', font=('Arial', 24), fg='white',bg='red')
    label_title.place(width=700, height=50, x=0,y=0)

    b1 = Button(text='узнать что-то новое', font=('Arial', 24), fg='black', command = get_fact)
    b1.place(x=25,y=75, width=300)
    b2 = Button(text='куда сходить', font=('Arial', 24), fg='black', command = get_fact)
    b2.place(x=375,y=75, width=300)
    b3 = Button(text='какой фильм посмотреть', font=('Arial', 12), fg='black', command= get_film)
    b3.place(x=60,y=160, width=300)

def get_film():
    clear()
    response = requests.get('https://www.kinoafisha.info/rating/movies/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_= 'movieItem_info'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=10,y=10)

def get_fact():
    clear()
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_ = 'p-2 clearfix'))
    mes_label = Message(text=res.text, font=('Arial', 24), fg ='black', width=680, borderwidth=0)
    mes_label.place(x=10,y=10)
    window.after(5000, menu)

def geroi_dota():
    clear()
    response = requests.get('https://cyber.sports.ru/tribuna/blogs/doyouwannaplayagame/2864832.html')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_ = 'is-regular'))
    mes_label = Message(text=res.text, font=('Arial', 24), fg ='black', width=680, borderwidth=0)
    mes_label.place(x=10,y=10)
    window.after(5000, menu)

def get_festival():
    clear()
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='post-content'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=130, y=10)
    window.after(5000, menu)


def clear():
    
    all_widg = window.place_slaves()
    for widg in all_widg:
        widg.destroy()
# def horror_game():
#     break

def game():
    clear()
    b4 = Button(text='Ужасы', font=('Arial', 12), fg='black', command=horror)
    b4.place(x=50,y=300, width=300)
    b5 = Button(text='ММО', font=('Arial', 12), fg='black', command=MMO)
    b5.place(x=50,y=400, width=300)
    b6 = Button(text='Шутер', font=('Arial', 12), fg='black', command=shooter)
    b6.place(x=50,y=500, width=300)
    b8 = Button(text='Приключения', font=('Arial', 12), fg='black', command=MMO)
    b8.place(x=350,y=300, width=300)
    b9 = Button(text='Гонки', font=('Arial', 12), fg='black', command=MMO)
    b9.place(x=350,y=400, width=300)
    b10 = Button(text='Файтинг', font=('Arial', 12), fg='black', command=MMO)
    b10.place(x=350,y=500, width=300)
    

def horror():
    response = requests.get('https://www.igromania.ru/games/all/horror/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)
def shooter():
    response = requests.get('https://www.igromania.ru/games/all/shooter/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)

def MMO():
    response = requests.get('https://www.igromania.ru/games/all/online/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)

def adventure():
    response = requests.get('https://www.igromania.ru/games/all/adventure/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)

def races():
    response = requests.get('https://www.igromania.ru/games/all/racing/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)

def fighting():
    response = requests.get('https://www.igromania.ru/games/all/fighting/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    res = random.choice(html.find_all(class_='game-card'))
    mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
    mes_label.place(x=50, y=20)
    window.after(5000, menu)

window = Tk()
window.title('Мой первый проект')
window.geometry('700x600')

label_title = Label(text = 'Что вы хотите сделать?', font=('Arial', 24), fg='white', bg = 'red')
label_title.place(width=700, height=50, x=0, y=0)

b1 = Button(text='узнать что-то новое', font=('Arial', 24), fg='black', command = get_fact)
b1.place(x=25,y=75, width=300)
b2 = Button(text='куда сходить', font=('Arial', 24), fg='black', command = get_festival)
b2.place(x=375,y=75, width=300)
b3 = Button(text='какой фильм посмотреть', font=('Arial', 12), fg='black', command=get_film)
b3.place(x=200,y=160, width=300)
b7 = Button(text='в какую игру поиграть', font=('Arial', 12), fg='black', command=game)
b7.place(x=200,y=200, width=300)
b13 = Button(text='дота', font=('Arial', 12), fg='black', command=geroi_dota)
b13.place(x=200,y=250, width=300)




window.mainloop()