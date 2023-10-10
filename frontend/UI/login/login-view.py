import tkinter as tk
import ttkbootstrap as ttk


window = ttk.Window(themename="journal", title="Login", size=(600, 400))

username_var = tk.StringVar(value="Username")
username = ttk.Entry(master=window, textvariable=username_var)
username.pack()

password_var = tk.StringVar(value="Password")
password = ttk.Entry(master=window, textvariable=password_var)
password.pack()

login = ttk.Button(master=window, text="Login", command=lambda: print("logged in"))
login.pack()

register_user = ttk.Button(
    master=window,
    text="Register new user",
    command=lambda: print("New user registered"),
)
register_user.pack()

window.mainloop()
