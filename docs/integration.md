# Integration Guide

## Login Flow
```python
from auth import authenticate_user

def handle_login(username, password):
    user = authenticate_user(username, password)
    if user:
        token = create_session_token(user.id)
        return {"success": True, "token": token}
    else:
        return {"success": False, "error": "Invalid credentials"}
```

## Registration Flow
```python
from auth import register_user

def handle_signup(username, password):
    user = register_user(username, password)
    if user:
        return {"success": True, "user_id": user.id}
    else:
        return {"success": False, "error": "Username already exists"}
```

## Middleware Integration
```python
def require_auth(username, password):
    """Middleware to verify authentication"""
    user = authenticate_user(username, password)
    if not user:
        raise AuthenticationError("Invalid credentials")
    return user
```

## Testing
```python
def test_login():
    register_user("testuser", "password123")
    
    # Should succeed with correct password
    user = authenticate_user("testuser", "password123")
    assert user is not None
    
    # Should fail with wrong password
    user = authenticate_user("testuser", "wrongpassword")
    assert user is None
```

## Error Handling
- Returns `None` for invalid credentials
- No exceptions for authentication failures
- Simple true/false authentication

## Common Patterns
```python
# Pattern 1: Simple check
user = authenticate_user(username, password)
if user:
    proceed_with_login(user)

# Pattern 2: With error handling
user = authenticate_user(username, password)
if user is None:
    return error_response("Login failed")

# Pattern 3: In decorators
def login_required(func):
    def wrapper(username, password, *args, **kwargs):
        user = authenticate_user(username, password)
        if not user:
            return {"error": "Authentication required"}
        return func(user, *args, **kwargs)
    return wrapper
```
