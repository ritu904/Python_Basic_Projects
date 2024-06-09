import datetime
import time
import winsound  # For playing sound (Windows specific)
from playsound import playsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play sound (Windows specific)
            #winsound.Beep(1000, 2000)  # Frequency in Hz, duration in milliseconds
            playsound("C:\Users\Ritu Rani\Desktop\PROJECTS\sound.mp3")
            break
        time.sleep(1)  # Check every second

def main():
    print("Welcome to Simple Alarm Clock")
    print("Enter the time for the alarm (24-hour format HH:MM:SS)")
    alarm_hour = input("Hour: ")
    alarm_minute = input("Minute: ")
    alarm_second = input("Second: ")
    alarm_time = f"{alarm_hour.zfill(2)}:{alarm_minute.zfill(2)}:{alarm_second.zfill(2)}"

    try:
        # Validate alarm time
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        return

    print(f"Alarm set for: {alarm_time}")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
