import math
import os
import time

# Donut display size (make it huge!)
width = 120
height = 40

# Animation angles
A = 0  # Rotation angle 1
B = 0  # Rotation angle 2

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

            # Make the donut much bigger
            K1 = 30
            viewer_distance = 5
            ooz = 1 / (z_final + viewer_distance)
            xp = int(width / 2 + K1 * ooz * x_rot)
            yp = int(height / 2 + K1 * ooz * y_rot)

            if 0 <= xp < width and 0 <= yp < height:
                screen[yp][xp] = '@'

    for row in screen:
        print(''.join(row))

    # Spin much faster
    A += 0.12
    B += 0.06

    time.sleep(0.02)