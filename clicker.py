import pyautogui
import time

# Set the screen coordinates where you want to click
x, y = 100, 100

# Set the time interval between clicks (in seconds)
interval = 0.5

while True:
    # Move the cursor to the specified screen position
    pyautogui.moveTo(x, y)

    # Perform the click
    pyautogui.click()

    # Wait for the specified time interval before the next click
    time.sleep(interval)