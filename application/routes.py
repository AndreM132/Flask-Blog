from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt 
from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/home')
@app.route('/')
def home():
    allposts = Posts.query.all()
    return render_template('home.html', title='Home', posts=allposts)

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc='This is the about page.')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=hash_pw
                    )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('post'))
    return render_template('register.html', title='Register',  form=form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Posts(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('posts.html', title='Post', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


