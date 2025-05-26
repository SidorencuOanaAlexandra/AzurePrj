# templates/routes.py
from flask import Blueprint, render_template, redirect, request, session, url_for, flash
import service
import templates

ui = Blueprint('templates', __name__)

@ui.route('/')
def index():
    # if 'user_id' not in session:
    #     return redirect(url_for('templates.login'))
    # ideas = service.list_ideas_for_user(session['user_id'])
    # return render_template('index.html', ideas=ideas)
    return render_template('login.html')

@ui.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    service.submit_idea(session['user_id'], content)
    return redirect(url_for('templates.index'))

@ui.route('/vote/<int:idea_id>')
def vote(idea_id):
    service.add_vote(session['user_id'], idea_id)
    return redirect(url_for('templates.index'))

@ui.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = service.authenticate_user(username, password)
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('templates.index'))
        else:
            flash('Login failed')
    return render_template('login.html')

@ui.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = service.register_user(username, email, password)
        if user:
            flash('Account created. Please login.')
            return redirect(url_for('templates.login'))
        else:
            flash('Username already taken')
    return render_template('register.html')

@ui.route('/comment/<int:idea_id>', methods=['POST'])
def comment(idea_id):
    if 'user_id' not in session:
        return redirect(url_for('templates.login'))
    content = request.form.get('comment')
    service.add_comment(session['user_id'], idea_id, content)
    return redirect(url_for('templates.index'))
