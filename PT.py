import pygame
import tkinter as tk
import keyboard
import threading
import time

prayer_times = ["05:37", "07:08", "12:06","14:45","17:37","18:36"]  # Example times (24-hour format)

def freeze_pc():
    for key in ["esc", "alt", "tab", "ctrl", "shift", "win", "enter", "backspace"]:
        keyboard.block_key(key)
    
    def block_all_keys():
        while True:
            keyboard.write("")
            if not threading.main_thread().is_alive():
                break

    block_thread = threading.Thread(target=block_all_keys, daemon=True)
    block_thread.start()

def unfreeze_pc():
    keyboard.unhook_all()  # Unblock all keys

def play_sound():
    pygame.mixer.init()  # Initialize pygame mixer
    pygame.mixer.music.load("prayer.mp3")  # Replace with the path to your audio file
    pygame.mixer.music.play()

def show_popup():
    freeze_pc()  # Freeze the PC
    popup = tk.Tk()
    popup.title("Prayer Reminder")
    popup.geometry("300x150")
    popup.attributes("-topmost", True)  # Ensures the popup stays on top
    popup.resizable(False, False)  # Disable resizing of the popup

    # Play sound in a separate thread to avoid blocking the program
    threading.Thread(target=play_sound, daemon=True).start()

    # Add the label for the reminder
    label = tk.Label(popup, text="Time to pray!", font=("Helvetica", 16))
    label.pack(pady=20)

    # Dismiss button to close the popup and unfreeze the PC
    def dismiss():
        unfreeze_pc()
        popup.destroy()

    button = tk.Button(popup, text="Dismiss", command=dismiss)
    button.pack(pady=10)

    # Auto-dismiss the popup after 2 minutes (120,000 milliseconds)
    popup.after(120000, dismiss)
    popup.mainloop()

def check_prayer_time():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time in prayer_times:
            show_popup()
            time.sleep(60)  # Avoid triggering multiple times within a minute
        time.sleep(1)

# Run the prayer time checker in a separate thread
thread = threading.Thread(target=check_prayer_time, daemon=True)
thread.start()

print("Prayer notifier is running...")

