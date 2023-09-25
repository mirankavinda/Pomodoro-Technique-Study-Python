import time
import os

# Function to start a Pomodoro session
def start_pomodoro(work_time, break_time):
    print("Pomodoro Started!")
    total_time = work_time + break_time
    num_pomodoros = 0

    while True:
        for _ in range(work_time):
            time.sleep(60) # Sleep for 60 seconds (1 minute)
            total_time -= 1

            if total_time % 20 ==0 and total_time > 0:
                print(f"Take a 5-minute break! {total_time} minutes left.")

        num_pomodoros += 1
        if total_time <= 0:
            print("Pomodoro completed!")
        else:
            print(f"Pomodoro {num_pomodoros} completed. Starting the next one!")

def get_study_time():
    while True:
        try:
            study_hours = float(input("Enter the total study time (hours): "))
            return study_hours * 60  # Convert hours to minutes
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")  # Clear the console screen
    study_time = get_study_time()
    start_pomodoro(study_time, 5)
    print("Study session completed!")