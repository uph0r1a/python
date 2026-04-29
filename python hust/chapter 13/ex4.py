import tkinter as tk
from tkinter import messagebox


def convert():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (9 / 5) * celsius + 32
        result_label.config(text=f"{celsius:.2f} °C  =  {fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")
window.geometry("320x200")
window.resizable(False, False)

tk.Label(window, text="Temperature Converter", font=("Arial", 13, "bold")).pack(pady=12)

form_frame = tk.Frame(window)
form_frame.pack(padx=20)

tk.Label(
    form_frame, text="Celsius temperature:", font=("Arial", 11), anchor="w", width=20
).grid(row=0, column=0, pady=6)
celsius_entry = tk.Entry(form_frame, width=10, font=("Arial", 11))
celsius_entry.grid(row=0, column=1)

tk.Button(
    window, text="Convert to Fahrenheit", font=("Arial", 11), command=convert, width=20
).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack()

window.mainloop()
