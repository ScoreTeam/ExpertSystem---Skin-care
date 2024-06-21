
from flask import Flask, request, render_template
from experta import *
from typing import Union

app = Flask(__name__)

class Answer(Fact):
    ident = Field(str)
    text = Field(str)
    cf = Field(float, mandatory=False, default=1.0)

class Question(Fact):
    ident = Field(str)
    questionType = Field(str)
    valid = Field(list or int or str)
    text = Field(str)
    cfq = Field(str, mandatory=True, default="What is your cf?")

class Ask(Fact):
    questionIdent = Field(str)
    cf = Field(float, mandatory=False, default=1.0)

class User(Fact):
    skintype = Field(str)
    skintypeconf = Field(float)
    skintone = Field(str)
    skintoneconf = Field(float)
    season = Field(str)
    seasonconf = Field(float)
    routinetype = Field(str)
    routinetypeconf = Field(float)
    sensitivity = Field(str)
    sensitivityconf = Field(float)
    sensitivitydetails = Field(str)
    sensitivitydetailsconf = Field(float)
    have_acne = Field(str)
    have_acneconf = Field(float)
    acnedetails = Field(str)
    acnedetailsconf = Field(float)
    skindeffects = Field(str)
    skindeffectsconf = Field(float)
    skincondition = Field(str)
    skinconditionconf = Field(float)
    deffectsdetails = Field(str)
    deffectsdetailsconf = Field(float)
    age = Field(str)
    ageconf = Field(float)
    gender = Field(str)
    genderconf = Field(float)
    pregnancy = Field(str)
    pregnancyconf = Field(float)
    breastfeeding = Field(str)
    breastfeedingconf = Field(float)

class Recommendations(Fact):
    product = Field(str)
    ingredients = Field(list)
    reason = Field(str)
    avoidance = Field(list)
    conf = Field(float)

class SkinCareExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []
        self.valid_cf_values = [-1.0, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]

    # Placeholder for rule definitions

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        expert_system = SkinCareExpertSystem()
        # Here we would pass user_data to the expert system
        expert_system.reset()
        expert_system.declare(User(**user_data))
        expert_system.run()
        recommendations = expert_system.recommendations
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('questions.html')

if __name__ == '__main__':
    app.run(debug=True)
