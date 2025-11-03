import tkinter as tk
from tkinter import messagebox
from quiz_game import start_quiz_game

# Global variables
root = None
welcome_label = None
instruction_label = None
name_label = None
name_entry = None
Start_button = None

def start_quiz():
    player_name = name_entry.get()
    if player_name.strip() == "":
        messagebox.showerror("Error", "Please enter your name!")
    else:
        print(f"Player Name: {player_name}")
        messagebox.showinfo("Quiz Started", f"Good luck {player_name}!")
        # Clear welcome screen
        welcome_label.destroy()
        instruction_label.destroy()
        name_label.destroy()
        name_entry.destroy()
        Start_button.destroy()
        # Start quiz
        start_quiz_game(root, player_name)

def main():
    global root, welcome_label, instruction_label, name_label, name_entry, Start_button
    
    root = tk.Tk()
    root.title("Programming Quiz")
    root.geometry("600x500")
    root.configure(bg="#2c3e50")

    welcome_label = tk.Label(root, text="🎮 PROGRAMMING QUIZ 🎮",
                            font=("Arial", 20, "bold"),
                            bg="#2c3e50", fg="#27ae60")
    welcome_label.pack(pady=40)

    instruction_label = tk.Label(root, text="Answer 30 programming questions!",   
                                font=("Arial", 14),
                                bg="#2c3e50", fg="white")
    instruction_label.pack(pady=15)

    name_label = tk.Label(root, text="Enter your name",
                         font=("Arial", 14),
                         bg="#2c3e50", fg="white")
    name_label.pack(pady=(30, 8))

    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=8)

    Start_button = tk.Button(root, text="START QUIZ", 
                            command=start_quiz,
                            font=("Arial", 14, "bold"),
                            bg="#27ae60", fg="white", width=20)
    Start_button.pack(pady=40)

    root.mainloop()

if __name__ == "__main__":
    main()