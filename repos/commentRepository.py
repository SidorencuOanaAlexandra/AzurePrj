from models.models import db, User, Idea, Vote, Comment

def get_comments_by_idea_id(idea_id):
    return Comment.query.filter_by(idea_id=idea_id).order_by(Comment.timestamp).all()

def add_comment(user_id, idea_id, content):
    comment = Comment(user_id=user_id, idea_id=idea_id, content=content)
    db.session.add(comment)
    db.session.commit()