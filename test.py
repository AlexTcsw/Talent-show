import tkinter as tk
from tkinter import simpledialog

# --- FUNCTIONS ---

def math_secret():
    # This pops up a box for Nova or anyone else to solve
    answer = simpledialog.askstring("Math Challenge", "What is 5x5?")
    
    if answer == "25":
        Label.config(text="ACCESS GRANTED: Good job!", fg="green")
    else:
        Label.config(text="ACCESS DENIED: Keep practicing!", fg="red")

# --- MAIN WINDOW SETUP ---

root = tk.Tk()
root.geometry("600x600")
root.title("Code Club: Talent Show Edition")

# --- THE DISPLAY LABEL ---
# This is the big text area at the top
Label = tk.Label(root, text="This is the Jokers App", 
                 font=("Arial", 20, "bold"), 
                 wraplength=500, 
                 justify="center")
Label.pack(pady=40)

# --- THE BUTTONS ---

# Button 1: The Setup
Button1 = tk.Button(root, text="Click for a Joke", font=("Arial", 12), width=20,
                   command=lambda: Label.config(text="Why did the laptop go to the doctor?", fg="black"))
Button1.pack(pady=10)

# Button 2: The Punchline
Button2 = tk.Button(root, text="Joke Answer", font=("Arial", 12), width=20,
                   command=lambda: Label.config(text="Because it had a virus!", fg="blue"))
Button2.pack(pady=10)

# Button 3: The Math Challenge
Button3 = tk.Button(root, text="MATH ONLY", font=("Arial", 12), width=20, bg="lightgray",
                   command=math_secret)
Button3.pack(pady=10)

# Button 4: The Squad Intro
Button4 = tk.Button(root, text="About Us", font=("Arial", 12), width=20,
                   command=lambda: Label.config(text="Hi! I am Alex, Daymein, and Wyatt.\nWe are the Code Club!", fg="purple"))
Button4.pack(pady=10)

# Button 5: Reset (Extra "Pro" Move)
Button5 = tk.Button(root, text="Reset App", font=("Arial", 10), width=10,
                   command=lambda: Label.config(text="This is the Jokers App", fg="black"))
Button5.pack(pady=30)

# --- RUN THE APP ---
root.mainloop()
