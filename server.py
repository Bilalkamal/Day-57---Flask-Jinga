from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().strftime("%Y")
    return render_template("index.html", year = year)

@app.route('/guess/<name>')
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    nation = get_nationality(name)
    return render_template('guess.html',name = name, nation = nation, gender = gender, age = age)

def get_age(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    return age

def get_nationality(name):
    nation = requests.get(f'https://api.nationalize.io?name={name}').json()['country'][0]['country_id']
    return nation

def get_gender(name):
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    return gender

@app.route('/blog')
def blog():
    blogs = requests.get("https://api.npoint.io/481a7600531b2b6e139d").json()
    print(blogs)
    return render_template("blog.html", blogs = blogs)

if __name__ == '__main__':
    app.run(debug=True)
    
    
