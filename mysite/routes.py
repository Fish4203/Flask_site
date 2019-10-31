from flask import render_template, flash, redirect, request, url_for
from flask_app import app, db
from models import Post, User
from fourms import Login, Sign_up, Postmain, Profile_form
from flask_login import current_user, login_user, logout_user, login_required
from models import User

@app.route('/')
def hello_world():
    post_dic = []
    db_out = Post.query.all()
    for post in range(len(db_out)):
        post_dic.append({'title' : db_out[post].Title, 'text' : db_out[post].Body, 'user' : User.query.get(db_out[post].User)})

    return render_template('index.html', posts=post_dic)

@app.route('/Sign_in', methods=['GET', 'POST'])
def Sign_in():
    form = Login()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        user = User.query.filter_by(Name=form.Username.data).first()

        if user is None or not user.check_pass(form.Password.data):
            flash('Invalid username or password')
            return redirect('/Sign_in')

        login_user(user, remember=form.Save.data)

        next_page = request.args.get('next')
        if not next_page:
            next_page = '/'
        #return redirect('/')
        return redirect(next_page)

    return render_template('sign_in.html', title='sign in', form=form)


@app.route('/regester', methods=['GET', 'POST'])
def regester():
    form = Sign_up()

    if current_user.is_authenticated:
        return redirect('/')

    if form.validate_on_submit():
        #form.email_used(form.Emailenter.data)
        #form.username_used(form.Username.data)

        user = User(Name=form.Username.data, Email=form.Emailenter.data)
        user.gen_pass(form.Password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/Sign_in')

    return render_template('regestration.html', title='regestration', form=form)

@app.route('/Post_main', methods=['GET', 'POST'])
@login_required
def Post_main():
    form = Postmain()

    if current_user.is_anonymous:
        return redirect('/')

    if form.validate_on_submit():
        post = Post(Title=form.Post_title.data, Body=form.Post_body.data, User=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect('/')

    return render_template('Post_main.html', title='Make a post', form=form)

@app.route('/Profile', methods=['GET', 'POST'])
@login_required
def Profile():
    form = Profile_form()

    post_dic = []
    db_out = Post.query.filter_by(User = current_user.id).all()

    post_count = len(db_out)

    for post_db in db_out:
        post_dic.append({'title' : post_db.Title, 'text' : post_db.Body, 'user' : User.query.get(post_db.User), 'id' : post_db.id})

    return render_template('profile.html', posts=post_dic, post_count=post_count, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
