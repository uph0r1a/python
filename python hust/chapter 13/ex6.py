import tkinter as tk

services = [
    ("Oil Change", 30.00),
    ("Lube Job", 20.00),
    ("Radiator Flush", 40.00),
    ("Transmission Flush", 100.00),
    ("Inspection", 35.00),
    ("Muffler Replacement", 200.00),
    ("Tire Rotation", 20.00),
]


def calculate_total():
    total = sum(price for var, price in check_vars if var.get())
    total_label.config(text=f"Total Charges:  ${total:.2f}")


window = tk.Tk()
window.title("Joe's Automotive")
window.geometry("320x340")
window.resizable(False, False)

tk.Label(window, text="Joe's Automotive", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="Select the services performed:", font=("Arial", 11)).pack()

checks_frame = tk.Frame(window)
checks_frame.pack(padx=30, pady=8, anchor="w")

check_vars = []
for name, price in services:
    var = tk.BooleanVar()
    tk.Checkbutton(
        checks_frame,
        text=f"{name:<22} ${price:.2f}",
        variable=var,
        font=("Courier", 11),
        anchor="w",
    ).pack(anchor="w", pady=1)
    check_vars.append((var, price))

tk.Button(
    window,
    text="Calculate Total",
    font=("Arial", 11),
    command=calculate_total,
    width=16,
).pack(pady=10)

total_label = tk.Label(
    window, text="Total Charges:  $0.00", font=("Arial", 12, "bold"), fg="blue"
)
total_label.pack()

window.mainloop()
