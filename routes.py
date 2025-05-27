from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from utils.auth_utils import login_required
import utils.analytics as analytics
import services.commentService as commentService
import services.ideaService as ideaService
import services.userService as userService
import services.voteService as voteService

ui = Blueprint('templates', __name__)

@ui.route('/')
@login_required
def index():
    if 'user_id' not in session:
        return redirect(url_for('templates.login'))
    ideas = ideaService.list_ideas_for_user(session['user_id'])
    return render_template('index.html', ideas=ideas)

@ui.route('/submit', methods=['POST'])
@login_required
def submit():
    content = request.form['content']
    ideaService.add_idea(session['user_id'], content)
    return redirect(url_for('templates.index'))

@ui.route('/vote/<int:idea_id>')
@login_required
def vote(idea_id):
    voteService.add_vote(session['user_id'], idea_id)
    return redirect(url_for('templates.index'))

@ui.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = userService.authenticate_user(username, password)
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
        user = userService.add_user(username, email, password)
        if user:
            flash('Account created. Please login.')
            return redirect(url_for('templates.login'))
        else:
            flash('Username already taken')
    return render_template('register.html')



@ui.route('/comment/<int:idea_id>', methods=['POST'])
@login_required
def comment(idea_id):
    if 'user_id' not in session:
        return redirect(url_for('templates.login'))
    content = request.form.get('comment')

    if analytics.is_negative_comment(content):
        flash("Comentariul este negativ și nu a fost adăugat.")
        return redirect(url_for('templates.index'))

    commentService.add_comment(session['user_id'], idea_id, content)
    return redirect(url_for('templates.index'))
