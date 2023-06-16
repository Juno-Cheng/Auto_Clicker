import pyautogui
import time
import tkinter as tk

# Set the initial time interval (in seconds)
interval = 0.5

# Define variable for clicking status
clicking = False

# Function to update the interval when the button is clicked
def update_interval():
    global interval
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    milliseconds = int(milliseconds_entry.get())
    interval = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

# Function to start the clicking loop
def start_clicking():
    global clicking
    clicking = True
    click()

def click():
    if clicking:
        # Get the current coordinates of the mouse cursor
        x, y = pyautogui.position()

        # Perform the click at the current cursor position
        pyautogui.click(x, y)

        # Schedule the next click after the specified time interval
        window.after(int(interval * 1000), click)

def stop_clicking():
    global clicking
    clicking = False

# Create the GUI window
window = tk.Tk()
window.title("Auto Clicker")
window.geometry("490x200")
window.resizable(False, False)
window.iconbitmap('icon.ico')

# Create the label and entry for the time interval
label = tk.Label(window, text="Time Interval:")
label.grid(row=0, column=0, columnspan=8)

hours_label = tk.Label(window, text="Hours:")
hours_label.grid(row=1, column=0)
hours_entry = tk.Entry(window, width=5)
hours_entry.insert(0, '0')  # Default value
hours_entry.grid(row=1, column=1)

minutes_label = tk.Label(window, text="Minutes:")
minutes_label.grid(row=1, column=2)
minutes_entry = tk.Entry(window, width=5)
minutes_entry.insert(0, '0')  # Default value
minutes_entry.grid(row=1, column=3)

seconds_label = tk.Label(window, text="Seconds:")
seconds_label.grid(row=1, column=4)
seconds_entry = tk.Entry(window, width=5)
seconds_entry.insert(0, '0')  # Default value
seconds_entry.grid(row=1, column=5)

milliseconds_label = tk.Label(window, text="Milliseconds:")
milliseconds_label.grid(row=1, column=6)
milliseconds_entry = tk.Entry(window, width=5)
milliseconds_entry.insert(0, '0')  # Default value
milliseconds_entry.grid(row=1, column=7)

# Create the button to update the interval
update_button = tk.Button(window, text="Update Interval", command=update_interval)
update_button.grid(row=2, column=0, columnspan=8)

# Create the button to start the clicking loop
start_button = tk.Button(window, text="Start Clicking", command=start_clicking)
start_button.grid(row=3, column=0, columnspan=8)

# Create the button to stop the clicking loop
stop_button = tk.Button(window, text="Stop Clicking", command=stop_clicking)
stop_button.grid(row=4, column=0, columnspan=8)

exit_button = tk.Button(window, text="Exit Program", command=window.destroy)
exit_button.grid(row=5, column=0, columnspan=8)

window.mainloop()

