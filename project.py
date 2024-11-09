import time
from datetime import datetime

def fetch_light_data():
    """
    Replace this function with the actual data-fetching logic
    from the light-sensing app, such as a request to an API or
    reading a file/database.
    """
    # Placeholder for light-sensing data
    return True  # True means light detected, False means no light

def check_time_range(start_hour, end_hour):
    """Check if the current time is within the specified wake-up range."""
    now = datetime.now()
    return start_hour <= now.hour < end_hour

from pydub import AudioSegment
from pydub.playback import play

def play_sound():
    sound = AudioSegment.from_file("C:/path/to/your/soundfile.mp3")  # Use an absolute path
    play(sound)


def monitor_light(start_hour, end_hour):
    """Continuously checks for light detection within the specified wake-up hours."""
    while True:
        light_detected = fetch_light_data()
        if light_detected and check_time_range(start_hour, end_hour):
            play_sound()
            break  # Stop monitoring after triggering the alarm
        time.sleep(10)  # Check every 10 seconds (adjust as needed)

'''
import tkinter as tk
from tkinter import messagebox

def start_alarm():
    start_hour = int(start_hour_entry.get())
    end_hour = int(end_hour_entry.get())
    messagebox.showinfo("Alarm", f"Alarm will monitor from {start_hour}:00 to {end_hour}:00.")
    monitor_light(start_hour, end_hour)  # Start light monitoring

# Setup Tkinter UI
root = tk.Tk()
root.title("Light-Sensitive Alarm")

tk.Label(root, text="Start Hour:").grid(row=0, column=0)
start_hour_entry = tk.Entry(root)
start_hour_entry.grid(row=0, column=1)
start_hour_entry.insert(0, "6")  # Default start time

tk.Label(root, text="End Hour:").grid(row=1, column=0)
end_hour_entry = tk.Entry(root)
end_hour_entry.grid(row=1, column=1)
end_hour_entry.insert(0, "9")  # Default end time

start_button = tk.Button(root, text="Start Alarm", command=start_alarm)
start_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
'''
