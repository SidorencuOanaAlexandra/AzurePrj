import repos.commentRepository as commentRepository

def add_comment(user_id, idea_id, content):
    commentRepository.add_comment(user_id, idea_id, content)

# def notify_owner_by_email(owner_email, commenter, comment_text):
#     url = "https://commentnotify123.azurewebsites.net/api/send_comment_email"
#     data = {
#         "owner_email": owner_email,
#         "commenter": commenter,
#         "comment": comment_text
#     }
#
#     try:
#         response = requests.post(url, json=data)
#         print("Status email:", response.text)
#     except Exception as e:
#         print("Eroare trimitere email:", e)
