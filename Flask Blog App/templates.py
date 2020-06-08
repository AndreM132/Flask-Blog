from flask import render_template, url_for
from application import app


blogData = [
    {
        "name": {"first":"Mike", "last":"Ike"},
        "title":"First Post",
        "content":"Blog data for Flask lectures"
    },
    {
        "name": {"first":"Danny", "last":"Manny"},
        "title":"Second Post",
        "content":"Even more blog data for Flask lectures"
    }
]



@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home', posts=blogData)

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc='This is the about page.')

@app.route('/login')
def login():
    return render_template('login.html', title='Login', desc= 'Welcome Back!')

@app.route('/register')
def register():
    return render_template('register.html', title='Register', desc='Step right up!')

~                                                                                          