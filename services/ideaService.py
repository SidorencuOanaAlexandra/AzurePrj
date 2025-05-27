import repos.userRepository as userRepository
import repos.commentRepository as commentRepository
import repos.ideaRepository as ideaRepository
import repos.voteRepository as voteRepository
import utils.analytics as analytics
from models.models import db, User, Idea, Vote, Comment

def get_all_ideas():
    return ideaRepository.get_all_ideas()

def list_ideas_for_user(user_id):
    ideas = ideaRepository.get_all_ideas_ordered()

    user_votes = voteRepository.get_all_votes_by_user_id(user_id)
    user_voted_idea_ids = {vote.idea_id for vote in user_votes}
    idea_votes = voteRepository.get_all_vote_counts()
    user_ids = userRepository.get_all_users_id_username()

    result = []
    for idea in ideas:
        vote_count = idea_votes.get(idea.id, 0)
        user_voted = idea.id in user_voted_idea_ids
        comments = commentRepository.get_comments_by_idea_id(idea.id)
        ideaViewContent = idea.content + " (" + str(idea.sentiment) + ")"

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
            "content": ideaViewContent,
            "username": user_ids.get(idea.user_id, "Utilizator necunoscut"),
            "date": idea.timestamp.strftime('%d.%m.%Y %H:%M'),
            "vote_count": vote_count,
            "voted": user_voted,
            "comments": comment_list
        })
    return result

def add_idea(user_id, content):
    sentiment = analytics.get_sentiment(content)
    idea = Idea(user_id=user_id, content=content, sentiment=sentiment)

    return ideaRepository.add_idea(idea)