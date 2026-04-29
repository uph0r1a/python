import tkinter as tk
from tkinter import messagebox

rates = [
    ("Daytime (6:00 a.m. - 5:59 p.m.)", 0.07),
    ("Evening (6:00 p.m. - 11:59 p.m.)", 0.12),
    ("Off-Peak (Midnight - 5:59 a.m.)", 0.05),
]


def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            messagebox.showerror("Error", "Minutes cannot be negative.")
            return

        selected = rate_var.get()
        rate_name, rate_per_min = rates[selected]
        charge = minutes * rate_per_min

        messagebox.showinfo(
            "Call Charge",
            f"Rate Category:  {rate_name}\n"
            f"Minutes:        {minutes:.1f}\n"
            f"Rate:           ${rate_per_min:.2f} per minute\n"
            f"─────────────────────────\n"
            f"Total Charge:   ${charge:.2f}",
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")


window = tk.Tk()
window.title("Long-Distance Call Calculator")
window.geometry("360x280")
window.resizable(False, False)

tk.Label(window, text="Long-Distance Call Calculator", font=("Arial", 13, "bold")).pack(
    pady=12
)

tk.Label(window, text="Select a rate category:", font=("Arial", 11)).pack(
    anchor="w", padx=30
)

rate_var = tk.IntVar(value=0)

radio_frame = tk.Frame(window)
radio_frame.pack(padx=30, pady=6, anchor="w")

for i, (name, rate) in enumerate(rates):
    tk.Radiobutton(
        radio_frame,
        text=f"{name}  (${rate:.2f}/min)",
        variable=rate_var,
        value=i,
        font=("Arial", 10),
        anchor="w",
    ).pack(anchor="w", pady=3)

minutes_frame = tk.Frame(window)
minutes_frame.pack(padx=30, pady=10, anchor="w")

tk.Label(minutes_frame, text="Number of minutes:", font=("Arial", 11)).grid(
    row=0, column=0, padx=(0, 10)
)
minutes_entry = tk.Entry(minutes_frame, width=10, font=("Arial", 11))
minutes_entry.grid(row=0, column=1)

tk.Button(
    window,
    text="Calculate Charge",
    font=("Arial", 11),
    command=calculate_charge,
    width=16,
).pack(pady=12)

window.mainloop()
