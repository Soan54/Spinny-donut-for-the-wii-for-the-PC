import math
import os
import time

# Donut display size
width = 40
height = 20

# Animation angles
A = 0  # Rotation angle 1
B = 0  # Rotation angle 2

while True:
    # Clear the terminal (works on Windows and Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create a 2D array (list of lists) for the screen
    screen = [[' ' for _ in range(width)] for _ in range(height)]

    # Loop over theta and phi to create the donut shape
    for theta in range(0, 628, 7):  # 0 to 2pi, step ~0.11
        for phi in range(0, 628, 2):  # 0 to 2pi, step ~0.03
            # Convert to radians
            t = theta / 100.0
            p = phi / 100.0

            # Donut math (parametric equations)
            # R1 = 1 (radius of circle), R2 = 2 (distance from center)
            x = math.cos(t) * (2 + math.cos(p))
            y = math.sin(t) * (2 + math.cos(p))
            z = math.sin(p)

            # Rotate in 3D
            x_rot = x * math.cos(A) - z * math.sin(A)
            z_rot = x * math.sin(A) + z * math.cos(A)
            y_rot = y * math.cos(B) - z_rot * math.sin(B)
            z_final = y * math.sin(B) + z_rot * math.cos(B)

            # Project 3D point to 2D screen
            # Perspective: closer points appear larger
            K1 = 10  # Controls size
            viewer_distance = 5
            ooz = 1 / (z_final + viewer_distance)
            xp = int(width / 2 + K1 * ooz * x_rot)
            yp = int(height / 2 + K1 * ooz * y_rot)

            # Draw the donut point if it's on screen
            if 0 <= xp < width and 0 <= yp < height:
                screen[yp][xp] = '@'

    # Print the screen
    for row in screen:
        print(''.join(row))

    # Update rotation angles for animation
    A += 0.04
    B += 0.02

    # Slow down the animation
    time.sleep(0.03)