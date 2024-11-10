import time
from datetime import datetime
import csv
import tkinter as tk
from tkinter import messagebox
from threading import Thread
import pygame  # For controlling audio playback

# Initialize pygame mixer
pygame.mixer.init()

file = 'Raw Data.csv'  # global
stop_monitoring = False  # Global flag to control the alarm monitoring

def fetch_light_data(csv_filename):
    with open(csv_filename, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for row in csv_reader:
            try:
                illuminance = float(row[1])
                
                # Check if the illuminance value is greater than 1000 lux
                if illuminance > 1000:
                    return True
                
            except (ValueError, IndexError):
                # Ignore rows with non-numeric illuminance values or missing data
                continue
    return False

def check_time_range(start_hour, end_hour):
    now = datetime.now()
    return start_hour <= now.hour < end_hour

def trigger_alarm():
    # Create a new window for the alarm
    alarm_window = tk.Toplevel(root)
    alarm_window.title("Alarm Triggered!")
    alarm_window.geometry("300x150")
    alarm_window.configure(bg="red")

    # Display message
    label = tk.Label(alarm_window, text="Alarm! Light detected.", bg="red", fg="white", font=("Helvetica", 16))
    label.pack(pady=20)

    # Stop alarm button in the new window
    stop_button = tk.Button(alarm_window, text="Stop Alarm", command=lambda: stop_alarm(alarm_window))
    stop_button.pack(pady=10)

    # Play the alarm sound in a separate thread
    Thread(target=play_alarm_sound).start()

def play_alarm_sound():
    pygame.mixer.music.load('song.mp3')  # Replace with the path to your alarm sound file
    pygame.mixer.music.play(-1)  # Loop the alarm sound until stopped

def stop_alarm(alarm_window=None):
    global stop_monitoring
    stop_monitoring = True  # Stop monitoring
    pygame.mixer.music.stop()  # Stop the alarm sound
    if alarm_window:
        alarm_window.destroy()  # Close the alarm window if it exists

def monitor_light(start_hour, end_hour, file):
    global stop_monitoring
    stop_monitoring = False
    while not stop_monitoring:
        light_detected = fetch_light_data(file)
        if light_detected and check_time_range(start_hour, end_hour):
            trigger_alarm()
            break
        time.sleep(10)

def set_alarm():
    start_hour = int(entry1.get())
    end_hour = int(entry2.get())
    messagebox.showinfo("Alarm", f"Alarm will monitor from {start_hour}:00 to {end_hour}:00.")
    Thread(target=monitor_light, args=(start_hour, end_hour, file)).start()

# Create the main window
root = tk.Tk()
root.title("Black Themed GUI")
root.geometry("300x250")
root.configure(bg="black")

# Configure the style
label_style = {"bg": "black", "fg": "white"}
entry_style = {"bg": "black", "fg": "white", "insertbackground": "white"}
button_style = {"bg": "black", "fg": "white"}

# Create the first label
label1 = tk.Label(root, text="Start Hour:", **label_style)
label1.pack(pady=5)

# Create the first entry
entry1 = tk.Entry(root, **entry_style)
entry1.pack(pady=5)

# Create the second label
label2 = tk.Label(root, text="End Hour:", **label_style)
label2.pack(pady=5)

# Create the second entry
entry2 = tk.Entry(root, **entry_style)
entry2.pack(pady=5)

# Create a Set Alarm button
button_set = tk.Button(root, text="Set Alarm", command=set_alarm, **button_style)
button_set.pack(pady=10)

# Run the application
root.mainloop()

def main():

    monitor_light(start_hour, end_hour, file)



if __name__ == "__main__":
    main()
