import pyautogui
import time

# Set the time interval between clicks (in seconds)
interval = 0.5


while True:
    # Get the current coordinates of the mouse cursor
    x, y = pyautogui.position()

    # Perform the click at the current cursor position
    pyautogui.click(x, y)

    # Wait for the specified time interval before the next click
    time.sleep(interval)

