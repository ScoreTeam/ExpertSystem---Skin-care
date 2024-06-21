from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {"id": 1, "text": "What is your skin type?", "ident": "skin_type"},
    {"id": 2, "text": "Do you have acne?", "ident": "acne"},
    {"id": 3, "text": "How sensitive is your skin?", "ident": "sensitivity"}
]

recommendations = [
    "Use a gentle cleanser",
    "Moisturize daily",
    "Apply sunscreen"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    return redirect(url_for('question', question_id=1))

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    if request.method == 'POST':
        ident = request.form['ident']
        answer = request.form['text']
        cf = float(request.form['cf'])
        print(f"Question ID: {ident}, Answer: {answer}, CF: {cf}")

        next_question_id = question_id + 1
        if next_question_id > len(questions):
            return redirect(url_for('recommendations'))
        else:
            return redirect(url_for('question', question_id=next_question_id))

    # Find the question by matching the question_id
    question = None
    for q in questions:
        if q["id"] == question_id:
            question = q
            break

    if question is None:
        return "Question not found", 404

    return render_template('questions.html', question=question, question_id=question_id)

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
