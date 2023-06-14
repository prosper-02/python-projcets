# Name:  
# Student Number:  


import tkinter as tk
from tkinter import messagebox
import json
import random

class KiaGame:
    def __init__(self):
        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Missing/Invalid File", "The data file is missing or contains invalid data.")
            return

        if not self.data:
            messagebox.showerror("No Categories", "There are no categories in the data file.")
            return

        random.shuffle(self.data)

        self.index = 0
        self.total_score = 0

        self.window = tk.Tk()
        self.window.title("KIA Game")

        self.category_label = tk.Label(self.window, text="")
        self.category_label.pack()

        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.set_category()

        self.window.mainloop()

    def set_category(self):
        if self.index >= len(self.data):
            messagebox.showinfo("Game Over", f"Your total score: {self.total_score}")
            self.window.destroy()
            return

        category = self.data[self.index]
        self.category_label.configure(text=category["category"])

        self.current_category_score = 0
        self.lowercase_answers = [answer.lower() for answer in category["answers"]]

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()

        if user_answer == "":
            return

        if user_answer in self.lowercase_answers:
            self.current_category_score += category["difficulty"]
            self.lowercase_answers.remove(user_answer)
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect.")

        self.answer_entry.delete(0, tk.END)

        if len(self.lowercase_answers) == 0:
            self.current_category_score += 2 * category["difficulty"]
            messagebox.showinfo("Category Over", f"Your score for this category: {self.current_category_score}")
            self.total_score += self.current_category_score
            self.index += 1
            self.set_category()

if __name__ == "__main__":
    KiaGame()
