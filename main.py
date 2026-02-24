import speech_recognition as sr
import os
from gtts import gTTS
import pygame
import asyncio
import edge_tts
from mapping import COMMANDS_MAP

async def _generate_audio(text, voice, filename):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def speak(text):
    """Генерація нейромережевого голосу з тексту"""
    print(f"Асистент: {text}")

    voice = "uk-UA-OstapNeural"
    filename = "response.mp3"

    try:
        asyncio.run(_generate_audio(text, voice, filename))
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
    
    if "до побачення" in command or "вимкнись" in command or "можеш відпоч" in command:
        speak("Завершую роботу. До зустрічі!")
        return False

    # Пошук ключових слів у словнику
    for keyword, func in COMMANDS_MAP.items():
        if keyword in command:
            func(speak)
            return True
    speak("Я почув команду, але ще не вмію її виконувати")
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