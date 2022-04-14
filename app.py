from flask import Flask
from flask import render_template, redirect, request, url_for
from datetime import date

app = Flask(__name__)

birth_year = 0
current_age = 0

friend_list = [{"name": "Mike Colbert" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Mike\'s Friends', friends = friend_list)

@app.route('/mike')
def mike():
    return render_template('mike.html', pageTitle='About Mike')

def calculate_current_age(birth_year):
    today = date.today()
    return today.year - float(birth_year)

def calcuate_future_age(current_age):
    return current_age + 10

def calcuate_past_age(current_age):
    return current_age - 10

@app.route('/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        #capture year from form:
        form = request.form
        birth_year = form['birth_year']
        current_age = calculate_current_age(birth_year)
        if 'future_age' in request.form:
            age = calcuate_future_age(current_age)
        if 'past_age' in request.form:
            age = calcuate_past_age(current_age)
        return render_template('age.html', pageTitle='Calculate Your Age', age=age)
    return render_template('age.html', pageTitle='Calculate Your Age')

@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        friend_dict = {"name": fname + " " + lname}
        friend_list.append(friend_dict)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)