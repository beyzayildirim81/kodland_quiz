from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Question Model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    option1 = db.Column(db.String(100))
    option2 = db.Column(db.String(100))
    option3 = db.Column(db.String(100))
    correct_answer = db.Column(db.String(100))

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    high_score = db.Column(db.Integer, default=0)

# Initialize the database
with app.app_context():
    db.create_all()
    if not User.query.first():  # Eğer veritabanında hiç kullanıcı yoksa, bir tane ekle
        new_user = User(name='Admin', high_score=0)
        db.session.add(new_user)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET'])
def quiz():
    questions = Question.query.all()
    best_score = User.query.first().high_score if User.query.first() else 0
    return render_template('quiz.html', questions=questions, best_score=best_score)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    questions = Question.query.all()
    for i, question in enumerate(questions, 1):
        answer = request.form.get(f"question{i}")
        if answer == question.correct_answer:
            score += 1
    
    score_percentage = (score / len(questions)) * 100
    best_score = User.query.first().high_score if User.query.first() else 0
    user = User.query.first()
    if user and score_percentage > user.high_score:
        user.high_score = score_percentage
        db.session.commit()

    return render_template('result.html', score=int(score_percentage), best_score=int(best_score))

if __name__ == '__main__':
    app.run(debug=True)
