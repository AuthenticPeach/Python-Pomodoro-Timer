# Python Pomodoro Timer

The Pomodoro Timer is a Python program that helps users manage their work sessions and breaks following the Pomodoro Technique. The program can be run from the command line and allows users to specify the number of Pomodoro cycles they want to complete.

## Features

- **Work Sessions**: The program starts with a work session of 25 minutes, allowing users to focus on their tasks without distractions.

- **Break Sessions**: After each work session, a break session of 5 minutes is provided, allowing users to rest and recharge before the next work session.

- **Customizable Duration**: The duration of work and break sessions can be easily customized by modifying the `WORK_DURATION` and `BREAK_DURATION` constants in the code.

- **Multiple Cycles**: Users can specify the number of Pomodoro cycles they want to complete. Each cycle consists of a work session followed by a break session, except for the last cycle.

- **Cancellation**: The program allows users to cancel the timer during a work or break session by pressing any key. When cancelled, the current session is stopped, and users are prompted to continue or exit.

- **Looping**: After completing a set of Pomodoro cycles, users have the option to run the timer again, allowing for multiple rounds of work and breaks.

## Getting Started

1. Clone the repository or download the Python file (`pomodoro_timer.py`) to your local machine.

2. Make sure you have Python installed on your system (version 3 or above).

3. Open a command line or terminal and navigate to the directory where the `pomodoro_timer.py` file is located.

4. Run the program by executing the following command:
```python pomodoro_timer.py```

5. Follow the prompts to enter the number of Pomodoro cycles you want to complete.

6. During the timer, press any key to cancel it. You'll be prompted to continue or exit.

7. If you choose to continue, you can run the timer again with a different number of cycles or exit the program.

## Customization

You can customize the duration of work and break sessions by modifying the following constants in the code:

```python
WORK_DURATION = 25 * 60  # 25 minutes in seconds
BREAK_DURATION = 5 * 60  # 5 minutes in seconds
```
Simply change the values to the desired duration in seconds. For example, to set a work session of 30 minutes, you can change WORK_DURATION to 30 * 60.

## Dependencies
The program requires the Python standard library and does not have any external dependencies.

## License
This project is licensed under the MIT License.
