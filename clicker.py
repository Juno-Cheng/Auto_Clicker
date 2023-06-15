import pyautogui
import time
import tkinter as tk

# Set the initial time interval (in seconds)
interval = 0.5

# Function to update the interval when the button is clicked
def update_interval():
    global interval
    interval = float(entry.get())

# Function to start the clicking loop
def start_clicking():
    try:
        while True:
            # Get the current coordinates of the mouse cursor
            x, y = pyautogui.position()

            # Perform the click at the current cursor position
            pyautogui.click(x, y)

            # Wait for the specified time interval before the next click
            time.sleep(interval)

    except KeyboardInterrupt:
        # Handle the keyboard interrupt
        print("Program stopped by user")

# Create the GUI window
window = tk.Tk()
window.title("Auto Clicker")
window.geometry("300x150")
window.resizable(False, False)

# Create the label and entry for the time interval
label = tk.Label(window, text="Time Interval (in seconds):")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the button to update the interval
update_button = tk.Button(window, text="Update Interval", command=update_interval)
update_button.pack()

# Create the button to start the clicking loop
start_button = tk.Button(window, text="Start Clicking", command=start_clicking)
start_button.pack()

# Create the button to stop the clicking loop
start_button = tk.Button(window, text="Stop Clicking", command=start_clicking)
start_button.pack()

exit_button = tk.Button(window, text="Exit Program", command=window.destroy)
exit_button.pack()

# Start the GUI main loop
window.mainloop()
