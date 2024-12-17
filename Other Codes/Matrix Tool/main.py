import tkinter as tk


def add_vals(win : tk.Tk, a, b):
    tk.Label(win, text=f" = {a + b}").grid(row=0, column=3)


window = tk.Tk()
window.title("Test")
window.geometry("500x250")

a = tk.Entry(master=window, width=5)
a.grid(row=0)
tk.Label(master=window, text=" + ").grid(row=0, column=1)
b = tk.Entry(master=window, width=5)
b.grid(row=0, column=2)

calc_b = tk.Button(master=window,
                   text="Calculate",
                   width=15,
                   command=lambda: add_vals(window, int(a.get()), int(b.get())))
calc_b.grid(row=1, columnspan=3)

window.mainloop()