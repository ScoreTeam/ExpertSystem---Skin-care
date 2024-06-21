from expert_system import SkinCareExpertSystem, Answer
from flask import Flask, render_template, request, redirect, url_for
from experta import *

app = Flask(__name__)
engine = SkinCareExpertSystem()

# Define Flask routes
@app.route('/')
def index():
    engine.reset()  # Reset engine when starting a new session
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        for key, value in request.form.items():
            engine.declare(Answer(ident=key, text=value))
        engine.run()
        return redirect(url_for('results'))
    return render_template('questions.html', questions=list(engine._initial_action()))

@app.route('/results')
def results():
    recommendations = engine.recommendations
    return render_template('results.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
