import tkinter as tk
root=tk.Tk()
root.title("Button Example")
root.geometry("300x200")
def say_hello():
    label.config(text="Hello, Tkinter")
label=tk.Label(root,text="",font=("Arial", 14))
label.pack(pady=20)
button=tk.Button(root,text="Click Me",command=say_hello)
button.pack(pady=10)
root.mainloop()