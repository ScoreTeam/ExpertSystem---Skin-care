import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageEnhance
import json
from FactClasses import *
from ProjectV2 import *
from collections import defaultdict

intro = 'logo2.png'
small = 'score.png'
background_img = 'background.png'  

with open('Qu.json', 'r') as f:
    questions = json.load(f)
with open('recommendations.json', 'r') as f:
    recommendations = json.load(f)

user_answers = []

class QuestionnaireApp:
    def __init__(self, master):
        self.master = master
        self.current_question_index = 0
        self.current_recommendation_index = 0
        self.master.attributes('-fullscreen', True)
        self.intro_img = None
        self.small_img = None
        self.background_img = None  
        self.show_intro_screen()
        self.delay=2000
        

    def display_question(self):
        if self.current_question_index < len(questions):
            current_question = questions[self.current_question_index]
            self.question_label.config(text=current_question['text'])

            for widget in self.answer_frame.winfo_children():
                widget.destroy()
            self.selected_answer = tk.StringVar(value=current_question['valid'][0])
            for i, answer in enumerate(current_question['valid']):
                rb = ttk.Radiobutton(self.answer_frame, text=answer, variable=self.selected_answer, value=answer, style="Custom.TRadiobutton")
                rb.pack(anchor=tk.W, pady=5)
        else:
            self.show_loading_page()

    def next_question(self):
        if hasattr(self, 'selected_answer') and self.selected_answer.get():
            user_answers.append(self.selected_answer.get())
            self.current_question_index += 1
            self.display_question()
        else:
            messagebox.showwarning("No Answer Selected", "Please select an answer.")

    def show_loading_page(self):
        self.question_label.config(text="Please wait while we process your answers...", font=("Arial", 18))

        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        self.progress_bar = ttk.Progressbar(self.answer_frame, mode='indeterminate')
        self.progress_bar.pack(pady=20)
        self.progress_bar.start()
        self.master.update()
        self.master.after(2000, self.stop_loading_page)

    def stop_loading_page(self):
        self.progress_bar.stop()
        self.progress_bar.destroy()
        self.show_recommendations()

    def show_recommendations(self):
        self.display_recommendation()

        self.master.bind('<Return>', lambda event: self.next_recommendation())

    def display_recommendation(self):
        if self.current_recommendation_index < len(recommendations):
            recommendation = recommendations[self.current_recommendation_index]
            recommendation_text = (
                f"Product: {recommendation['product']}\n\n"
                f"Ingredients: {', '.join(recommendation['ingredients'])}\n\n"
                f"Reason: {recommendation['reason']}\n\n"
                f"Avoidance: {', '.join(recommendation['avoidance'])}\n\n"
                f"Confidence: {recommendation.get('confidence', 'N/A')}"
            )
            self.question_label.config(text="Recommendations:", font=("Arial", 18))
            for widget in self.answer_frame.winfo_children():
                widget.destroy()

            recommendation_label = ttk.Label(self.answer_frame, text=recommendation_text, wraplength=800, padding="10", font=("Arial", 14))
            recommendation_label.pack(anchor=tk.W)
        else:
            messagebox.showinfo("End of Recommendations", "You have viewed all the recommendations.\nThank you for using our app 💚",)
            self.master.after(self.delay,self.master.quit())
            # self.master.quit()

    def next_recommendation(self):
        self.current_recommendation_index += 1
        self.display_recommendation()
    
    def show_intro_screen(self):
        style = ttk.Style()
        style.configure("Intro.TLabel", background="light green", font=('Arial', 20))
        style.configure("Intro.TFrame", background="light green", font=('Arial', 30), padding=20)
        intro_frame = ttk.Frame(self.master, style="Intro.TFrame")
        intro_frame.pack(fill=tk.BOTH, expand=True)

        intro_img_pil = Image.open(intro)
        intro_img_pil = intro_img_pil.resize((400, 400))
        self.intro_img = ImageTk.PhotoImage(intro_img_pil)
        intro_label = ttk.Label(intro_frame, image=self.intro_img, background="light green")
        intro_label.pack(pady=150)

        small_img_pil = Image.open(small)
        small_img_pil = small_img_pil.resize((100, 100))
        self.small_img = ImageTk.PhotoImage(small_img_pil)
        small_label = ttk.Label(intro_frame, image=self.small_img, background="light green")
        small_label.pack(pady=0)

        intro_frame.image = self.intro_img
        intro_frame.small_image = self.small_img

        self.master.after(2000, lambda: self.show_intro_page(intro_frame))

    def read_intro_text(self,type):
        if type == "intro" :
            with open('intro.txt', 'r') as file:
                return file.read()
        else :
            with open('outro.txt', 'r') as file:
                return file.read()

    def show_intro_page(self, previous_frame):
        previous_frame.destroy()

        style = ttk.Style()
        style.configure('IP.TLabel', background="light green", font=('Arial', 18), padding=20)
        style.configure('IP.TButton', font=('Arial', 18), padding=10, background='lightblue')

        intro_text = self.read_intro_text("intro")

        main_frame = tk.Frame(self.master, bg="light green", padx=0, pady=0)  
        main_frame.grid(row=0, column=0, sticky="nsew")

        bg_img_pil = Image.open(background_img)
        bg_img_pil = bg_img_pil.resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.background_img = ImageTk.PhotoImage(bg_img_pil)
        bg_label = tk.Label(main_frame, image=self.background_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        inner_frame = tk.Frame(main_frame, padx=20, pady=20, bg="", highlightthickness=0)
        inner_frame.grid(row=0, column=0, padx=20, pady=20)

        intro_text_label = ttk.Label(inner_frame, text=intro_text, wraplength=800, style='IP.TLabel')
        intro_text_label.grid(row=0, column=0, padx=20, pady=20)
        
        # to center 

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        self.master.after(self.delay, lambda: self.start_questionnaire(main_frame))
    def show_outro_page(self, previous_frame):
        previous_frame.destroy()
        style = ttk.Style()
        style.configure('IP.TLabel', background="light green", font=('Arial', 18), padding=20)
        style.configure('IP.TButton', font=('Arial', 18), padding=10, background='lightblue')

        intro_text = self.read_intro_text("outro")
        main_frame = tk.Frame(self.master, bg="light green", padx=0, pady=0) 
        main_frame.grid(row=0, column=0, sticky="nsew")

        bg_img_pil = Image.open(background_img)
        bg_img_pil = bg_img_pil.resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.background_img = ImageTk.PhotoImage(bg_img_pil)
        bg_label = tk.Label(main_frame, image=self.background_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        inner_frame = tk.Frame(main_frame, padx=20, pady=20, bg="", highlightthickness=0)
        inner_frame.grid(row=0, column=0, padx=20, pady=20)

        intro_text_label = ttk.Label(inner_frame, text=intro_text, wraplength=800, style='IP.TLabel')
        intro_text_label.grid(row=0, column=0, padx=20, pady=20)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(0, weight=1)
        inner_frame.grid_columnconfigure(0, weight=1)

        self.master.after(self.delay, lambda: self.start_questionnaire(main_frame))


    def start_questionnaire(self, previous_frame):
        previous_frame.destroy()

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        bg_img_pil = Image.open(background_img)
        bg_img_pil = bg_img_pil.resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.background_img = ImageTk.PhotoImage(bg_img_pil)
        bg_label = tk.Label(self.main_frame, image=self.background_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        style = ttk.Style()
        style.configure("TFrame", background="light green", font=('Arial', 30), padding=20)
        style.configure('TLabel', background="light green", font=('Arial', 18), padding=20)
        style.configure('TButton', font=('Arial', 18), padding=10, background='lightblue')
        style.configure('Custom.TRadiobutton', font=('Arial', 16), background='lightgreen')
        style.map('Custom.TRadiobutton',
                  background=[('active', 'lightgray'), ('disabled', 'lightgreen')])

        self.inner_frame = ttk.Frame(self.main_frame, padding="20", style='TFrame')
        self.inner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.question_label = ttk.Label(self.inner_frame, text="", wraplength=800, style='TLabel')
        self.question_label.grid(row=0, column=0, padx=20, pady=20, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.answer_frame = ttk.Frame(self.inner_frame, style="TFrame")
        self.answer_frame.grid(row=1, column=0, padx=20, pady=20, sticky=(tk.N, tk.S, tk.E, tk.W))


        self.display_question()

        self.master.bind('<Return>', lambda event: self.next_question())
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Questionnaire")
    
    app = QuestionnaireApp(root)

    root.mainloop()

    print("User answers:", user_answers)
    engine = SkinCareExpertSystem()
    engine.reset()
    engine.declare(User(skintype=user_answers[0], skintypeconf=1.0,
                        skintone=user_answers[1], skintoneconf=1.0,
                        season=user_answers[5], seasonconf=1.0,
                        routinetype=user_answers[6], routinetypeconf=1.0,
                        sensitivitydetails=user_answers[7], sensitivitydetailsconf=float(user_answers[8]),
                        have_acne=user_answers[11], have_acneconf=float(user_answers[13]),
                        acnedetails=user_answers[12], acnedetailsconf=float(user_answers[13]),
                        skincondition=user_answers[9], skinconditionconf=float(user_answers[10]),
                        age=user_answers[4], ageconf=1.0,
                        gender=user_answers[2], genderconf=1.0,
                        pregnancy=user_answers[3], pregnancyconf=1.0,
                        breastfeeding=user_answers[3], breastfeedingconf=1.0,
                        ))
    engine.run()
    print(engine.facts)
