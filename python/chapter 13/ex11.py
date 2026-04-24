import tkinter as tk

WIDTH, HEIGHT = 600, 300
root = tk.Tk()
root.title("Simple Car")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white", highlightthickness=0)
canvas.pack()

canvas.create_rectangle(80, 160, 520, 240, outline="black", width=2)

canvas.create_polygon(
    150, 160, 190, 100, 380, 100, 430, 160, outline="black", width=2, fill=""
)

canvas.create_polygon(
    200, 155, 220, 108, 310, 108, 310, 155, outline="black", width=1, fill=""
)

canvas.create_polygon(
    320, 155, 320, 108, 375, 108, 415, 155, outline="black", width=1, fill=""
)

canvas.create_oval(130, 210, 210, 270, outline="black", width=2, fill="white")
canvas.create_oval(152, 222, 188, 258, outline="black", width=1, fill="")
canvas.create_oval(380, 210, 460, 270, outline="black", width=2, fill="white")
canvas.create_oval(402, 222, 438, 258, outline="black", width=1, fill="")
canvas.create_rectangle(505, 175, 522, 195, outline="black", width=1)
canvas.create_rectangle(78, 175, 95, 195, outline="black", width=1)
canvas.create_line(300, 160, 300, 238, fill="black", width=1)
canvas.create_rectangle(315, 195, 340, 202, outline="black", width=1)
canvas.create_rectangle(250, 195, 275, 202, outline="black", width=1)

root.mainloop()
