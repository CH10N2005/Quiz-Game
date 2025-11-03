import tkinter as tk
from tkinter import messagebox
from questions import questions_database
from leaderboard import save_score, get_leaderboard_text
import random

# Global variables
current_score = 0
current_question_num = 1
total_questions = 30
current_answer = None
player_name = ""

# Widget references
score_label = None
question_text = None
current_question = None
answer_entry = None
current_question_type = "fill_in_blank"
all_fill_blank = []
all_true_false = []

def start_quiz_game(root_window, name):
    """Main entry point for quiz game"""
    global player_name, all_fill_blank, all_true_false, current_question_type, current_score, current_question_num
    
    # Reset scores
    current_score = 0
    current_question_num = 1
    
    player_name = name
    
    # Shuffle questions separately
    all_fill_blank = questions_database["fill_in_blank"].copy()
    all_true_false = questions_database["true_false"].copy()
    random.shuffle(all_fill_blank)
    random.shuffle(all_true_false)
    
    # Start with fill-in-blank
    current_question_type = "fill_in_blank"
    show_quiz_screen(root_window)

def show_quiz_screen(root):
    """Display quiz interface"""
    global score_label, question_text, current_question, answer_entry, current_question_type
    
    print("Quiz screen displayed")
    
    # Quiz title
    quiz_title = tk.Label(root, text="🎯 QUIZ TIME! 🎯",
                         font=("Arial", 21, "bold"),
                         bg="#2c3e50", fg="#27ae60")
    quiz_title.pack(pady=30)
    
    # Score display
    score_label = tk.Label(root, text=f"Score: {current_score}/{total_questions}",
                          font=("Arial", 14, "bold"),
                          bg="#2c3e50", fg="#f39c12")
    score_label.pack(pady=10)
    
    # Question counter
    question_text = tk.Label(root, text=f"Question {current_question_num} of {total_questions}:",
                            font=("Arial", 14, "bold"),
                            bg="#2c3e50", fg="white")
    question_text.pack(pady=10)
    
    # Get first question
    question_data = get_random_question()
    question_text_display = question_data["question"]
    global current_answer
    current_answer = question_data["answer"]
    
    # Question display
    current_question = tk.Label(root, text=question_text_display,
                               font=("Arial", 16),
                               bg="#2c3e50", fg="white")
    current_question.pack(pady=20)
    
    # Check question type and show appropriate input
    if current_question_num <= 15:
        # Fill-in-the-blank interface
        show_fill_blank_input(root)
    else:
        # True/False interface
        show_true_false_buttons(root)

def show_fill_blank_input(root):
    """Show text input for fill-in-the-blank questions"""
    global answer_entry
    
    answer_label = tk.Label(root, text="Your answer:",
                           font=("Arial", 12),
                           bg="#2c3e50", fg="white")
    answer_label.pack(pady=(20,5))
    
    answer_entry = tk.Entry(root, font=("Arial", 14), width=30)
    answer_entry.pack(pady=5)
    
    submit_btn = tk.Button(root, text="SUBMIT ANSWER",
                          command=check_answer,
                          font=("Arial", 12, "bold"),
                          bg="#3498db", fg="white", width=20)
    submit_btn.pack(pady=20)

def show_true_false_buttons(root):
    """Show TRUE/FALSE buttons for true/false questions"""
    
    # Buttons frame
    buttons_frame = tk.Frame(root, bg="#2c3e50")
    buttons_frame.pack(pady=30)
    
    # TRUE button
    true_btn = tk.Button(buttons_frame, text="TRUE ✓",
                        command=lambda: check_tf_answer(True),
                        font=("Arial", 14, "bold"),
                        bg="#27ae60", fg="white", 
                        width=15, height=2)
    true_btn.pack(side="left", padx=20)
    
    # FALSE button
    false_btn = tk.Button(buttons_frame, text="FALSE ✗",
                         command=lambda: check_tf_answer(False),
                         font=("Arial", 14, "bold"),
                         bg="#e74c3c", fg="white",
                         width=15, height=2)
    false_btn.pack(side="left", padx=20)

def check_answer():
    """Check if fill-in-blank answer is correct and update score"""
    global current_score, current_question_num
    
    user_answer = answer_entry.get().strip()
    if user_answer == "":
        messagebox.showerror("Error", "Please enter your answer!")
        return
    
    # Convert answer to string for comparison
    correct_answer_str = str(current_answer)
    
    if user_answer.lower() == correct_answer_str.lower():
        current_score += 1
        score_label.config(text=f"Score: {current_score}/{total_questions}")
        messagebox.showinfo("Correct! 🎉", f"Right answer: {correct_answer_str}")
        print("User got it right!")
    else:
        messagebox.showerror("Wrong ❌", f"Correct answer is: {correct_answer_str}")
        print("User got it wrong!")
    
    current_question_num += 1
    
    if current_question_num <= total_questions:
        next_question()
    else:
        show_final_score()

def check_tf_answer(user_answer):
    """Check true/false answer"""
    global current_score, current_question_num
    
    correct_answer = current_answer
    
    if user_answer == correct_answer:
        current_score += 1
        score_label.config(text=f"Score: {current_score}/{total_questions}")
        messagebox.showinfo("Correct! 🎉", f"Right answer: {correct_answer}")
        print("User got it right!")
    else:
        messagebox.showerror("Wrong ❌", f"Correct answer is: {correct_answer}")
        print("User got it wrong!")
    
    current_question_num += 1
    
    if current_question_num <= total_questions:
        next_question_tf()
    else:
        show_final_score()

def next_question():
    """Load next question for fill-in-blank"""
    global current_answer
    
    # Clear previous answer
    if answer_entry:
        answer_entry.delete(0, tk.END)
    
    # Update question counter
    question_text.config(text=f"Question {current_question_num} of {total_questions}:")
    
    # Get new question
    question_data = get_random_question()
    question_text_display = question_data["question"]
    current_answer = question_data["answer"]
    
    # Update question display
    current_question.config(text=question_text_display)
    
    # Check if we need to switch to True/False interface
    if current_question_num == 16:
        # Need to switch interface
        # This will be handled by clearing and recreating
        messagebox.showinfo("Section Complete!", "Great job! Now let's do True/False questions!")

def next_question_tf():
    """Load next question for true/false"""
    global current_answer
    
    # Update question counter
    question_text.config(text=f"Question {current_question_num} of {total_questions}:")
    
    # Get new question
    question_data = get_random_question()
    question_text_display = question_data["question"]
    current_answer = question_data["answer"]
    
    # Update question display
    current_question.config(text=question_text_display)

def get_random_question():
    """Get next question based on current question number"""
    global current_question_num
    
    # Questions 1-15: Fill in the blank
    if current_question_num <= 15:
        index = current_question_num - 1
        return all_fill_blank[index]
    # Questions 16-30: True/False
    else:
        index = current_question_num - 16
        return all_true_false[index]

def show_final_score():
    """Display final score and save to leaderboard"""
    global current_score, player_name
    
    percentage = (current_score / total_questions) * 100
    
    # Save score to leaderboard
    save_score(player_name, current_score, total_questions)
    
    # Create result message
    message = f"Quiz Complete!\n\n"
    message += f"Player: {player_name}\n"
    message += f"Final Score: {current_score}/{total_questions}\n"
    message += f"Percentage: {percentage:.1f}%\n\n"
    
    if percentage >= 90:
        message += "🏆 EXCELLENT! You're a programming master!"
    elif percentage >= 75:
        message += "👏 GREAT JOB! Keep it up!"
    elif percentage >= 50:
        message += "📚 GOOD EFFORT! Practice more!"
    else:
        message += "💪 KEEP LEARNING! You'll get better!"
    
    message += "\n\nYour score has been saved to the leaderboard!"
    
    messagebox.showinfo("Quiz Results", message)
    
    # Show leaderboard
    show_leaderboard()
    
    print(f"Final score: {current_score}/{total_questions}")

def show_leaderboard():
    """Display leaderboard in popup"""
    leaderboard_text = get_leaderboard_text()
    messagebox.showinfo("Leaderboard", leaderboard_text)