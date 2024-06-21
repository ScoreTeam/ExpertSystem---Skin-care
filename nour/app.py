from flask import Flask, request, render_template, redirect, url_for
from engine import SkinCareExpertSystem
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the expert system
expert_system = SkinCareExpertSystem()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        app.logger.debug(f"User data received: {user_data}")
        
        expert_system.declare_user_facts(user_data)
        
        next_question = expert_system.get_next_question()
        app.logger.debug(f"Next question after POST: {next_question}")

        if next_question:
            return render_template('questions.html', question=next_question)
        else:
            return redirect(url_for('recommendations'))

    app.logger.debug("Resetting expert system and running inference")
    expert_system.reset()
    expert_system.run()
    
    first_question = expert_system.get_next_question()
    app.logger.debug(f"First question after GET: {first_question}")

    if first_question:
        return render_template('questions.html', question=first_question)
    else:
        return redirect(url_for('recommendations'))

@app.route('/recommendations')
def recommendations():
    recommendations = expert_system.recommendations if hasattr(expert_system, 'recommendations') else []
    app.logger.debug(f"Recommendations: {recommendations}")
    return render_template('results.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
