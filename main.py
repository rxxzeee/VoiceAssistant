import speech_recognition as sr
import webbrowser
import time 
import pyautogui
import os
from gtts import gTTS
import pygame

def speak(text):
    """Генерація голосу з тексту"""
    print(f"Ассистент: {text}")
    try:
        tts = gTTS(text=text, lang='uk')
        filename = "response.mp3"
        tts.save(filename)

        #ініціалізація мікшеру
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
        os.remove(filename)
    except Exception as e:
        print(f"Помилка відтворення голосу: {e}")
    
def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nСлухаю команду...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language="uk-UA".lower())
            print(f"Роспізнана команда: {command}")
            return command
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Не вдалося розпізнати команду")
        except sr.RequestError:
            print("Помилка з'єднання з GoogleAPI")
    
    return ""

def execute_command(command):
    if not command:
        return True
    
    if "музик" in command or "ютуб" in command:
        speak("Вмикаю музику на ютубі. Приємно прослуховування!")
        webbrowser.open("https://music.youtube.com/")
        time.sleep(6)
        pyautogui.press('space')
    elif "погод" in command:
        speak("Відкриваю сайт з прогнозом погоди")
        webbrowser.open("https://sinoptik.ua/")
    elif "до побачення" in command or "вимкнись" in command or "відпоч" in command:
        speak("Завершую роботую. До зустрічі!")
        return False
    else:
        speak("Я почув вашу команду але ще не вмію її оброблювати")
    return True

def main():
    speak("До ваших послуг готовий!")
    running = True

    while running:
        command = listen_command()
        if command:
            running = execute_command(command)

if __name__ == "__main__":
    main()