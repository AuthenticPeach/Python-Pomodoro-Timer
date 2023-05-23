import time

# Constants for work and break durations
WORK_DURATION = 25 * 60  # 25 minutes in seconds
BREAK_DURATION = 5 * 60  # 5 minutes in seconds

def pomodoro_timer():
    while True:
        cycles = int(input("Enter the number of Pomodoro cycles: "))

        for i in range(cycles):
            print(f"Pomodoro {i+1} - Work, Press ESC to Cancel")
            if work_timer(WORK_DURATION):
                break

            if i < cycles - 1:
                print("Take a break!")
                if work_timer(BREAK_DURATION):
                    break

        print("Pomodoro timer completed!")
        
        choice = input("Do you want to run the Pomodoro timer again? (y/n): ")
        if choice.lower() != "y":
            break

def work_timer(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time // 60:02d}:{remaining_time % 60:02d}", end="\r")
        time.sleep(1)
        
        if time.time() > end_time:
            print("Time's up!")
            return False
        
        if time.time() < end_time and kbhit():
            print("Timer cancelled!")
            return True

def kbhit():
    try:
        import msvcrt  # For Windows OS
        return msvcrt.kbhit()
    except ImportError:
        import select
        import sys
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

# Run the Pomodoro timer
pomodoro_timer()
