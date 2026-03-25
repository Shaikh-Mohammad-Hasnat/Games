import cv2 
import numpy as np
import keyboard
import random

# Load bird
Flappy_bird_img = cv2.imread("flappy.png")
Flappy_bird_img = cv2.resize(Flappy_bird_img, (60, 60))

# Initial values
x, y = 190, 150
canvas_h, canvas_w = 700, 1020

gap_y = random.randint(150, 450)
gap_size = 200
pillar_x = canvas_w

Points = 0
game_over = False
scored = False

while True:
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)
  
    bird_h, bird_w = Flappy_bird_img.shape[0], Flappy_bird_img.shape[1]

    # Movement (only if game not over)
    if not game_over:
        if keyboard.is_pressed("space"):
            y -= 10
        else:
            y += 3

    # Clamp bird inside screen
    y = max(0, min(y, canvas_h - bird_h))

    # Move pillar
    if not game_over:
        pillar_x -= 5

    # Reset pillar
    if pillar_x < -80:
        pillar_x = canvas_w
        gap_y = random.randint(150, 450)
        scored = False

    # Default pillar color
    color = (0, 255, 0)

    # Collision detection
    if not game_over:
        if (x + bird_w > pillar_x and x < pillar_x + 80):
            if y < gap_y or y + bird_h > gap_y + gap_size:
                print("OUT")
                color = (0, 0, 255)
                game_over = True

    # Score when passing pillar
    if not scored and pillar_x + 80 < x:
        Points += 1
        scored = True

    # Draw pillars
    cv2.rectangle(canvas, (pillar_x, 0), (pillar_x+80, gap_y), color, -1)
    cv2.rectangle(canvas, (pillar_x, gap_y+gap_size), (pillar_x+80, canvas_h), color, -1)

    # Draw bird
    canvas[y:y+bird_h, x:x+bird_w] = Flappy_bird_img

    # Show score
    cv2.putText(canvas, f"Score: {Points}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    # Game over text
    if game_over:
        cv2.putText(canvas, "GAME OVER", (350, 350),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 4)

    cv2.imshow("Flappy Bird", canvas)

    if keyboard.is_pressed("r"):   
        game_over = False
        y = 150
        pillar_x = canvas_w
        gap_y = random.randint(150, 450)
        scored = False
        Points = 0


    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()