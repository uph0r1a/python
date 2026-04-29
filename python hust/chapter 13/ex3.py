import tkinter as tk
from tkinter import messagebox


def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())

        if gallons <= 0:
            messagebox.showerror("Error", "Gallons must be greater than zero.")
            return

        mpg = miles / gallons
        result_label.config(text=f"Miles Per Gallon:  {mpg:.2f} MPG")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


window = tk.Tk()
window.title("Gas Mileage Calculator")
window.geometry("320x230")
window.resizable(False, False)

tk.Label(window, text="Gas Mileage Calculator", font=("Arial", 13, "bold")).pack(
    pady=12
)

form_frame = tk.Frame(window)
form_frame.pack(padx=20)

tk.Label(
    form_frame, text="Gallons of gas:", font=("Arial", 11), anchor="w", width=18
).grid(row=0, column=0, pady=6)
gallons_entry = tk.Entry(form_frame, width=10, font=("Arial", 11))
gallons_entry.grid(row=0, column=1)

tk.Label(
    form_frame, text="Miles on a full tank:", font=("Arial", 11), anchor="w", width=18
).grid(row=1, column=0, pady=6)
miles_entry = tk.Entry(form_frame, width=10, font=("Arial", 11))
miles_entry.grid(row=1, column=1)

tk.Button(
    window, text="Calculate MPG", font=("Arial", 11), command=calculate_mpg, width=16
).pack(pady=12)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack()

window.mainloop()
