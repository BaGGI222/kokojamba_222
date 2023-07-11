# from tkinter import *

# window = Tk()
# window.geometry('700x1000')
# window.title('нажатия по кнопке')


# count = 0

# def which_button():
#     global count
#     count += 1
#     print(count)

# bt = Button(text='Кликни', font=('Arial', 20), fg='white', bg='black', command=which_button)
# bt.place(x=200, y=130)


# if count == 20:
#     bt['bg'] == 'red'
# bt.place(x=200, y=130)

# window.mainloop()



# from tkinter import *
# from tkinter import messagebox
# from random import *
# from time import *
 
 
# window = Tk()
# window.geometry('700x900')
# window.title('Кликер')
# count = 0
# count_2 = 0
 
# bg_colors = ['black', 'blue', 'red', 'lime', 'orange']
# bg_index = 0
 
# def check():
#     global count, bg_index, b_2
#     b.place(x=randint(70, 500), y=randint(70, 650))
#     # b_2.place(x=randint(70, 500), y=randint(70, 650))
#     count += 1
#     if count % 20 == 0:
#         bg_index = 0 if bg_index == len(bg_colors) else bg_index + 1
#         b['fg'] = bg_colors[bg_index]
#         time.sleep(2)
#     if count % 10 == 0:
#         b_2['text'] = 'Ну пожалуйста'
    
# def check_2():
#     b_2.place(x=randint(70, 500), y=randint(70, 650))
    

# b = Button(text='нажми', font=('Arial', 20), fg='black', command=check)
# b.place(x=randint(70, 500), y=randint(70, 650))
# b_2 = Button(text='нажми сюда', font=('Arial', 20), fg='black', command=check_2)
# b_2.place(x=randint(70, 500), y=randint(70, 650))
 
# window.mainloop()


# from tkinter import *
# import random
# import time
 
 
# window = Tk()
# window.geometry('700x900')
# window.title('Кликер')
# count_1 = 0
# count_2 = 0
 
# bg_colors = ['black', 'blue', 'red', 'lime', 'orange']
# bg_index = 0
 
# def check_1():
#     global count_1,  bg_index
#     b.place(x=random.randint(1, 550), y=random.randint(1, 250))
#     if count_1 % 20 == 0:
#         bg_index = 0 if bg_index == len(bg_colors) else bg_index + 1
#         b['fg'] = bg_colors[bg_index]
#         time.sleep(2)
#     if count_1 % 10 == 0:
#         if count_2 % count_1 == 0:
#             b_2['text'] == 'Ну пожалуйста'
# def check_2():
#     global count_2, bg_index
#     b_2.place(x=random.randint(1,550), y = random.randint(1,250))
#     bg_index = 0 if bg_index == len(bg_colors) else bg_index + 1
#     b_2['fg'] = bg_colors[bg_index]
#     time.sleep(2)
#     if count_2 % 10 == 0:
#         if count_1 % count_2 == 0:
#             b['text'] == 'Ну пожалуйста'

    

 
# b = Button(text='нажми', font=('Arial', 20), fg='black', command=check_1)
# b.place(x=220, y=400)
# b_2 = Button(text='нажми сюда', font=('Arial', 20), fg = 'black', command=check_2)
# b_2.place(x=130, y=200)
    

# window.mainloop()

# from tkinter import *

# def on_close():
#     if int(count_text['text']) > 0:
#         count_text['text'] = int(count_text['text']) - 1
#         count_text.place(x=250,y=25, width=400, height=100)
#         window.after(1000, on_close)
#     else:
#         height = window.winfo_screenheight()
#         width = window.winfo_screenwidth()
#         # photo_l.place(width=width, height = height, x=0, y=0)
#         window.geometry(f'{width}x{height}')  

# window = Tk()
# window.geometry('900x500')
# window.title('danger')
# window.config(bg='black')
# window.resizable(width=False, height=False)

# text = Label(text='Ваш компьютер заражен', fg='green', bg='black', font=('Courier New', 20))
# text.place(x=200, y=200, width=700, height=100)

# count_text = Label(text='6', fg='green', bg = 'black', font=('Courier New', 20))

# # photo = PhotoImage(file='имя файла')
# # photo_l = Label(image=photo, bg= 'black')

# window.protocol('WM_DELETE_WINDOW', on_close)


# window.mainloop()

 
# from tkinter import *

# point = 0

# def checkButton():
#     global point
#     point += 1
#     if point == 1:
#         text_1.destroy()
#         text_2.place(x=100,y=200)
#         window.protocol('WM_DELETE_WINDOW', checkButton)

# window = Tk()
# window.geometry('900x500')
# window.title('ВЫИГРЫШ!!!')
# window.config(bg='black')

# text_1 = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', fg='white', bg='black', font=('Courier New', 20))
# text_1.place(x=200,y=200)
# bt = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', font=('Courier New', 20), fg='white', bg='black', command = checkButton)
# bt.place(x=400,y=300,)
# text_2 = Label(text='Чтобы забрать выйгрыш необходимо внести 1000руб.', fg='green', bg='black', font=('Courier New', 20))

# window.mainloop()



# from tkinter import *

# count = 0

# def clicker():
#     global count
#     bt_1.place(x=300, y=500)
#     count += 1
#     text['text'] = str(count)
#     text.pack()
# def clicker_minus():
#     global count
#     bt_2.place(x=600, y=500)
#     count -= 1 
#     if count <= 0:
#         count = 0
#     text['text'] = str(count)
#     text.pack()
    

# window = Tk()
# window.geometry('1000x1000')
# window.title('Кликер')
# window.config(bg='white')


# text = Label(text='0', font=('Arial', 34), fg='black', bg='white')
# text.pack()

# bt_1 = Button(window, text='+', font=('Arial', 12), fg='black', bg='white', command=clicker)
# bt_1.place(x=300,y=500)

# bt_2 = Button(text='-', font=('Arial', 12), fg='red', bg='white', command=click)
# bt_2.place(x=600,y=500)

# window.mainloop()




# from bs4 import BeautifulSoup
# import requests

# url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'lxml')
# ad = soup.find('div', class_='row ecomerce-items ecomerce-items-ajax')
# print(ad)



# a=int(input('Сколько вы зарабатываете в месяц?(в рублях) '))
# b=int(input('какую сумму денег вы бы жедади накопить?(в рублях)'))
# day = 0

# while b > 0:
#     b = b-a*0.3
#     day += 1
# print(day)



# from fpdf import FPDF

# '''
# P - портретное 
# L - альбомное
# '''
# '''
# pt - точки
# mm - милимметры
# cm - сантиметры
# in - дюймы
# '''
# pdf = FPDF('P', 'cm', 'A4')
# pdf.add_page()
# # pdf.set_font('courier', '', 'путь к шрифту', uni = True)
# pdf.set_font('courier', size=16)
# pdf.set_text_color(0, 255, 0)
# pdf.set_fill_color(150,50,168)
# pdf.cell(8,5, txt='hello world', align='C', border=1, fill=True)
# # pdf.image('название изображения', h=5, w=8,x=0,y=5)

# pdf.output('test_pdf.pdf')



# number = int(input('Введите число: '))
# summ = 0

# while number != 0:
#     summ += number
#     number = int(input('Введите следующее число: '))
# print(summ)




# a = int(input('Введите пароль: '))

# while a != 235:
#     a = int(input('Пароль неверный,попробуйте ещё раз: '))
# else:
#     print('пароль верный')



# from fpdf import FPDF
# import datetime     

# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
# pdf.image('1644366724_55-phonoteka-org-p-fon-svetlii-vertikalnii-56.jpg', h=297, w=210 , x=0, y=0)

# pdf.add_font('courier', '', 'C:\WINDOWS\FONTS\COUR.TTF', uni = True)
# pdf.set_font('courier', size = 37)
# pdf.set_text_color(0,0,0)
# friend = input('Введите имя друга: ')
# pdf.cell(0,50, ln=1)
# pdf.cell(0, 20, txt=f'Дорогой {friend}!', align='C', ln =1 )
# pdf.set_font('courier', size = 14)
# mess = input('Введите поздравление: ')
# pdf.set_right_margin(50)
# pdf.set_right_margin(50)
# pdf.multi_cell(0, 10, txt=mess, align='C')
# date_n = datetime.datetime.today().strftime('%d.%m.%y')
# pdf.cell(0,10, txt=date_n, align='R', ln=1)

# pdf.output('test_card_pdf.pdf')




# from tkinter import *
# from bs4 import BeautifulSoup
# import requests
# import random

# def menu():
#     clear()
#     label_title = Label(text='Что вы хотите сделать?', font=('Arial', 24), fg='white',bg='red')
#     label_title.place(width=700, height=50, x=0,y=0)

#     b1 = Button(text='узнать что-то новое', font=('Arial', 24), fg='black', command = get_fact)
#     b1.place(x=25,y=75, width=300)
#     b2 = Button(text='куда сходить', font=('Arial', 24), fg='black', command = get_fact)
#     b2.place(x=375,y=75, width=300)
#     b3 = Button(text='какой фильм посмотреть', font=('Arial', 12), fg='black', command= get_film)
#     b3.place(x=60,y=160, width=300)

# def get_film():
#     clear()
#     response = requests.get('https://www.kinoafisha.info/rating/movies/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_= 'movieItem_info'))
#     mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
#     mes_label.place(x=10,y=10)

# def get_fact():
#     clear()
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_ = 'p-2 clearfix'))
#     mes_label = Message(text=res.text, font=('Arial', 24), fg ='black', width=680, borderwidth=0)
#     mes_label.place(x=10,y=10)
#     window.after(5000, menu)

# def get_festival():
#     clear()
#     response = requests.get('https://kudago.com/msk/festival/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='post-content'))
#     mes_label = Message(text=res.text, font=('Arial', 12), fg='black', width=680, borderwidth=0)
#     mes_label.place(x=130, y=10)
#     window.after(5000, menu)

# def clear():
    
#     all_widg = window.place_slaves()
#     for widg in all_widg:
#         widg.destroy()

# window = Tk()
# window.title('Мой первый проект')
# window.geometry('700x600')

# label_title = Label(text = 'Что вы хотите сделать?', font=('Arial', 24), fg='white', bg = 'red')
# label_title.place(width=700, height=50, x=0, y=0)

# b1 = Button(text='узнать что-то новое', font=('Arial', 24), fg='black', command = get_fact)
# b1.place(x=25,y=75, width=300)
# b2 = Button(text='куда сходить', font=('Arial', 24), fg='black', command = get_festival)
# b2.place(x=375,y=75, width=300)
# b3 = Button(text='какой фильм посмотреть', font=('Arial', 12), fg='black', command=get_film)
# b3.place(x=200,y=160, width=300)

# window.mainloop()



# import telebot
# from tkinter import *
# from bs4 import BeautifulSoup
# import requests
# import random
# # from DS.settings_bot import *
# token = '5829038962:AAEEHx0NeBTjmSFWFCf0Q-dCTSlY7grTSSo'

# bot = telebot.TeleBot(token)

# def get_fact():
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='p-2 clearfix'))
#     return [res.text,  ]

# def my_decorator(func_to_decorate): # декоратор
#     def decorated_func(): # обертка
#         print('Я начинаю работать!') # код, который выполнится перед функцией
#         func_to_decorate()    # функция, которую мы оборачиваем
#         print('Я устал')   #код, который выполнится после функции
#     return decorated_func

# @my_decorator
# def my_func():
#     print('Я начинаю работать')

# @my_decorator
# def func2():
#     print('!!!!!111111!!!!!')

# my_func()

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     weolcome_text = '''
#     Добро пожаловать!!!!
#     '''
#     bot.send_message(message.chat.id, weolcome_text)
    

# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     text = get_fact()
#     bot.send_message(message.chat.id, text=[0])
#     bot.send_message(message.chat.id, text=[1])

# import requests
# from bs4 import BeautifulSoup
# import random
# import telebot
# from telebot import types
# # from DS.settings_bot import *  # не пишите это!!!!!!!!!!!!
# token = '5641833016:AAFsclZv733Gow39pYbP5VYMJ2lrpfGnXjU'     # а эту пишите!!!!!!!!!!!!

# bot = telebot.TeleBot(token)

# game_advice = ['Resident Evil 7:Biohazard','Mortal Kombat 11','DOOM ETERNAL','Grand Theft Auto 5','Super Meat Boy']



# @bot.message_handler(commands=['random_game'])
# def send_advice(message):
#     games = ['Dota', 'StarCraft II', 'CS:GO']
#     correction = input("Укажите жанр игры (стратегия, моба, шутер): ")
#     if correction == "стратегия":
#         game = "StarCraft II"
#     elif correction == "моба":
#         game == "Dota 2"
#     elif correction == "шутер":
#         game == "CS:GO"
    
#     bot.send_message(message.chat.id, game)

# def get_fact():
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     res = random.choice(html.find_all(class_='p-2 clearfix'))
#     return [res.text, res.a.attrs['href']]


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
    
#     welcome_txt = '''
#     Добро пожаловать!
#     Добро пожаловать!
#     Добро пожаловать!
#     '''

#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#     button1 = telebot.types.KeyboardButton('Факт')
#     button2 = telebot.types.KeyboardButton('Игра')
#     keyboard.add(button1, button2)

#     bot.send_message(message.chat.id, welcome_txt)




# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     text = get_fact()
#     bot.send_message(message.chat.id, text[0])
#     bot.send_message(message.chat.id, text[1])
    

# @bot.message_handler(content_types='text')
# def message_reply(message):
#     bot.send_message(message.chat.id, message.text)



   

# bot.polling()




# n = int(input())
# lst = list()
# for i in range(n): lst.append(int(input()))
# print(lst)
# _min = min(lst)
# ind_min = lst.index(_min)
# _max = max(lst)
# ind_max = lst.index(_max)
# lst[ind_min] = _max
# lst[ind_max] = _min
# print(lst)




# from tkinter import *
# window = Tk()
# window.geometry('800x600')

# canvas = Canvas(window, width = 800, height=600, bg='white')
# canvas.pack()

# canvas.create_rectangle(10,10, 10,10, fill = 'black', outline='green')

# canvas.create_rectangle(200,200,200,200, fill = 'red', outline='white')

# canvas.create_rectangle(400,400,400,400, fill = 'pink', outline='blue')

# canvas.create_polygon(200, 200, 100, 400, 300, 400, fill='gold')
# canvas.create_rectangle(100,400, 300, 600, fill='yellow')
# canvas.create_rectangle(150,500, 200, 600, fill='black')



# class House:
#     def __init__(self, wall_color, roof_color, height, width):
#         self.wall_color= wall_color
#         self.roof_color = roof_color
#         self.height = height
#         self.width = width
#         self.height_roof = 70
#         self.roof = None
#         self.wall = None

#     def build_house(self, x, y):    
#         w = self.width
#         h = self.height
#         h_roof = self.height_roof
#         self.roof = canvas.create_polygon(x, y, x - w/2, y + h_roof, x + w/2,y + h_roof, fill=self.roof_color)
#         self.wall = canvas.create_rectangle(x - w/2, y + h_roof, x + w/2 + 20, y + h, fill = self.wall_color, outline = '')

#     def print_info(self):
#         print(f'Цвет крыши - {self.roof_color}')
#         print(f'Цвет стен - {self.wall_color}')
#         print(f'Высота дома - {self.height}')
#         print(f'Ширина дома - {self.width}')
#         print(f'Высота крыши - {self.height_roof}')

# house_1 = House('red', 'gold', 300, 200)    
# house_1.build_house(100, 10)

# house_1.print_info()
# print('-'*100)
# house_1.print_info()


# house_1.roof_color = 'black'

# window.mainloop()



# import random

# class Warrior:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#     def hit(self, target):
#         if type(self) == type(target):
#             target.health -= 20
#         else:
#             raise TypeError

# check = 1

# warriors = [Warrior('Юнит1'), Warrior('Юнит2')]
# while check == 1:
#     q = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
#     if q == '1':
#         i = random.randint(0, 1)
#         attacker, victim = warriors[i], warriors[i - 1]
#         attacker.hit(victim)
#         print(attacker.name, 'атаковал', victim.name)
#         print('У', victim.name, 'осталось здоровья', victim.health)
#         if victim.health <= 0:
#             print(attacker.name, 'победил!!!')
#             break
#     elif q == '2':
#         break
#     else:
#         print('Ошибка ввода')

# import random 

# check = 1

# unitts = None
# unit1 = None
# unit2 = None

# units = [unit1, unit2]

# health1 = 100
# health2 = 100

# healthss = [health1, health2]

# while check == 1:
#     inputtattack = input('Напишите 1, чтобы кто-то кого-то атаковал:')
#     if inputtattack == 1:
#         unitts = random.choice(units)
#     if unitts == unit1:
#         print('Первый юнит атаковал второго')
#         health2 -= 20
        
#     elif unitts == unit2:
#         print('Второй юнит атаковал первого')
#         health1-=20
#     print(health1, health2)

# if health2 <= 0:
#     print('Первый юнит победил')
# if health1 <= 0:
#     print('Второй юнит победил')




    
# while True:
#     choice = input("Выберите другие операции или дискриминант ")
#     if choice == "дискриминант":
#         a = int(input("Введите значение a "))
#         b = int(input("Введите значение b "))
#         c = int(input("Введите значение c "))
#         print(b*2 - 4*a*c)

#     if choice == "другие операции":
#         num1 = int(input("Введите первое число : "))
#         num2 = int(input("Введите второе число: "))
#         operation = input("Введите операцию(+, -, * или /): ")
#         if operation == ("+"):
#             print (num1 + num2)
#         elif operation == ("-"):
#             print (num1 - num2)
#         elif operation == ("*"):
#             print (num1 * num2)
#         elif operation == ("/"):\
#             print (num1 / num2)
#         else:
#             print('Ошибка')

           

    



# from tkinter import *
# import random

# class Knight:
#     def __init__(self):
#         self.x = 70
#         self.y = h // 2
#         self.v = 0
#         self.v_x = 0
#         self.img = PhotoImage(file='knight.png')
    
#     def up(self, event):
#         self.v = -6

#     def down(self, event):
#         self.v = 6

#     def stop(self, event): 
#         self.v = 0
#     def right(self, event):
#         self.v_x = 6
#     def left(self, event):
#         self.v_x = -6
#     def stop_all(self, event): 
#         self.v = 0 
#         self.v_x = 0 

# class Dragon:
#     def __init__(self):
#         self.x = w - 50
#         self.y = random.randint(100, h - 30)
#         self.v = random.randint(1, 6)
#         self.img = PhotoImage(file='dragon.png')

# def game():
#     canvas.delete('all')
#     canvas.create_image(w // 2, h // 2, image=bg_img)
#     canvas.create_image(knight.x, knight.y, image=knight.img)
#     knight.y += knight.v
#     knight.x += knight.v_x

#     if knight.y < 0:
#         knight.y = 0
#     if knight.y > h - 96:
#         knight.y = h - 96
#     if knight.x < 0:
#         knight.x = 0
#     if knight.x > w - 96:
#         knight.x = w - 96
    
    
#     current_dragon = 0
#     dragon_to_kill = -1
    
#     for dragon in dragons:
#         canvas.create_image(dragon.x, dragon.y, image= dragon.img)
#         dragon.x -= dragon.v


#         if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) <= 98 ** 2:
#             dragon_to_kill = current_dragon
#         current_dragon += 1

#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w//2, h//2, text ='Ты проиграл!', font = 'Verdana 42', fill='red')
#             break

#     if dragon_to_kill >= 0:
#         del dragons[dragon_to_kill]
#     if len(dragons) == 0:
#         canvas.delete('all')
#         canvas.create_text(w//2, h//2, text ='Ты победил!', font = 'Verdana 42', fill='red')
#     else:
#         window.after(50, game)


   

# window = Tk()

# w = 600
# h = 600

# window.geometry(f'{w}x{h}')

# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_ = window, x=0, y=0)
# bg_img = PhotoImage(file='bg_2.png')

# knight = Knight()
# dragons = []
# for i in range(3):
#     dragons.append(Dragon())

# dragon = Dragon()

# game()

# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<KeyRelease>', knight.stop)
# window.bind('<Key-Left>', knight.left)
# window.bind('<Key-Right>', knight.right)
# window.bind('<KeyRelease>', knight.stop_all)

# window.mainloop()



# var_1 = True
# var_2 =False

# var_3 = 5 == 3

# lst= []
# st = 'dsjjfjsdf'

# if var_3:
#     pass
# else:
#     print('ложь')

# hour = 5
# if hour >= 0 and hour <= 4 or hour == 23:
#     print('ночь')
# elif 5 <= hour <= 10:
#     print('утро')
# elif 11 <= hour <= 17:
#     print('день')
# else:
#     print('Вечер')

    

# import requests
# from pprint import pprint

# starships = []

# def get_people(url):
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()
#         print(response)
# def get_planets(url):
#     diameters = []
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         diameters.append({response.get('name'): response.get('diameter')})
#         pprint(response)
# def get_starships(url):
#     for i in range(1,6):
#         starships = []
#         response = requests.get(f'{url}/{i}').json()
#         starships.append({response.get('starships')})
#         pprint(response)
  
# url = 'https://swapi.dev/api/'


# response = requests.get(url).json()
# # print(response)
# # pprint(response)


# people_api_url = response.get('people')
# planets_api_url = response.get('planets')
# starships_api_url_1 = response.get('starships')
# starships_api_url_2 = response.get('starships')
# strsh_1 = get_starships(starships_api_url_1)
# strsh_1.append(starships)
# strsh_2 = get_starships(starships_api_url_2)
# strsh_2.append(starships)

# res = list(set[0] & set[1])
# print(res)




# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# today = datetime.today().strftime('%d/%m/%Y')

# url = 'https://www.cbr.ru/scripts/XML_daily.asp?'

# responce = requests.get(url, params={'date_req': today})

# xml = BeautifulSoup(responce.content, 'html.parser')

# def get_course(id, k):
#     rez = xml.find('valute', {'id': id})
#     val = float(rez.value.text).replace(',', '.')
#     file.write(f'')
#     print(f'{k} {rez.charcode.text} = {round(k * val, 2)} RUB\n')

# file = open('urok_6_2.txt', 'r')
# file.write(f'Курс валют на {today}')

# k = (int(input('Введите кол-во валюты: ')))
# print(f'Курс валют на {today}')
# get_course('R01235', k)
# get_course('R01239', k)
# get_course('R01035', k)
 
# for rows in file.readlines():
#     print(rows)
# print(file.readline())
# file.close()

# import random
  
# class Unit:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def hit(self, damage):
#         if type(self) == type(damage):
#             damage.health -= 20
        
# Units = [Unit('игрок 1', 100), Unit('игрок 2', 100)]

# while True:
#     choice = input("Введите 1, чтобы кто-то атаковал: ")
#     if choice == '1':
#         i = random.randint(0,1)
#         attacker, attacked = Units[i], Units[i - 1]
#         attacker.hit(attacked)
#         print(attacker.name, ' атаковал ', attacked.name)
#         print('у ' + str(attacked.name) + str(attacked.health) + ' здоровья')
#         if attacked.health <= 0:
#             print(attacker.name, ' победил')
#             break
#         elif choice != '1':
#             print("Ошибка ввода")


# valute_from = "EUR" 
# valute_to = "USD" 
# amount = int(input("Введите количество денег: ")) 
 
# def course(valute_from, valute_to, amount): 
#     rates = { 
#         "RUR": 1.0, 
#         "USD": 63.0, 
#         "EUR": 75.0 
#     } 
     
#     if valute_from == "RUR": 
#         return amount / rates[valute_to] 
#     else: 
#         return amount / rates[valute_from] * rates[valute_to] 
 
# print("Converted amount:", course(valute_from, valute_to, amount))



# def summ(a,b,*args, f=0, **kwargs):
#    print(a,b,args,f)
#    print(kwargs.get('flag'))

# summ(1,3,7,10, f=11, flag = True, f_2=5)

# a = 5
# b = 8
# if a > b:
#     print('+')
# else:
#     print('-')

# print('+' if a > b else '-')

# c = 10 if a == b else 0
# print(c)

# val = 2
# if val is None:
#     rez = []
# else:
#     rez = val

# print(rez)
# rez = [] if val is None else val
# print(rez)
# rez = val or []
# print(rez)

# lst = []
# for i in range(0, 301):
#     if i % 31 == 0:
#         lst.append(i)
#     if i % 30 == 0:
#         lst.append(i)
# print(lst)

# lst = [i for i in range(301) if i % 30 == 0]
# print(lst)
# lst = [i for i in range(301) if i % 31 == 0]
# print(lst)

# lst_2 = [i ** 2 if i < 50 else i for i in range(0,101) if i % 12 == 0]
# print(lst_2)

# lst_1 = []
# for i in range(101):
#     lst_1.append(i)

# print(lst_1)

# lst_2 = [i for i in range(101)]
# print(lst_2)

# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType
# from pprint import pprint
# from course import *
# from random import randint
# from wiki import *

# token = 'vk1.a.mMWT43dyKOVPJkBYLq5Vuk1pVR3ZjzuPtX16oxLwEl_HX_gVbZ7nf8AfktqTEj2qrvTLD8SHcDuMbk2iYUI4MfrJeLucDWjvrr_YSWMihKHjN5nQgZ-QLCLiX775fwej5QVsqDCqMOk-vvLZA3wx2keANrY-W4gK6oPrp5o-bFNYZFUTEtl5YiJsXnpXxriu2s3TuByKtzxKxchJIa-Neg'

# vk_session = vk_api.VkApi(token = token)

# vk = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)

# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         msg = event.text.lower()
#         user_id = event.user_id
#         msg_id = randint(1, 10 ** 7)
#         print(msg)
#         if msg[:2] == '-к':
#             res = f'1 $ = {get_course("R01235")}'
#         elif msg.startswith('-в'):
#             res = get_wiki_article(msg[3:])
#         else:
#             res = 'Не понимаю, что ты хочешь'
#         vk.messages.send(user_id = user_id, random_id = msg_id, message = res)
#         print(res)


# import time

# t1 = time.time()
# lst = (time.sleep(i) for i in range(1,4))
# t2 = time.time()

# print(lst, t2-t1)

# t1 = time.time()
# for elem in lst:
#     print(elem)
# t2 = time.time()
# print(t2 - t1)

# r = range(1, 10000000)
# print(r)

# # for i in r:
# #     print(i)


# def not_lazy_func():
#     for i in range(5):
#         return i
    

# def lazy_func():
#     for i in range(5):
#         print('до i')
#         yield i
#         print('после i')
    

# print(lazy_func())

# for elem in lazy_func():
#     print(elem)



# lst = [1, 2, 5]
# def lazy_func(my_lst):
#     # for elem in my_lst:
#     #     yield my_lst
#     yield from my_lst

# for i in lazy_func(lst):
#     print(i)

# f = open('1.txt', 'w')
# f.write('hi')
# f.close()

# with open('1.txt', 'w') as f:
#     f.write('hiieritepwiortiupioeritpoieortiepr')
#     print(f.closed)
# print(f.closed) 



# import contextlib

# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Вошли в менеджер контекста.')
#     yield my_str[::-1]
#     print('Выходим из контекстного менеджера...')

# with str_reverse('hello') as s:
#     print(f'Выполняем действия: {s}')

# import contextlib

# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print(f'Произошло исключение - {exc}')

# with exc_handler(IndexError):
#     lst = [2, 4, 5]
#     print(lst[783748374])
#     print(2)

# print(1)

# def func(*args, **kwargs):
#     print(f'Арги: {args}\nКварги: {kwargs}')

# func(1,18,32,3,32,13,3, a = 3, x = 7, z = 1203919428)





# with open('1.txt')as f:
#     print(f.readline())


# import time

# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#     def __enter__(self):
#         self.start = time.time()
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         t = time.time() - self.start
#         print(f"Время выполнения программы: {t}")
#         # print(f'{exc_type}\n, {exc_val}\n, {exc_tb}\n')
#         print(exc_type, exc_val, exc_tb, sep='\n')
#         return True


# with RunningCodeJudge() as t1:
#     lst = [i for i in range(10000)]
#     print(t1)
#     lst - 1

# lst = [1,2,3]
# my_iterator  = iter(lst)
# print(my_iterator)

# for i in my_iterator:
#     print(i)

# from random import randint

# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.__reload = limit
#     def __iter__(self):
#         self.limit = self.__reload
#         return self
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit -= 1
#         return randint(1, 100)
    
# rand_iter = RandomIter(5)
# # print(iter(rand_iter))
# for i in rand_iter:
#     print(i)

# for i in rand_iter:
#     print(i)


# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
    
#     def get_days(self):
#         return self.__days 
#     def get_season(self):
#         return self.__season
    
#     def set_days(self, days):
#         # if days == 365 or days == 366:
#         #     self.__days = days
#         # else:
#         #     raise Exception('Некорректоное значение')

#         if days != 365 and days != 366:
#             raise Exception('Некорректоное значение')
#         self.__days = days
        
           

#     def set_season(self, season):
#         self.__season = season

# year = Year(365, 'summer')
# year.set_days(300)
# print(year.get_days(), year.get_season(), sep = '\n')


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
# person = Person('Tom', 56)
# person.name = 'Tim'
# print(person.name)


# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season

#     @property
#     def days(self):
#         return self.__days
#     @days.setter
#     def days(self, days):
#         self.__days = days

# year = Year(365, 'winter')
# year.days = 366
# print(year.days)



# class Item:
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other

# item_1 = Item('Монитор', 20_000, 5)
# item_2 = Item('Видеокарта', 15_000, 0.8)

# # print(item_1.price * item_1.weight + item_2.price * item_1.weight)
# # print(item_1 + item_2)
# # print(type(item_1), isinstance(item_1, Item) sep = '\n')
# print(item_1 + item_2)



# from tkinter import *
# from random import randint 

# window = Tk()
# window.geometry('600x600')
# canvas = Canvas(window, width=600, height=600)
# canvas.pack()

# class Fire:
#     image = PhotoImage(file='fire.png').subsample(4,4)

#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Clay

# class Wind:
#     image = PhotoImage(file='wind-sign.png').subsample(4,4)

# class Earth:
#     image = PhotoImage(file='plant.png').subsample(4,4)

#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
        
# class Water:
#     image = PhotoImage(file='watering.png').subsample(4,4)

# class Clay:
#     image = PhotoImage(file='clay.png').subsample(4,4)

# class Wood:
#     image = PhotoImage(file = 'wood.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Earth
# class Arg:
#     image = PhotoImage(file = 'argentum.png').subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Wind):
#             return Water

# def move(event):
#     image_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y +10)
#     if len(image_id) == 2:
#         elem_1 = elements[image_id[0] - 1]
#         elem_2 = elements[image_id[1] - 1]
#         elem_3 = elements[image_id[4] - 1]
#         elem_4 = elements[image_id[5] - 1]
#         new_elem = elem_1 + elem_2
#         new_elem_2 = elem_3 + elem_1
#         new_elem_3 = elem_4 + elem_2
#         if new_elem not in elements:
#             elements.append(new_elem)
#             canvas.create_image(event.x, event.y, image = new_elem.image)
#         elif new_elem_2 not in elements:
#             elements.append(new_elem_2)
#             canvas.create_image(event.x, event.y, image = new_elem_2.image)
#         elif new_elem_3 not in elements:
#             elements.append(new_elem_3)
#             canvas.create_image(event.x, event.y, image= new_elem_3.image)
#     canvas.coords(image_id, event.x, event.y)


# elements = [Fire(), Water(), Wind(), Earth(), Wood()]
# for elem in elements:
#     canvas.create_image(randint(50, 350), randint(50, 350), image = elem.image)

# window.mainloop()



# import pprint

# goods = [{'name': 'Pudge', 'brand': 'top tower', 'price': 'crystal maiden'},
#         {'name': 'TideHunter', 'brand': '3-ka', 'price': 'kunkka'},
#         {'name': 'MK', 'brand': 'MID', 'price': 'LINA'}]

# def item_price(item):
#     return item['price']

# print(sorted(goods, key = lambda item: item['price']))

# ttower_list = list(filter(lambda item: item['brand'] == 'top tower', goods))
# print(ttower_list)

# indexes_list = []
# k = 0
# for i in goods:
#     indexes_list.append({k:i})
#     k += 1
# pprint(indexes_list)

# import sqlite3


# try:
#     connection = sqlite3.connect('lesson_bd.db')
#     cursor = connection.cursor()

# except sqlite3.DatabaseError:
#     print('Ошибка при работе с БД')
# finally:
#     connection.close()

# with sqlite3.connect('lesson_db.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute('CREATE TABLE IF NOT EXISTS (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# import sqlite3 

# class Database:
#     def __init__(self, db):
#         self.connection = sqlite3.connect(db)
#         self.cursor = self.connection.cursor()

#     def create_table(self):
#         with self.connection:
#             self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

#     def add_user(self, name, age):
#         with self.connection:
#             return self.cursor.execute('INSERT INTO users(name,age) VALUES (?,?)', (name,age))
    
#     def get_users_list(self):
#         with self.connection:
#             return self.cursor.execute("SELECT * FROM users").fetchall()
    
#     def get_user(self, user_id):
#         with self.connection:
#             return self.cursor.execute("SELECT name, FROM users WHERE id = ?", (user_id, )).fetchall()
    
#     def update_user_age(self, user_id, age):
#         with self.connection:
#             return self.cursor.execute("SELECT name, age FROM users WHERE id = ?", (user_id, )).fetchall()
    
#     def del_user(self, user_id):
#         with self.connection:
#             self.cursor.execute('DELETE FROM users WHERE if = ?', (user_id, ))

#     def del_all_users(self):
#         with self.connection:
#             self.cursor.execute*'DELETE FROM users'
    
#     def user_gender(self, user_id, gender):
#         with self.connection:
#             return self.cursor.execute("SELECT name, age, gender FROM users Wherer if = ?", (user_id, )).fetchall()


# if __name__ == '__main__':
#     db = Database('lesson_bd.db')
#     # db.create_table()
#     db.add_user("DIMA", 21)
#     print(db.get_users_list())
#     print(db.get_user(6))
#     db.add_user('Dima', 21)
#     db.del_user(2)
#     print(db.get_users_list())
#     db.del_all_users()
#     print(db.get_users_list())
#     db.add_user('Dima', 77231, 'Male')
#     print(db.get_users_list())




# 1 1 1 1


# name = input('Введите имя сотрудника: ')
# salary = int(input('Зарплата сотрудника в месяц: '))
# print(f'У {name} зарплата в год {salary * 12}')

# ['name', 'age', 'salary']

# emplyees_list = [{   
#                     'name': 'Данил', 
#                     'salary': '100_000'
#                 },

#                 {
#                     'name': 'Ваня',
#                     'salary': 200_000
#                 }{
#                     'name': 'Олег'
#                     'salary': 50_000
#                 }]


# for employee in emplyees_list:
#     if employee['name'] == 'Ваня':
#         emplyees_list.remove(employee)
#         break

# emplyees_list.append({'name': 'Кирилл', 'salary': 30_000})

# for employee in emplyees_list:
#     print(f' У {employee.get("name")} зарплата за год составляет {employee.get("salary") * 12} рублей.')
# print(emplyees_list)

# list_1 = []

# class Employee:
#     def __init__(self, name, salary, on_work, on_vocation, is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.on_work = True
#         self.on_vocation = on_vocation
#         self.is_good_employee = is_good_employee

#     def get_info(self):
#         print(f'У {self.name} зарплата за год составляет {self.salary * 12} рублей')

# good_employee = bool(input('Хорошо ли работал этот сотрудник? (введите True, если да и не заполняйте поле, если нет) - ')) 

# dict_1 = {} 
#     dict_1['name'] = Employee.name 
#     dict_1['good_job'] = Employee.is_good_employee 
#     list_1.append(dict_1) 

# for a in range(len(list_1) - 1, -1, -1): 
#     if list_1[a]['good_job'] == False: 
#         del list_1[a] 
 

# def get_info_employees(employees_list):
#     for employee in employees_list:
#         employee.get_info()

# def get_info_employee(employees_list, name):
#     for employee in employees_list:
#         if employee.name == name:
#             employee.get_info()
# def get_info_employee_vocation(employeers_list, on_vocation):
#     for employee in employeers_list:
#         if employee.on_vocaion == True:
#             employee.get_info_employee()

# employees_list = [ 
#     Employee('Даниил', 100_000),
#     Employee('Ваня', 200_000)
#     Employee('Олег', 50_000)
# ]

# # get_info_employees(employees_list)
# # get_info_employee(employees_list, employees_list.name)

# while True:
#     print('1 - получить информацию о всех сотрудниках')
#     print('2 - получить информацию об одном сотруднике')
#     k = input('Введите номер команды: ')
#     if k == 1:
#         get_info_employees(employees_list)
#     if k == 2:
#         get_info_employee(employees_list)
#     if k == 3:
#         break




# 12 12 12 12

# import os
# path = r'e:\vscode\python\lesson.py'
# current_path = os.path.abspath(__file__)
# parent_path = os.path.joun(current_path, '..')


# print(current_path)

# import sys
# sys.setrecursionlimit(3000)

# def f(n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return 4 * f(n-1)

# print(f(2300) / f(2290))


