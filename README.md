# README.md

# User Authentication Service

Internal user authentication for our application.

## Current Method
**Password-only authentication** - Users login with username and password.

## Functions
- `authenticate_user(username, password)` - Verify user credentials
- `register_user(username, password)` - Create new user account

## Quick Start
```python
from auth import authenticate_user, register_user

# Register a new user
user = register_user("john", "secretpassword")

# Authenticate user
authenticated_user = authenticate_user("john", "secretpassword")
if authenticated_user:
    print("Login successful!")
```

## Testing
Run tests with: `python -m pytest tests/`
```

---

# docs/auth-flow.md

```markdown
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