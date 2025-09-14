import bcrypt
from user_db import get_user_by_username, save_user

# authenticate user
def authenticate_user(username, password):
    """
    Authenticate user with password only
    """
    user = get_user_by_username(username)
    if not user:
        return None
    
    # Simple password verification
    if bcrypt.checkpw(password.encode(), user.password_hash):
        return user
    
    return None

# user registration
def register_user(username, password):
    """
    Register new user with password
    """
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_data = {
        'username': username,
        'password_hash': password_hash
    }
    return save_user(user_data)
