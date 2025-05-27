import repos.userRepository as userRepository
import repos.commentRepository as commentRepository
import repos.ideaRepository as ideaRepository
import repos.voteRepository as voteRepository

def add_vote(user_id, idea_id):
    voteRepository.add_vote(user_id, idea_id)

