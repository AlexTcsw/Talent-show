import tkinter as tk 
root = tk.Tk()
root.geometry("500x500")
root.title("Jokers")
Label = tk.Label(root, text="This is the jokers app")
Label.pack()

Button = tk.Button(root, text="Click me", command=lambda: Label.config(text="Wow this is cool here is the joke. Why did the laptop go to the doctor?"))
Button.pack()

Button2 = tk.Button(root, text="Click for joke answer", command = lambda: Label.config(text="Because it had a virus"))
Button2.pack()

Button3 = tk.Button(root, text="catsarecoolmath", command = lambda: Label.config(text="This is changed to catsarecoolmath"))
Button3.pack()

root.mainloop()