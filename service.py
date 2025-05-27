import requests
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import Config
from models.models import db, User, Idea, Vote, Comment
import repos.userRepository as userRepository
import repos.commentRepository as commentRepository
import repos.ideaRepository as ideaRepository
import repos.voteRepository as voteRepository

def submit_idea(user_id, content):
    sentiment = get_sentiment(content)
    idea = Idea(user_id=user_id, content=content, sentiment=sentiment)

    return ideaRepository.add_idea(idea)

def list_ideas():
    return ideaRepository.get_all_ideas()

def add_vote(user_id, idea_id):
    voteRepository.add_vote(user_id, idea_id)

def register_user(username, email, password):
    existing = userRepository.get_user_by_username(username)
    if existing:
        return None  # Username already taken
    return userRepository.create_user(username, email, password)

def authenticate_user(username, password):
    user = userRepository.get_user_by_username(username)
    if user and user.check_password(password):
        return user
    return None

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
    commentRepository.add_comment(user_id, idea_id, content)

def notify_owner_by_email(owner_email, commenter, comment_text):
    url = "https://commentnotify123.azurewebsites.net/api/send_comment_email"
    data = {
        "owner_email": owner_email,
        "commenter": commenter,
        "comment": comment_text
    }

    try:
        response = requests.post(url, json=data)
        print("Status email:", response.text)
    except Exception as e:
        print("Eroare trimitere email:", e)

credential = AzureKeyCredential(Config.key)
text_analytics_client = TextAnalyticsClient(endpoint=Config.endpoint, credential=credential)

def is_negative_comment(comment_text):
    try:
        #response = text_analytics_client.analyze_sentiment([comment_text])[0]
        return get_sentiment(comment_text) == "negative"
    except Exception as e:
        print("Eroare analiză sentiment:", e)
        return False

def get_sentiment(text):
    response = text_analytics_client.analyze_sentiment([text])[0]

    return response.sentiment