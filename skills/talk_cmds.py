import random
import datetime

howays = [
    "В мене все добре. А як ваші справи?",
    "Чудово. Чим займемося?",
    "Просто суперово. Готовий до ваших команд!"
]
helloes = [
    "Доброго ранку! З чого почнемо день?"
    "Доброго дня! Чим можу допомогти?"
    "Добрий вечір! Бажаєте відпочити чи попрацювати?"
]
wakeups = [
    "До ваших послуг!",
    "Слухаю вас!",
    "Чим можу допомогти?",
    "Завжди тут!"
]

def get_time_based_greeting():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if 6 <=current_hour < 12:
        return helloes[0]
    elif 12 <= current_hour <=18:
        return helloes[1]
    else:
        return helloes[2]
    
greeting = get_time_based_greeting
rand_wakeup =random.choice(wakeups)
rand_howay = random.choice(howays)

def helloe(speak):
    speak(greeting)

def howay(speak):
    speak(rand_howay)

def wakeup(speak):
    speak(rand_wakeup)