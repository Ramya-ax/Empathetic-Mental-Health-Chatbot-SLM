sessions = {}

def get_chat_history(session_id):
    if session_id not in sessions:
        sessions[session_id] = []
    return sessions[session_id]

def update_history(session_id, user, bot):
    sessions[session_id].append({
        "user": user,
        "bot": bot
    })