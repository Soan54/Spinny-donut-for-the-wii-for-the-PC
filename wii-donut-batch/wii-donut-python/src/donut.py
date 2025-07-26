import math
import os
import time

width = 270      # Make the screen much wider
height = 76      # Make the screen taller

A = 0
B = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    screen = [[' ' for _ in range(width)] for _ in range(height)]

    for theta in range(0, 628, 7):
        for phi in range(0, 628, 2):
            t = theta / 100.0
            p = phi / 100.0

            x = math.cos(t) * (2 + math.cos(p))
            y = math.sin(t) * (2 + math.cos(p))
            z = math.sin(p)

            x_rot = x * math.cos(A) - z * math.sin(A)
            z_rot = x * math.sin(A) + z * math.cos(A)
            y_rot = y * math.cos(B) - z_rot * math.sin(B)
            z_final = y * math.sin(B) + z_rot * math.cos(B)

            K1 = 30    # Make the donut itself much larger
            viewer_distance = 5
            ooz = 1 / (z_final + viewer_distance)
            xp = int(width / 2 + K1 * ooz * x_rot)
            yp = int(height / 2 + K1 * ooz * y_rot * 0.5)

            if 0 <= xp < width and 0 <= yp < height:
                screen[yp][xp] = '@'

    for row in screen:
        print(''.join(row))

    # Update rotation angles for animation
    A += 0.04
    B += 0.02

    time.sleep(0.03)

    # Print copyright/message at the bottom
    print("\n" * 2 + "Made by Soan copyright 2025".center(width))