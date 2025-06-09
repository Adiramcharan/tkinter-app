import tkinter as tk
def greet():
    name=entry.get()
    label.config(text=f"Hello, {name}!")
root=tk.Tk()
root.title("Greeter App")
root.geometry("300x150")
entry=tk.Entry(root)
entry.pack(pady=10)
button=tk.Button(root,text="Greet",command=greet)
button.pack()
label=tk.Label(root,text="")
label.pack()
root.mainloop()