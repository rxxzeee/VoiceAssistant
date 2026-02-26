import webbrowser
import time
import pyautogui

def play_youtube_music(speak):
    speak("Вмикаю музику на ютубі. Приємного прослуховування!")
    webbrowser.open("https://music.youtube.com/")
    time.sleep(6)
    pyautogui.press('space')

def open_youtube(speak):
    speak("Яке відео подивимось сьогодні?")
    webbrowser.open("https://youtube.com/")

def open_weather(speak):
    speak("Зараз відкрию сайт із прогнозом погоди.")
    webbrowser.open("https://sinoptik.ua/")

def watch_films(speak):
    speak("Відкриваю сайт для перегляду фільмів. Приємного перегляду!")
    webbrowser.open("https://hdrezka.inc/")

def watch_sport_news(speak):
    speak("Ось добірка новостей у спорті.")
    webbrowser.open("https://sport.ua/")

def food_order_site(speak):
    speak("Відкриваю сайт доставки. Смачного!")
    webbrowser.open("https://glovoapp.com/uk/ua/kyiv-right-bank/categories/food_1?")

def view_github_page(speak):
    speak("Можете переглянути свої досягнення тут.")
    webbrowser.open("https://github.com/rxxzeee/")

def open_elearn(speak):
    speak("Відкриваю навчальний портал. Бажаю плідного навчання!")
    webbrowser.open("https://elearn.nubip.edu.ua/login/index.php/")

def open_twitch(speak):
    speak("Час розважитись на стрімах!")
    webbrowser.open("https://twitch.tv/")

def watch_travel_channel(speak):
    speak("Про яку країну хотіли б дізнатись?")
    webbrowser.open("https://youtube.com/@alexshevtsov?si=3qZz-hFVnYGDCnLp")