import time
from datetime import datetime
import csv
import tkinter as tk
from tkinter import messagebox, ttk
from threading import Thread
import pygame  # For controlling audio playback

# Initialize pygame mixer for sound control
pygame.mixer.init()

filename = 'Raw Data.csv'  # global
stop_monitoring = False  # Global flag to control the alarm monitoring

# Light data and time checking functions
def fetch_light_data():
    global filename
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for row in csv_reader:
            try:
                illuminance = float(row[1])
                if illuminance > 1000:  # Check if illuminance is above 1000 lux
                    return True
            except (ValueError, IndexError):
                continue
    return False

def check_time_range(start_hour, end_hour):
    now = datetime.now()
    return start_hour <= now.hour < end_hour

# Alarm trigger functions
def trigger_alarm():
    alarm_window = tk.Toplevel(root)
    alarm_window.title("Alarm Triggered!")
    alarm_window.geometry("350x200")
    alarm_window.configure(bg="#FFE4E1")  # Light pink for alarm background

    label = tk.Label(alarm_window, text="ALARM! Light detected.", bg="#FFE4E1", fg="black", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    stop_button = ttk.Button(alarm_window, text="Stop Alarm", command=lambda: stop_alarm(alarm_window), style="Stop.TButton")
    stop_button.pack(pady=10)

    Thread(target=play_alarm_sound).start()

def play_alarm_sound():
    pygame.mixer.music.load('song.mp3')  # Path to alarm sound file
    pygame.mixer.music.play(-1)  # Loop until stopped

def stop_alarm(alarm_window=None):
    global stop_monitoring
    stop_monitoring = True
    pygame.mixer.music.stop()
    if alarm_window:
        alarm_window.destroy()

# Main monitoring function
def monitor_light(start_hour, end_hour):
    global stop_monitoring
    stop_monitoring = False
    while not stop_monitoring:
        light_detected = fetch_light_data()
        if light_detected and check_time_range(start_hour, end_hour):
            trigger_alarm()
            break
        time.sleep(10)

def set_alarm():
    start_hour = int(entry1.get())
    end_hour = int(entry2.get())
    Thread(target=monitor_light, args=(start_hour, end_hour)).start()

# GUI Styling and Layout
root = tk.Tk()
root.title("Light Alarm App")
root.geometry("400x300")
root.configure(bg="#F0F8FF")  # Light blue background for readability

# Define styles
style = ttk.Style()
style.configure("TLabel", background="#F0F8FF", foreground="black", font=("Arial", 11))
style.configure("TEntry", fieldbackground="#FFFFFF", foreground="black")  # White entry box background
style.configure("TButton", background="#ADD8E6", foreground="black", font=("Arial", 10, "bold"), padding=10)
style.configure("Stop.TButton", background="#FF6347", foreground="black", font=("Arial", 10, "bold"), padding=10)
style.map("TButton", background=[("active", "#87CEFA")])  # Lighter blue for hover effect

# Title Label
title_label = tk.Label(root, text="Shine and Rise", bg="#F0F8FF", fg="black", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Start hour entry
label1 = ttk.Label(root, text="Start Hour:")
label1.pack(pady=5)
entry1 = ttk.Entry(root, style="TEntry")
entry1.pack(pady=5)

# End hour entry
label2 = ttk.Label(root, text="End Hour:")
label2.pack(pady=5)
entry2 = ttk.Entry(root, style="TEntry")
entry2.pack(pady=5)

# Set Alarm button
button_set = ttk.Button(root, text="Set Alarm", command=set_alarm, style="TButton")
button_set.pack(pady=20)



def main():
    
    # Run the application
    root.mainloop()

    
if __name__ == "__main__":
    main()
