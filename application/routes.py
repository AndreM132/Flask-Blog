from flask import render_template, url_for, redirect
from application import app, db 
from application.models import Posts
from application.forms import PostForm



@app.route('/home')
@app.route('/')
def home():
    allposts = Posts.query.all()
    return render_template('home.html', title='Home', posts=allposts)

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc='This is the about page.')

@app.route('/login')
def login():
    return render_template('login.html', title='Login', desc= 'Welcome Back!')

@app.route('/register')
def register():
    return render_template('register.html', title='Register', desc='Step right up!')

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Posts(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('posts.html', title='Post', form=form)
