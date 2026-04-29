import tkinter as tk


def show_info():
    label.config(text="Steven Marcus\n274 Baily Drive\nWaynesville, NC 27999")


def quit_app():
    window.destroy()


window = tk.Tk()
window.title("My Info")
window.geometry("300x200")
window.resizable(False, False)

label = tk.Label(window, text="", font=("Arial", 12), justify="center")
label.pack(expand=True)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

show_button = tk.Button(button_frame, text="Show Info", command=show_info, width=10)
show_button.pack(side="left", padx=10)

quit_button = tk.Button(button_frame, text="Quit", command=quit_app, width=10)
quit_button.pack(side="left", padx=10)

window.mainloop()
