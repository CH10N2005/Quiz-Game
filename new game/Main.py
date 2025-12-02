import tkinter as tk
from tkinter import messagebox
from quiz_game import start_quiz_game
from leaderboard import get_leaderboard_text
import pygame

# --- GLOBAL VARIABLES ---
root = None
welcome_label = None
instruction_label = None
name_label = None
name_entry = None
sectionyear_label = None
sectionyear_entry = None
Start_button = None
leaderboard_button = None

def start_quiz():
    player_name = name_entry.get().strip()
    section_year = sectionyear_entry.get().strip()
    

    if not player_name and not section_year:
        messagebox.showerror("Error", "Please enter your name and your section & year!")
        return
    if not player_name:
        messagebox.showerror("Error", "Please enter your name!")
        return
    if not section_year:
        messagebox.showerror("Error", "Please enter your section & year!")
        return
    
    #terminal
    print(f"Player Name: {player_name}")
    print(f"Section & Year: {section_year}")
    messagebox.showinfo("Quiz Started", f"Good luck {player_name}!")

    #clear widgets or welcome screen 
    welcome_label.destroy()
    instruction_label.destroy()
    name_label.destroy()
    name_entry.destroy()
    sectionyear_label.destroy()
    sectionyear_entry.destroy()
    Start_button.destroy()
    leaderboard_button.destroy()

    player_info = f"{player_name} ({section_year})"
    
    
    def restart_program():
        main()
    
    start_quiz_game(root, player_info, restart_callback=restart_program)


def show_leaderboard():
    leaderboard_text = get_leaderboard_text()
    messagebox.showinfo("🏆 Leaderboard 🏆", leaderboard_text)


def main():
    global root, welcome_label, instruction_label, name_label, name_entry, Start_button, sectionyear_label, sectionyear_entry, leaderboard_button


#===============================Music=======================================
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('new game/Harvestmoon.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Music error: {e}")
#=======================================================================



    root = tk.Tk()
    root.title("Programming Quiz") 
    root.configure(bg="#2c3e50")
#=======================================================================

    #new add for centering window
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 650
    window_height = 750
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    # Set position and size
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)
    
    # Lock position - prevent window from being dragged
    def lock_position(event=None):
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    root.bind("<Configure>", lock_position)
    
#=================================================================

    #UI ELEMENTS 
    welcome_label = tk.Label(root, text="🎮Code Master🎮",
                             font=("Arial", 28, "bold"),
                             bg="#2c3e50", fg="#27ae60")
    welcome_label.pack(pady=20)

    instruction_label = tk.Label(root, text="Answer 30 programming questions!",  
                                 font=("Arial", 15),
                                 bg="#2c3e50", fg="white")
    instruction_label.pack(pady=15)

    name_label = tk.Label(root, text="Enter your name",
                          font=("Arial", 14),
                          bg="#2c3e50", fg="white")
    name_label.pack(pady=(30, 8))

    name_entry = tk.Entry(root, font=("Arial", 14), width=25)
    name_entry.pack(pady=8)

    sectionyear_label = tk.Label(root, text="Enter your section & year",
                                 font=("Arial", 14),
                                 bg="#2c3e50", fg="white")
    sectionyear_label.pack(pady=(20, 8))

    sectionyear_entry = tk.Entry(root, font=("Arial", 14), width=25)
    sectionyear_entry.pack(pady=8)

    Start_button = tk.Button(root, text="START QUIZ",
                             command=start_quiz,
                             font=("Arial", 14, "bold"),
                             bg="#27ae60", fg="white", width=20)
    Start_button.pack(pady=30)

    leaderboard_button = tk.Button(root, text="VIEW LEADERBOARD",
                                   command=show_leaderboard,
                                   font=("Arial", 10, "bold"),
                                   bg="#3498db", fg="white", width=17)
    leaderboard_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()