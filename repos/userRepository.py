from models.models import db, User, Idea, Vote, Comment

#id_user, username
def get_all_users_id_username():
    return {user.id: user.username for user in User.query.all()}

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user