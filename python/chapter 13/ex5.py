import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        actual_value = float(actual_entry.get())

        if actual_value < 0:
            messagebox.showerror("Error", "Property value cannot be negative.")
            return

        assessment_value = actual_value * 0.60
        property_tax = (assessment_value / 100) * 0.75

        assessment_label.config(text=f"${assessment_value:,.2f}")
        tax_label.config(text=f"${property_tax:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


window = tk.Tk()
window.title("Property Tax Calculator")
window.geometry("340x250")
window.resizable(False, False)

tk.Label(window, text="Property Tax Calculator", font=("Arial", 13, "bold")).pack(
    pady=12
)

form_frame = tk.Frame(window)
form_frame.pack(padx=20)

tk.Label(
    form_frame,
    text="Actual property value ($):",
    font=("Arial", 11),
    anchor="w",
    width=22,
).grid(row=0, column=0, pady=6)
actual_entry = tk.Entry(form_frame, width=12, font=("Arial", 11))
actual_entry.grid(row=0, column=1)

tk.Button(
    window, text="Calculate", font=("Arial", 11), command=calculate, width=14
).pack(pady=10)

results_frame = tk.Frame(window)
results_frame.pack(padx=20)

tk.Label(
    results_frame, text="Assessment value:", font=("Arial", 11), anchor="w", width=18
).grid(row=0, column=0, pady=5)
assessment_label = tk.Label(
    results_frame, text="—", font=("Arial", 11, "bold"), fg="blue", width=12, anchor="w"
)
assessment_label.grid(row=0, column=1)

tk.Label(
    results_frame, text="Property tax:", font=("Arial", 11), anchor="w", width=18
).grid(row=1, column=0, pady=5)
tax_label = tk.Label(
    results_frame, text="—", font=("Arial", 11, "bold"), fg="blue", width=12, anchor="w"
)
tax_label.grid(row=1, column=1)

window.mainloop()
