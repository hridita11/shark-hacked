import time
from datetime import datetime

def fetch_light_data():
    """
    Replace this function with the actual data-fetching logic
    from the light-sensing app, such as a request to an API or
    reading a file/database.
    """
    
    return True  

def check_time_range(start_hour, end_hour):
    """Check if the current time is within the specified wake-up range."""
    now = datetime.now()
    return start_hour <= now.hour < end_hour

from playsound import playsound 

def trigger_alarm():
    """Plays an alarm sound when triggered."""
    print("Alarm! Light detected.")
    playsound('song.mp3')
    """Replace with path to your alarm sound"""

def monitor_light(start_hour, end_hour):
    """Continuously checks for light detection within the specified wake-up hours."""
    while True:
        light_detected = fetch_light_data()
        if light_detected and check_time_range(start_hour, end_hour):
            trigger_alarm()
            break
        time.sleep(10)

def main():
    start_hour = 6
    end_hour = 20

    print(f"Monitoring light between {start_hour}:00 and {end_hour}:00...")
    monitor_light(start_hour, end_hour)


import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Black Themed GUI")
root.geometry("300x200")
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

# Define a function for the button click
def set_alarm():
    start_hour=int(entry1.get())
    end_hour=int(entry2.get())
    messagebox.showinfo("Alarm", f"Alarm will monitor from {start_hour}:00 to {end_hour}:00.")
    monitor_light(start_hour,end_hour)

# Create a button
button = tk.Button(root, text="Set Alarm", command=set_alarm, **button_style)
button.pack(pady=10)

# Run the application
root.mainloop()
