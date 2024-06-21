import tkinter as tk
from tkinter import messagebox, ttk
from experta import Fact
from rules import SkinCareExpertSystem
from facts import SkinCareFact, EndOfQuestionsFact
import tkinter.font as font

class SkinCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skin Care Expert System")
        self.root.geometry("600x400")
        self.root.configure(bg="#2a3b4e")

        self.engine = SkinCareExpertSystem()
        self.engine.reset()

        self.current_fact = None
        self.response_var = tk.StringVar()

        self.setup_ui()
        self.asked_facts = set()
        self.display_next_question()

        # Bind Enter key to submit action
        self.root.bind('<Return>', lambda event: self.process_input())

    def setup_ui(self):
        # Create main frame
        main_frame = tk.Frame(self.root, bg="#2e3b4e", padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Create custom fonts
        header_font = font.Font(family="Helvetica", size=18, weight="bold")
        text_font = font.Font(family="Helvetica", size=14)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")

        # Create and pack question label
        self.question_label = tk.Label(main_frame, text="Welcome to the Skin Care Expert System!", font=header_font, bg="#2e3b4e", fg="#ffffff", wraplength=500, justify=tk.CENTER)
        self.question_label.pack(pady=20)

        # Create and pack response entry
        self.response_entry = tk.Entry(main_frame, textvariable=self.response_var, font=text_font, bg="#ffffff", fg="#000000", relief=tk.FLAT, borderwidth=5)
        self.response_entry.pack(pady=10, fill=tk.X, padx=50)

        # Create and pack submit button
        self.submit_button = tk.Button(main_frame, text="Submit", command=self.process_input, font=button_font, bg="#4a90e2", fg="#ffffff", activebackground="#357ABD", activeforeground="#ffffff", relief=tk.FLAT)
        self.submit_button.pack(pady=20)

        # Create and pack recommendations label
        self.recommendations_label = tk.Label(main_frame, text="", font=text_font, bg="#2e3b4e", fg="#ffffff", wraplength=500, justify=tk.CENTER)
        self.recommendations_label.pack(pady=20)

    def display_next_question(self):
        self.engine.run()
        new_questions = []
        for fact in self.engine.facts.values():
            if isinstance(fact, SkinCareFact) and fact.get("question") and fact["field"] not in self.asked_facts:
                new_questions.append(fact)
                self.asked_facts.add(fact["field"])  # Add new question to asked questions
        if new_questions:
            self.current_fact = new_questions[0]  # Set current fact to the first new question
            self.question_label.config(text=self.current_fact["question"])
            self.response_var.set('')
            self.response_entry.focus()  # Set focus to the entry field for quick typing
        else:
            self.question_label.config(text="Thank you for your responses. Check the console for recommendations.")
            self.engine.declare(SkinCareFact(question='Based on your answers, here are the recommended products and routine:', field='recommendation'))
            self.engine.declare(EndOfQuestionsFact())
            self.response_entry.pack_forget()
            self.submit_button.pack_forget()
            self.engine.save_graph('skin_care_expert_system')

    def process_input(self):
        user_value = self.response_entry.get().strip()
        if not user_value:
            messagebox.showerror("Error", "Please enter a value.")
            return

        if self.current_fact is not None:
            fact_id = self.current_fact.get('__factid__')  # Extract fact ID
            if fact_id is not None and fact_id in self.engine.facts:
                try:
                    self.engine.modify(self.engine.facts[fact_id], **{self.current_fact['field']: user_value})
                except IndexError:
                    messagebox.showerror("Error", "Fact not found in the engine's fact list.")
                    return
                self.display_next_question()
            else:
                messagebox.showerror("Error", "Invalid fact ID.")
        else:
            messagebox.showerror("Error", "No current fact to modify.")
             
if __name__ == "__main__":
    root = tk.Tk()
    app = SkinCareApp(root)
    root.mainloop()
