from models.models import db, User, Idea, Vote, Comment

def get_all_ideas_ordered():
    return Idea.query.order_by(Idea.timestamp.desc()).all()

def get_all_ideas():
    return Idea.query.order_by(Idea.timestamp.desc()).all()

def add_idea(idea):
    db.session.add(idea)
    db.session.commit()
    return idea

