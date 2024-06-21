# # -*- coding: utf-8 -*-
# from experta import KnowledgeEngine, DefFacts, Rule, Fact, MATCH, NOT, AS
# from facts import User, Recommendations, Answer, Question, Ask

# class SkinCareExpertSystem(KnowledgeEngine):
#     def __init__(self):
#         super().__init__()
#         # this is for the tree @nour we can still do it if we have time ✌
#         # self.graph = graphviz.Digraph(comment='Skin Care Expert System')
#         self.recommendations = []
#         self.valid_cf_values = [-1.0, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
#          # keep it just in case:
#         # ----
#         # self.CleanserRecommendations = []
#         # self.MoisturizerRecommendations = []
#         # self.SunscreenRecommendations = []
#         # self.GenderRec = []
#         # self.SenRec = []
#         # self.pregrec = []
#         # ----

#     @DefFacts()
#     def _initial_action(self):
#         # yield Question(question='What is your gender? (1: Female, 2: Male)', field='gender')
#         # Noore ways (from labs)
#         yield Question(
#             ident="Skin Type",
#             questionType="multi",
#             valid=["dry", "oily", "normal", "combination"],
#             text="What is your skin type ?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="SkinTone",
#             questionType="multi",
#             valid=["fair", "medium", "dark"],
#             text="What is your skin tone ?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="Gender",
#             questionType="multi",
#             valid=["female", "male"],
#             text="What is your gender sir/mam?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="pregnancy",
#             questionType="multi",
#             valid=["yes", "no"],
#             text="are you pregnant or currently breastfeeding",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="Acne",
#             questionType="multi",
#             valid=["yes", "no"],
#             text="Do you happen to have acne ?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="Age",
#             questionType="multi",
#             valid=["young", "adult", "mature"],
#             text="How old are you?",
#             cfq="What is your cf?"
#         )
#         ## noore's notes: im against putting season because again seasons doesn's represent real
#         # enviroment temperature , instead we should use temperature or enviroment
#         yield Question(
#             ident="season",
#             questionType="multi",
#             valid=["summer", "winter", "spring", "automn"],
#             text="What is the current season in your location?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="routine",
#             questionType="multi",
#             valid=["morning", "night", "both"],
#             text="What type of routine are you looking for?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="sensitvity",
#             questionType="multi",
#             valid=["yes", "no"],
#             text="Do you consider your skin to be sensitive?",
#             cfq="What is your cf?"
#         )
#         # @Laila : fill these informations 🤝,and dont remove Not any keep it as a choice
#         yield Question(
#             ident="sensitvity details",
#             questionType="multi",
#             valid=["Not any", "allergy to salicylic acid", "Fragrance Allergy", "Food", "Chemicals", "Preservative"],
#             text="Provide sens det?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="skin condition",
#             questionType="multi",
#             valid=["Not any", "Rosacea", "Eczema", "Perioral Dermatitis", "Periorific Dermatitis", "Seborrheic Dermatitis (scalp)", "Seborrheic Dermatitis (face)"],
#             text="Do you have any of those skin condition",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="acne details",
#             questionType="multi",
#             valid=["Not any", "moderte", "severe"],
#             text="How bad is your acne ?",
#             cfq="What is your cf?"
#         )
#         yield Question(
#             ident="skin defects",
#             questionType="multi",
#             valid=["yes", "no"],
#             text="Do you have any skin defects?",
#             cfq="What is your cf?"
#         )
#         # @laila fill these up too please 👐
#         yield Question(
#             ident="skin defects details",
#             questionType="multi",
#             valid=["Not any", "yes", "no"],
#             text="IDK (skin defs dets)?",
#             cfq="What is your cf?"
#         )

#     def validateAnswer(self, answer, questionType, valid):
#         if questionType == "multi" and answer in valid:
#             return True
#         if questionType == "number" and answer.isdigit() and int(answer) in valid:
#             return True

#         return False

#     def ask_user(self, question, questionType, valid, cfq):
#         answer = ""
#         cf = None

#         while not self.validateAnswer(answer, questionType, valid):
#             print(question)
#             if questionType == "multi":
#                 print("Valid answers are: " + ", ".join(valid))
#             elif questionType == "number":
#                 print(f"Valid range is: {valid[0]}-{valid[-1]}")
#             answer = input(question + "?\n" + 'Enter your answer: ')
#         # cf = float(input('Enter your cf: '))
#         while cf not in self.valid_cf_values:
#             print("Please enter a valid value from the list [-1.0, -0.5, 0, 0.5, 1]")
#             # cf = float(input('Enter your cf : '))

#             while True:
#                 try:
#                     cf = float(input('Enter your cf: '))
#                     if cf in self.valid_cf_values:
#                         break
#                     else:
#                         print("Invalid value, please enter a valid cf from the list.")
#                 except ValueError:
#                     print("Invalid input, please enter a float value.")

#         print("Valid value entered: ", cf)
#         print('your answer is: ' + str(answer) + ' with cf = ' + str(cf))

#         return answer, cf

#     def recommend_action(self, action):
#         print("I recommend that you " + action + "\n")

#     # this wont be called for now
#     # def success(self):
#     #     print('Your PC runs successfully, no further actions should be taken.')

#     # def failure(self):
#     #     print('We couldn\'t find the right products for you')
#     #     self.recommend_action('consult a real dermatologist')


###############################################################################NOUR

# from experta import KnowledgeEngine, DefFacts, Rule, Fact, MATCH, NOT, AS
# from facts import User, Recommendations, Answer, Question, Ask
# import json
# import os

# class SkinCareExpertSystem(KnowledgeEngine):
#     def __init__(self):
#         super().__init__()
#         # this is for the tree @nour we can still do it if we have time ✌
#         # self.graph = graphviz.Digraph(comment='Skin Care Expert System')
#         self.recommendations = []
#         self.questions = self.load_questions_from_json('questions.json')
#         self.valid_cf_values = self.load_valid_cf_values_from_json('valid_values.json')['valid_cf_values']
#          # keep it just in case:
#         # ----
#         # self.CleanserRecommendations = []
#         # self.MoisturizerRecommendations = []
#         # self.SunscreenRecommendations = []
#         # self.GenderRec = []
#         # self.SenRec = []
#         # self.pregrec = []
#         # ----

#     def load_questions_from_json(self, filename):
#         with open(filename, 'r') as f:
#             return json.load(f)

#     def load_valid_cf_values_from_json(self, filename):
#         with open(filename, 'r') as f:
#             return json.load(f)

#     @DefFacts()
#     def _initial_action(self):
#         for key, details in self.questions.items():
#             yield Question(ident=key, questionType=details['questionType'], valid=details['valid'],
#                            text=details['text'], cfq=details['cfq'])

#     def validateAnswer(self, answer, questionType, valid):
#         if questionType == "multi" and answer in valid:
#             return True
#         if questionType == "number" and answer.isdigit() and int(answer) in valid:
#             return True
#         return False

#     def ask_user(self, question, questionType, valid, cfq):
#         answer = ""
#         cf = None

#         while not self.validateAnswer(answer, questionType, valid):
#             print(question)
#             if questionType == "multi":
#                 print("Valid answers are: " + ", ".join(valid))
#             elif questionType == "number":
#                 print(f"Valid range is: {valid[0]}-{valid[-1]}")
#             answer = input('Enter your answer: ')

#         while cf not in self.valid_cf_values:
#             try:
#                 cf = float(input('Enter your cf: '))
#                 if cf in self.valid_cf_values:
#                     break
#                 else:
#                     print("Invalid value, please enter a valid cf from the list.")
#             except ValueError:
#                 print("Invalid input, please enter a float value.")

#         print(f'Valid value entered: {cf}')
#         print(f'Your answer is: {answer} with cf = {cf}')

#         return answer, cf

#     def recommend_action(self, action):
#         print(f"I recommend that you {action}\n")

#     # this wont be called for now
#     # def success(self):
#     #     print('Your PC runs successfully, no further actions should be taken.')

#     # def failure(self):
#     #     print('We couldn\'t find the right products for you')
#     #     self.recommend_action('consult a real dermatologist')

###############################################################################NOUR

import os
import json
from experta import KnowledgeEngine, DefFacts, Rule, Fact, MATCH, NOT, AS
from facts import User, Recommendations, Answer, Question, Ask

class SkinCareExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []
        self.questions = self.load_questions_from_json(self.get_full_path('questions.json'))
        self.valid_cf_values = self.load_valid_cf_values_from_json(self.get_full_path('valid_values.json'))['valid_cf_values']

    def get_full_path(self, filename):
        return os.path.join(os.path.dirname(__file__), filename)

    def load_questions_from_json(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def load_valid_cf_values_from_json(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    @DefFacts()
    def _initial_action(self):
        for key, details in self.questions.items():
            yield Question(ident=key, questionType=details['questionType'], valid=details['valid'],
                           text=details['text'], cfq=details['cfq'])

    def validateAnswer(self, answer, questionType, valid):
        if questionType == "multi" and answer in valid:
            return True
        if questionType == "number" and answer.isdigit() and int(answer) in valid:
            return True
        return False

    def ask_user(self, question, questionType, valid, cfq):
        answer = ""
        cf = None

        while not self.validateAnswer(answer, questionType, valid):
            print(question)
            if questionType == "multi":
                print("Valid answers are: " + ", ".join(valid))
            elif questionType == "number":
                print(f"Valid range is: {valid[0]}-{valid[-1]}")
            answer = input('Enter your answer: ')

        while cf not in self.valid_cf_values:
            try:
                cf = float(input('Enter your cf: '))
                if cf in self.valid_cf_values:
                    break
                else:
                    print("Invalid value, please enter a valid cf from the list.")
            except ValueError:
                print("Invalid input, please enter a float value.")

        print(f'Valid value entered: {cf}')
        print(f'Your answer is: {answer} with cf = {cf}')

        return answer, cf

    def recommend_action(self, action):
        print(f"I recommend that you {action}\n")

