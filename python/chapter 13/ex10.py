import tkinter as tk
import math


def draw_star(canvas, cx, cy, outer_r, inner_r, color, outline):
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        r = outer_r if i % 2 == 0 else inner_r
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.extend([x, y])
    canvas.create_polygon(points, fill=color, outline=outline, width=3)


def draw_terrazzo(canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill="#1a1a1a", outline="")
    import random

    random.seed(42)
    for _ in range(200):
        x = random.randint(0, width)
        y = random.randint(0, height)
        w = random.randint(3, 10)
        h = random.randint(2, 6)
        shade = random.choice(["#2a2a2a", "#252525", "#2e2e2e", "#333333"])
        canvas.create_rectangle(x, y, x + w, y + h, fill=shade, outline="")


NAME = "Euphoria"

WIDTH, HEIGHT = 680, 680
CX, CY = 340, 330
OUTER_R = 230
INNER_R = 95

root = tk.Tk()
root.title("Hollywood Walk of Fame")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1a1a", highlightthickness=0)
canvas.pack()

draw_terrazzo(canvas, WIDTH, HEIGHT)

canvas.create_rectangle(60, 60, 620, 620, fill="#1c1c1c", outline="#2a2a2a", width=1)
canvas.create_rectangle(72, 72, 608, 608, fill="", outline="#8B7355", width=2)

draw_star(canvas, CX, CY, OUTER_R, INNER_R, "#C8567A", "#8a3050")
draw_star(canvas, CX, CY, OUTER_R - 5, INNER_R + 3, "", "#e8789A")

canvas.create_text(
    CX,
    CY - 55,
    text="✦  WALK OF FAME  ✦",
    font=("Georgia", 12),
    fill="#d4a060",
    anchor="center",
)

canvas.create_line(CX - 70, CY - 35, CX - 35, CY - 35, fill="#d4a060", width=1)
canvas.create_line(CX + 35, CY - 35, CX + 70, CY - 35, fill="#d4a060", width=1)

spaced_name = "  ".join(NAME.upper())
canvas.create_text(
    CX,
    CY + 5,
    text=spaced_name,
    font=("Georgia", 26, "bold"),
    fill="#f0d090",
    anchor="center",
)

canvas.create_text(
    CX,
    CY + 40,
    text="★   AI   ★",
    font=("Georgia", 13),
    fill="#d4a060",
    anchor="center",
)

canvas.create_text(
    CX,
    HEIGHT - 80,
    text="HOLLYWOOD, CALIFORNIA",
    font=("Georgia", 11),
    fill="#8B7355",
    anchor="center",
)

for dx in [-20, 0, 20]:
    canvas.create_oval(
        CX + dx - 3,
        HEIGHT - 60 - 3,
        CX + dx + 3,
        HEIGHT - 60 + 3,
        fill="#8B7355",
        outline="",
    )

root.mainloop()
