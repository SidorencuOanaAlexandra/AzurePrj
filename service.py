import repo

def submit_idea(user_id, content):
    return repo.add_idea(user_id, content)

def list_ideas():
    return repo.get_all_ideas()

def add_vote(user_id, idea_id):
    repo.vote_idea(user_id, idea_id)

def register_user(username, email, password):
    existing = repo.get_user_by_username(username)
    if existing:
        return None  # Username already taken
    return repo.create_user(username, email, password)

def authenticate_user(username, password):
    user = repo.get_user_by_username(username)
    if user and user.check_password(password):
        return user
    return None

def list_ideas_for_user(user_id):
    ideas = repo.get_all_ideas_ordered()

    user_votes = repo.get_all_votes_by_user_id(user_id)
    user_voted_idea_ids = {vote.idea_id for vote in user_votes}
    idea_votes = repo.get_all_vote_counts()
    user_ids = repo.get_all_users_id_username()

    result = []
    for idea in ideas:
        vote_count = idea_votes.get(idea.id, 0)
        user_voted = idea.id in user_voted_idea_ids
        comments = repo.get_comments_by_idea_id(idea.id)

        comment_list = [
            {
                "author": user_ids.get(comment.user_id, "Utilizator necunoscut"),
                "date": comment.timestamp.strftime('%d.%m.%Y %H:%M'),
                "content": comment.content
            }
            for comment in comments
        ]

        result.append({
            "id": idea.id,
            "content": idea.content,
            "username": user_ids.get(idea.user_id, "Utilizator necunoscut"),
            "date": idea.timestamp.strftime('%d.%m.%Y %H:%M'),
            "vote_count": vote_count,
            "voted": user_voted,
            "comments": comment_list
        })
    return result

def add_comment(user_id, idea_id, content):
    repo.add_comment(user_id, idea_id, content)