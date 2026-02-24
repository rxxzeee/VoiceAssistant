import webbrowser
import time
import pyautogui

def play_youtube_music(speak):
    speak("Вмикаю музику на ютубі. Приємного прослуховування!")
    webbrowser.open("https://music.youtube.com/")
    time.sleep(6)
    pyautogui.press('space')

def open_weather(speak):
    speak("Зараз відкрию сайт із прогнозом погоди.")
    webbrowser.open("https://sinoptik.ua/")