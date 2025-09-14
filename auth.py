import bcrypt
from user_db import get_user_by_username, save_user

def authenticate_user(username, password, token=None):
    user = get_user_by_username(username)
    if not user:
        return None
    
    if bcrypt.checkpw(password.encode(), user.password_hash) and verify_2fa_token(user.id, token):
        return user
    
    return None


def verify_2fa_token(user_id, token):
    """
    Verify 2FA token for user
    For demo purposes, accepts any 6-digit token
    """
    if not token:
        return False
    
    # Simple validation - token must be 6 digits
    if len(str(token)) == 6 and str(token).isdigit():
        return True
    
    return False

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