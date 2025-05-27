from models.models import db, User, Idea, Vote, Comment
from sqlalchemy import func

def add_vote(user_id, idea_id):
    existing_vote = Vote.query.filter_by(user_id=user_id, idea_id=idea_id).first()
    if not existing_vote:
        vote = Vote(user_id=user_id, idea_id=idea_id)
        db.session.add(vote)
        db.session.commit()

def get_vote_count_by_idea_id(idea_id):
    return Vote.query.filter_by(idea_id=idea_id).count()

def get_all_votes_by_user_id(user_id):
    return Vote.query.filter_by(user_id=user_id).all()

#idea_id nr_voturi
def get_all_vote_counts():
    rows = db.session.query(Vote.idea_id, func.count().label("count")) \
        .group_by(Vote.idea_id).all()
    return {idea_id: count for idea_id, count in rows}