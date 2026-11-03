
import os
import time

# Enable ANSI terminal support on Windows
os.system("")

GREEN = "\033[92m"
RESET = "\033[0m"
CLEAR = "\033[2J"
HOME = "\033[H"

width = 60
position = 0
direction = 1

print(CLEAR, end="")

try:
    while True:
        # Move cursor to the beginning
        print(HOME, end="")

        # Draw moving cursor
        line = " " * position + GREEN + "●" + RESET

        print(line)
        print("\n" + "=" * width)
        print("   CONTINUOUS CURSOR ANIMATION")
        print("=" * width)
        print("\nPress CTRL + C to stop.")

        position += direction

        # Reverse direction at screen boundaries
        if position >= width:
            direction = -1
        elif position <= 0:
            direction = 1

        time.sleep(0.03)

except KeyboardInterrupt:
    print("\nAnimation stopped.")
    print(RESET)
