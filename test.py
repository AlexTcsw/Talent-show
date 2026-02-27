import tkinter as tk
from tkinter import simpledialog # This makes the popup box work

def math_secret():
    # This pops up a box with a math problem
    answer = simpledialog.askstring("Math Challenge", "What is 5x5?")
    
    if answer == "25":
        Label.config(text="ACCESS GRANTED: Good job", fg="green")
    else:
        Label.config(text="ACCESS DENIED: Keep practicing!", fg="red")

root = tk.Tk()
root.geometry("600x600") # Made it a bit bigger for the ViewBoard
root.title("The Talent Show App")

# Main Label - I added a bigger font so Nova can see it from the crowd
Label = tk.Label(root, text="This is the Jokers App", font=("Arial", 18, "bold"))
Label.pack(pady=20)

# Button 1: The Joke
Button1 = tk.Button(root, text="Click for a Joke", font=("Arial", 12),
                   command=lambda: Label.config(text="Why did the laptop go to the doctor?", fg="black"))
Button1.pack(pady=10)

# Button 2: The Answer
Button2 = tk.Button(root, text="Joke Answer", font=("Arial", 12),
                   command=lambda: Label.config(text="Because it had a virus!", fg="blue"))
Button2.pack(pady=10)

# Button 3: The Secret Math Challenge for Nova
Button3 = tk.Button(root, text="MATH ONLY", font=("Arial", 12), bg="lightgray",
                   command=math_secret)
Button3.pack(pady=10)

# Button 4: Your cool random button
Button4 = tk.Button(root, text="catsarecoolmath", font=("Arial", 12),
                   command=lambda: Label.config(text="This is changed to catsarecoolmath", fg="purple"))
Button4.pack(pady=10)

root.mainloop()
