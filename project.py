import time
from datetime import datetime

import csv

def fetch_light_data(csv_filename):
    """
    the data-fetching logic
    from the light-sensing app, such as a request to an API or
    reading a file/database.
    """
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

    # If no number above 1000 was found
    return False

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

def monitor_light(start_hour, end_hour, file):
    """Continuously checks for light detection within the specified wake-up hours."""
    while True:
        light_detected = fetch_light_data(file)
        if light_detected and check_time_range(start_hour, end_hour):
            trigger_alarm()
            break
        time.sleep(10)

def main():
    start_hour = 6 #assumed waking hours for the prototype
    end_hour = 20
    file = 'Raw Data.csv' 
    monitor_light(start_hour, end_hour, file)


if __name__ == "__main__":
    main()


