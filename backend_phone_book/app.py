from flask import Flask, render_template, request, redirect, url_for
from models import db, Person
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://username:password@localhost:1521/XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





# Add route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement login logic here
    return render_template('login.html')

# Add route for main screen
@app.route('/main', methods=['GET', 'POST'])
def main():
    # Implement main screen logic here
    return render_template('main.html')

# Add route for person screen
@app.route('/person/<int:person_id>', methods=['GET', 'POST'])
def person(person_id):
    # Implement person screen logic here
    return render_template('person.html')

# Example: Add new person
@app.route('/main/new_contact', methods=['POST'])
def new_contact():
    name = request.form['name']
    phone_number = request.form['phone_number']
    
    new_person = Person(name=name, phone_number=phone_number)
    db.session.add(new_person)
    db.session.commit()

    return redirect(url_for('main'))





db.init_app(app)
