import tkinter as tk

WIDTH = 1100
HEIGHT = 420

BODIES = [
    ("Sun", 55, 200, 48, "#FDB813", 65),
    ("Mercury", 145, 200, 6, "#b5b5b5", 20),
    ("Venus", 200, 200, 11, "#e8cda0", 25),
    ("Earth", 265, 200, 12, "#4fa3e0", 26),
    ("Mars", 330, 200, 8, "#c1440e", 22),
    ("Jupiter", 450, 200, 36, "#c88b3a", 50),
    ("Saturn", 590, 200, 28, "#e4d191", 42),
    ("Uranus", 720, 200, 18, "#7de8e8", 32),
    ("Neptune", 820, 200, 17, "#4b70dd", 31),
    ("Pluto", 900, 200, 5, "#c2a98a", 19),
]

SATURN_IDX = 6

root = tk.Tk()
root.title("Solar System")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#05050f", highlightthickness=0)
canvas.pack()

import random

random.seed(7)
for _ in range(220):
    sx = random.randint(0, WIDTH)
    sy = random.randint(0, HEIGHT)
    sr = random.choice([0.5, 1, 1])
    canvas.create_oval(sx - sr, sy - sr, sx + sr, sy + sr, fill="white", outline="")

for name, x, y, r, color, dy in BODIES[1:]:
    canvas.create_oval(
        55 - (x - 55), y - 4, x + (x - 55), y + 4, outline="#1a1a3a", width=1
    )

for i, (name, x, y, r, color, dy) in enumerate(BODIES):
    if i == SATURN_IDX:
        canvas.create_oval(
            x - r * 2.1,
            y - r * 0.45,
            x + r * 2.1,
            y + r * 0.45,
            outline="#c8b560",
            width=3,
            fill="",
        )
        canvas.create_oval(
            x - r * 1.7,
            y - r * 0.32,
            x + r * 1.7,
            y + r * 0.32,
            outline="#d4c070",
            width=2,
            fill="",
        )

    if name == "Sun":
        for glow in [r + 20, r + 12, r + 5]:
            canvas.create_oval(
                x - glow,
                y - glow,
                x + glow,
                y + glow,
                fill="",
                outline="#FDB813",
                width=1,
                stipple="gray25" if glow > r + 10 else "gray50",
            )
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")

    if name == "Earth":
        canvas.create_arc(
            x - r + 2,
            y - r + 3,
            x + r - 3,
            y + r - 5,
            start=30,
            extent=100,
            fill="#2d8a4e",
            outline="",
        )

    if name == "Jupiter":
        for band_y, bh, bc in [
            (y - 10, 4, "#a07030"),
            (y + 5, 3, "#a07030"),
            (y - 3, 3, "#d49050"),
        ]:
            canvas.create_arc(
                x - r + 1,
                band_y,
                x + r - 1,
                band_y + bh,
                start=0,
                extent=180,
                fill=bc,
                outline="",
            )

    lx, ly = x, y + r + dy - r
    canvas.create_text(
        lx,
        ly + r + 8,
        text=name,
        font=("Helvetica", 9, "bold"),
        fill="white",
        anchor="n",
    )

canvas.create_text(
    WIDTH // 2,
    18,
    text="Our Solar System",
    font=("Helvetica", 15, "bold"),
    fill="#aad4ff",
)

root.mainloop()
