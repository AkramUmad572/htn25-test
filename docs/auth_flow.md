# Authentication Flow

## Current Implementation

Simple password-based authentication:

```python
def authenticate_user(username, password):
    """
    Authenticate user with username/password
    Returns user object if valid, None if invalid
    """
    user = get_user_by_username(username)
    if user and verify_password_hash(password, user.password_hash):
        return user
    return None
```

## Login Process
1. User provides username and password
2. Password verified against stored hash
3. User object returned if valid

## Security
- Password-only authentication
- bcrypt password hashing
- No additional verification steps

## Example Usage
```python
def login_handler(username, password):
    user = authenticate_user(username, password)
    if user:
        return {"status": "success", "user_id": user.id}
    else:
        return {"status": "failed", "error": "Invalid credentials"}
```