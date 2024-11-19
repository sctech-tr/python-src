# protip: paint spaces to get rid of a pixel



import os
import sys

# Define the size of the canvas
CANVAS_WIDTH = 20
CANVAS_HEIGHT = 10

# Initialize canvas with empty spaces
canvas = [[" " for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]

# Clear the terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display the canvas
def display_canvas():
    clear_screen()
    print("Terminal Paint")
    print("=" * (CANVAS_WIDTH + 2))
    for row in canvas:
        print("|" + "".join(row) + "|")
    print("=" * (CANVAS_WIDTH + 2))
    print("\nControls: w = up, s = down, a = left, d = right, p = paint, c = change char, q = quit")

# Main program
def terminal_paint():
    x, y = 0, 0  # Starting position
    current_char = "█"  # Default paint character

    while True:
        display_canvas()
        print(f"Current character: {current_char}")
        print(f"Cursor position: ({x}, {y})")

        # Get user input
        key = input("Enter a command: ").strip().lower()

        if key == "w" and y > 0:  # Move up
            y -= 1
        elif key == "s" and y < CANVAS_HEIGHT - 1:  # Move down
            y += 1
        elif key == "a" and x > 0:  # Move left
            x -= 1
        elif key == "d" and x < CANVAS_WIDTH - 1:  # Move right
            x += 1
        elif key == "p":  # Paint
            canvas[y][x] = current_char
        elif key == "c":  # Change character
            current_char = input("Enter a new paint character: ")[0]
        elif key == "q":  # Quit
            print("Exiting Terminal Paint. Goodbye!")
            break

# Run the program
terminal_paint()
