import math
import os
import time

# Set the dimensions of the donut
width = 40
height = 20

# Initialize variables for the donut
A = 0
B = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    output = ""

    # Generate the donut
    for j in range(height):
        line = ""
        for i in range(width):
            x = A
            y = B
            x += int(math.sin(A) * math.cos(B) * 10)
            y += int(math.sin(B) * 10)
            line += " "
            if i == x and j == y:
                line += "o"
            line += " "
        output += line + "\n"

    print(output)
    A += 0.1
    B += 0.1
    time.sleep(0.1)