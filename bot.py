import time
import sys

def print_slowly(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_colored_text(text, color, delay):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }

    if color not in colors:
        print("Invalid color")
        return

    color_code = colors[color]

    for char in text:
        sys.stdout.write(color_code + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay)

    print()  # Move to the next line after printing the colored text

text_to_display = "Contact me through Telegram and buy the full version of the bot : @Trending_Bot_Developer"
colors_to_use = ['red', 'green', 'yellow', 'blue', 'white']
delay_between_chars = 0.06
repetitions = 10

for _ in range(repetitions):
    for color in colors_to_use:
        print_colored_text(text_to_display, color, delay_between_chars)

    time.sleep(1)  # Delay between each repetition