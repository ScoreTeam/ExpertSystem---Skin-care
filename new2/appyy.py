from flask import Flask, request, render_template
from Project import SkinCareExpertSystem, User  # Ensure correct import from Project.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    # Retrieve form data
    routine_type = request.form['routine_type']
    season = request.form['season']
    skin_condition = request.form['skin_condition']
    sensitivity_details = request.form['sensitivity_details']
    sensitivity_conf = float(request.form['sensitivity_conf'])
    skin_condition_conf = float(request.form['skin_condition_conf'])
    
    # Initialize and run the expert system
    engine = SkinCareExpertSystem()
    engine.reset()
    engine.declare(User(
        routinetype=routine_type,
        season=season,
        skincondition=skin_condition,
        sensitivitydetails=sensitivity_details,
        sensitivityconf=sensitivity_conf,
        skinconditionconf=skin_condition_conf
    ))
    engine.run()
    
    # Extract recommendations
    recommendations = engine.facts
    
    return render_template('recommendations.html', 
                           routine_type=routine_type, 
                           season=season, 
                           skin_condition=skin_condition, 
                           sensitivity_details=sensitivity_details, 
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
