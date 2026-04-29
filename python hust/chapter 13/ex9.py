import tkinter as tk

window = tk.Tk()
window.title("Tree Growth Rings")
window.resizable(False, False)

WIDTH, HEIGHT = 500, 500
cx, cy = WIDTH // 2, HEIGHT // 2

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#f5e6c8")
canvas.pack()

ring_colors = [
    "#c8a96e",
    "#b8935a",
    "#a87c46",
    "#956030",
    "#7a4520",
]

num_rings = 5
max_radius = 220
radii = [max_radius - i * (max_radius // num_rings) for i in range(num_rings)]

for i, (radius, color) in enumerate(zip(radii, ring_colors)):
    canvas.create_oval(
        cx - radius,
        cy - radius,
        cx + radius,
        cy + radius,
        fill=color,
        outline="#5c3310",
        width=2,
    )

canvas.create_text(
    cx,
    22,
    text="Tree Growth Rings — 5-Year-Old Tree",
    font=("Arial", 13, "bold"),
    fill="#3b1e08",
)

label_positions = [
    (0, (radii[0] + radii[1]) // 2),
    (1, (radii[1] + radii[2]) // 2),
    (2, (radii[2] + radii[3]) // 2),
    (3, (radii[3] + radii[4]) // 2),
    (4, radii[4] // 2),
]

import math

angle = math.radians(45)

for ring_idx, label_r in label_positions:
    year = num_rings - ring_idx
    lx = cx + label_r * math.cos(angle)
    ly = cy - label_r * math.sin(angle)

    canvas.create_text(
        lx, ly, text=f"Year {year}", font=("Arial", 10, "bold"), fill="white"
    )

for ring_idx, radius in enumerate(radii):
    year = num_rings - ring_idx
    tx = cx + radius
    canvas.create_line(tx, cy - 6, tx, cy + 6, fill="#3b1e08", width=2)
    canvas.create_text(
        tx, cy + 18, text=str(year), font=("Arial", 9, "bold"), fill="#3b1e08"
    )

canvas.create_text(
    cx + max_radius // 2,
    cy + 34,
    text="← year →",
    font=("Arial", 9, "italic"),
    fill="#5c3310",
)

canvas.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="#3b1e08", outline="#3b1e08")

window.mainloop()
