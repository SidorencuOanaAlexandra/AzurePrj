import repos.userRepository as userRepository
import repos.commentRepository as commentRepository
import repos.ideaRepository as ideaRepository
import repos.voteRepository as voteRepository

def add_user(username, email, password):
    existing = userRepository.get_user_by_username(username)
    if existing:
        return None  # Username already taken
    return userRepository.create_user(username, email, password)

def authenticate_user(username, password):
    user = userRepository.get_user_by_username(username)
    if user and user.check_password(password):
        return user
    return None