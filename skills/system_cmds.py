import pyautogui
import subprocess
import os

# === БЛОК ГУЧНОСТІ НА КОМП'ЮТЕРІ ===
def volume_up(speak):
    speak("Роблю гучніше")
    for _ in range(5):
        pyautogui.press('volumeup')

def volume_down(speak):
    speak("Роблю тихіше")
    for _ in range(5):
        pyautogui.press('volumedown')

def mute_volume(speak):
    speak("Перемикаю звук")
    pyautogui.press('volumemute')

# === БЛОК ВІДКРИВАННЯ ПРОГРАМ ===
def start_work(speak):
    speak("Запускаю віжуалку. Вдалого програмування!")

    try:
        subprocess.Popen("code", shell=True)
    except Exception as e:
        speak("Не вдалося запустити програму автоматично.")
        print(f"Помилка: {e}")

def open_game(speak):
    speak("запускаю гру. Бажаю перемогти!")
    game_path = r"C:\Games\Riot Games\League of Legends\LeagueClient.exe"

    try:
        os.startfile(game_path)
    except FileNotFoundError:
        speak("Не можу знайти файл за вказаним шляхом.")