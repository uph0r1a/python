import tkinter as tk

window = tk.Tk()
window.title("My House")
window.resizable(False, False)

canvas = tk.Canvas(window, width=600, height=450, bg="#87CEEB")
canvas.pack()

canvas.create_oval(480, 30, 570, 120, fill="#FFD700", outline="#FFA500", width=2)
for angle, (dx, dy) in enumerate(
    [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
):
    canvas.create_line(
        525 + dx * 45,
        75 + dy * 45,
        525 + dx * 60,
        75 + dy * 60,
        fill="#FFA500",
        width=2,
    )


def draw_cloud(x, y):
    for ox, oy, r in [
        (0, 0, 22),
        (25, -10, 28),
        (55, 0, 22),
        (80, 5, 18),
        (-15, 8, 18),
    ]:
        canvas.create_oval(
            x + ox - r,
            y + oy - r,
            x + ox + r,
            y + oy + r,
            fill="white",
            outline="white",
        )


draw_cloud(60, 50)
draw_cloud(200, 80)

canvas.create_rectangle(0, 350, 600, 450, fill="#5a8f3c", outline="")

canvas.create_rectangle(120, 210, 480, 355, fill="#F5DEB3", outline="#8B6914", width=2)

canvas.create_polygon(
    90, 215, 300, 80, 510, 215, fill="#8B2020", outline="#5C1010", width=2
)

canvas.create_rectangle(370, 95, 415, 175, fill="#A0522D", outline="#6B3510", width=2)
for i, (cx, cy) in enumerate([(393, 85), (385, 65), (395, 45)]):
    r = 8 + i * 3
    canvas.create_oval(
        cx - r,
        cy - r,
        cx + r,
        cy + r,
        fill="#cccccc",
        outline="#aaaaaa",
        stipple="gray50",
    )

canvas.create_rectangle(245, 268, 355, 355, fill="#8B4513", outline="#5C2E00", width=2)
canvas.create_arc(
    245, 248, 355, 290, start=0, extent=180, fill="#8B4513", outline="#5C2E00", width=2
)
canvas.create_oval(248, 307, 260, 319, fill="#FFD700", outline="#B8860B")  # doorknob

canvas.create_rectangle(145, 240, 225, 310, fill="#ADE8F4", outline="#5C3D1E", width=2)
canvas.create_line(185, 240, 185, 310, fill="#5C3D1E", width=2)
canvas.create_line(145, 275, 225, 275, fill="#5C3D1E", width=2)
canvas.create_line(150, 245, 165, 260, fill="white", width=2)

canvas.create_rectangle(375, 240, 455, 310, fill="#ADE8F4", outline="#5C3D1E", width=2)
canvas.create_line(415, 240, 415, 310, fill="#5C3D1E", width=2)
canvas.create_line(375, 275, 455, 275, fill="#5C3D1E", width=2)
canvas.create_line(380, 245, 395, 260, fill="white", width=2)

canvas.create_polygon(
    270, 355, 330, 355, 360, 450, 240, 450, fill="#c8b89a", outline=""
)

for fx in [80, 100, 62]:
    canvas.create_line(fx, 355, fx, 335, fill="#4a7c27", width=2)
    canvas.create_oval(fx - 8, 320, fx + 8, 336, fill="#FF69B4", outline="#FF1493")
    canvas.create_oval(fx - 3, 325, fx + 3, 331, fill="#FFD700", outline="")

for fx in [500, 520, 540]:
    canvas.create_line(fx, 355, fx, 335, fill="#4a7c27", width=2)
    canvas.create_oval(fx - 8, 320, fx + 8, 336, fill="#FF6347", outline="#CC3300")
    canvas.create_oval(fx - 3, 325, fx + 3, 331, fill="#FFD700", outline="")

canvas.create_rectangle(52, 305, 68, 355, fill="#8B6914", outline="#5C4A0A", width=1)
canvas.create_oval(10, 240, 110, 320, fill="#228B22", outline="#145214", width=2)
canvas.create_oval(25, 220, 95, 285, fill="#2E8B2E", outline="#145214", width=2)

window.mainloop()
