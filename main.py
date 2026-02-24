import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import webbrowser
import time
import pyautogui

def listen_command():
    fs = 44100  # Частота дискретизації
    seconds = 5  # Скільки секунд слухати команду
    
    print("\nСлухаю 5 секунд... (говори команду)")
    
    # 1. Записуємо звук у масив за допомогою sounddevice
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Чекаємо завершення 5 секунд
    
    # 2. Зберігаємо у тимчасовий аудіофайл
    sf.write('temp_command.wav', myrecording, fs)
    
    recognizer = sr.Recognizer()
    try:
        # 3. Згодовуємо файл модулю розпізнавання
        with sr.AudioFile('temp_command.wav') as source:
            audio = recognizer.record(source)
            
        command = recognizer.recognize_google(audio, language="uk-UA").lower()
        print(f"Розпізнано: {command}")
        return command
    except sr.UnknownValueError:
        print("Не вдалося розпізнати слова.")
        return ""
    except Exception as e:
        print(f"Помилка: {e}")
        return ""

# Далі йде твоя функція execute_command() без змін

def execute_command(command):
    """Виконує дії на основі отриманої команди."""
    
    # Словник або умови для команд
    if "музик" in command or "youtube music" in command:
        print("Відкриваю YouTube Music...")
        # 1. Відкриваємо сайт
        webbrowser.open("https://music.youtube.com/")
        
        # 2. Чекаємо завантаження сторінки
        # Час залежить від швидкості ПК та інтернету, можливо, доведеться збільшити
        time.sleep(6) 
        
        # 3. Імітуємо натискання пробілу
        # На YouTube Music пробіл працює як Play/Pause для останнього треку
        pyautogui.press('space')
        print("Музика увімкнена!")

    elif "погод" in command:
        print("Відкриваю прогноз погоди...")
        webbrowser.open("https://sinoptik.ua/")
        
    elif "до побачення" in command or "вимкнись" in command:
        print("Завершую роботу. Бувай!")
        return False
        
    else:
        print("Команда не підтримується або не розпізнана.")
        
    return True

def main():
    print("Асистент готовий до роботи!")
    running = True
    while running:
        command = listen_command()
        if command:
             running = execute_command(command)

if __name__ == "__main__":
    main()