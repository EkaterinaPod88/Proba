from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


t = 0
music = False


def set(): #создаем функцию для установки времени напоминания
    global  t
    rem = sd.askstring("Время напоминания", "Введите время напоминания в формате чч:мм (в 24 часовом формате")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t = dt.timestamp()
            print(t)
            text = sd.askstring("Текст напоминания", "Введите текст напоминания")
            lable.config(text=f"Надпоминание на {hour:02}: {minute:02} с текстом {text}")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка {e}")


def check(): # функция проверки
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(10000, check)# рекурсия когда функция вызывает себя

def play_snd(): # функция для игры музыки
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()


def stop_music(): # фукция для отключения музыки
    global music
    if music:
        pygame.mixer.stop()
        music = False
    lable.config(text="Установите новое напоминание")


window = Tk()
window.title("Напоминание")
lable = Label(text ="Установите напоминание", font=("Arial", 14))
lable.pack(pady=20)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()


stop_button = Button(text="Остановить музыку", command=stop_music)# кнопка остановки музыки
stop_button.pack()

check()


window.mainloop()