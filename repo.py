from models.models import db, User, Idea, Vote, Comment
from sqlalchemy import func

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def add_idea(user_id, content):
    idea = Idea(user_id=user_id, content=content)
    db.session.add(idea)
    db.session.commit()
    return idea

def get_all_ideas():
    return Idea.query.order_by(Idea.timestamp.desc()).all()

def vote_idea(user_id, idea_id):
    existing_vote = Vote.query.filter_by(user_id=user_id, idea_id=idea_id).first()
    if not existing_vote:
        vote = Vote(user_id=user_id, idea_id=idea_id)
        db.session.add(vote)
        db.session.commit()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_all_ideas_ordered():
    return Idea.query.order_by(Idea.timestamp.desc()).all()

def get_vote_count_for_idea(idea_id):
    return Vote.query.filter_by(idea_id=idea_id).count()

def get_all_votes_by_user_id(user_id):
    return Vote.query.filter_by(user_id=user_id).all()

#idea_id nr_voturi
def get_all_vote_counts():
    rows = db.session.query(Vote.idea_id, func.count().label("count")) \
        .group_by(Vote.idea_id).all()
    return {idea_id: count for idea_id, count in rows}

#id_user, username
def get_all_users_id_username():
    return {user.id: user.username for user in User.query.all()}

def add_comment(user_id, idea_id, content):
    comment = Comment(user_id=user_id, idea_id=idea_id, content=content)
    db.session.add(comment)
    db.session.commit()

def get_comments_by_idea_id(idea_id):
    return Comment.query.filter_by(idea_id=idea_id).order_by(Comment.timestamp).all()