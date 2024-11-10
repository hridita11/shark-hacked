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


if __name__ == "__main__":
    main()
