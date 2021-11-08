import tkinter as tk

from tkinter import ttk


def greet():
    print(f"Hello {user_name.get() or 'world'}!")


# main window of application
root = tk.Tk()
root.geometry("300x300")

user_name = tk.StringVar()

input_frame = ttk.Frame(root,padding=(20,10,30,0))
input_frame.pack(fill="both")


name_label = ttk.Label(input_frame, text="Name:  ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

buttons = ttk.Frame(root,padding=(20,10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="right")

# displays the main window, code after which will not run until window is closed
root.mainloop()

print("hello world")
