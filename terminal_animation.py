
import time
import random
import os

# Terminal colours
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

messages = [
    "Initializing system modules...",
    "Loading Python libraries...",
    "Connecting to database...",
    "Processing incoming requests...",
    "Compiling source code...",
    "Analyzing application architecture...",
    "Executing background processes...",
    "Optimizing system performance...",
    "Building application components...",
    "Checking security protocols...",
    "Running automated tests...",
    "Synchronizing system resources..."
]

symbols = ["[OK]", "[INFO]", "[RUN]", "[SUCCESS]", "[PROCESS]"]

print(GREEN + "==========================================")
print("       PYTHON CONTINUOUS TERMINAL")
print("==========================================" + RESET)
print("Press CTRL + C to stop the program.\n")

try:
    while True:
        message = random.choice(messages)
        symbol = random.choice(symbols)

        timestamp = time.strftime("%H:%M:%S")

        print(
            f"{CYAN}[{timestamp}]{RESET} "
            f"{YELLOW}{symbol}{RESET} "
            f"{GREEN}{message}{RESET}",
            flush=True
        )

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n\nTerminal animation stopped.")
