import tkinter as tk


def translate(word):
    translations = {"sinister": "left", "dexter": "right", "medium": "center"}
    result_label.config(text=f"{word} = {translations[word]}")


window = tk.Tk()
window.title("Latin Translator")
window.geometry("500x300")
window.resizable(False, False)

title_label = tk.Label(
    window, text="Click a Latin word to translate it:", font=("Arial", 11)
)
title_label.pack(pady=12)

button_frame = tk.Frame(window)
button_frame.pack()

for word in ["sinister", "dexter", "medium"]:
    tk.Button(
        button_frame,
        text=word.capitalize(),
        width=10,
        command=lambda w=word: translate(w),
    ).pack(side="left", padx=8)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

window.mainloop()
