
import pyautogui
import time
import random
import threading

pyautogui.FAILSAFE = True

messages = [
    "System running...",
    "Processing background tasks...",
    "Monitoring application...",
    "Executing Python operations...",
    "Checking system status...",
    "Running continuous processes...",
    "Application is active...",
    "System resources operational..."
]

def move_mouse():
    screen_width, screen_height = pyautogui.size()

    while True:
        x = random.randint(100, screen_width - 100)
        y = random.randint(100, screen_height - 100)

        pyautogui.moveTo(x, y, duration=2)
        time.sleep(0.5)

# Run mouse movement in background
mouse_thread = threading.Thread(
    target=move_mouse,
    daemon=True
)
mouse_thread.start()

print("================================")
print("   WINDOWS MOUSE AUTOMATION")
print("================================")
print("Mouse movement and terminal output active.")
print("Press CTRL + C to stop.\n")

try:
    while True:
        print(
            f"[{time.strftime('%H:%M:%S')}] "
            f"{random.choice(messages)}",
            flush=True
        )
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nAutomation stopped.")
