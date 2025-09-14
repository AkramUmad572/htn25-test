python
import pytest
from auth import authenticate_user, register_user

class TestAuthentication:
    
    def setup_method(self):
        """Setup test data before each test"""
        # Clear any existing test data
        clear_test_database()
    
    def test_register_user_success(self):
        """Test successful user registration"""
        user = register_user("testuser", "password123")
        
        assert user is not None
        assert user.username == "testuser"
        assert hasattr(user, 'password_hash')
    
    def test_register_user_duplicate(self):
        """Test registration with existing username"""
        register_user("testuser", "password123")
        
        # Second registration should fail
        duplicate_user = register_user("testuser", "differentpassword")
        assert duplicate_user is None
    
    def test_authenticate_user_success(self):
        """Test successful authentication"""
        register_user("testuser", "password123")
        
        user = authenticate_user("testuser", "password123")
        assert user is not None
        assert user.username == "testuser"
    
    def test_authenticate_user_wrong_password(self):
        """Test authentication with wrong password"""
        register_user("testuser", "password123")
        
        user = authenticate_user("testuser", "wrongpassword")
        assert user is None
    
    def test_authenticate_user_nonexistent(self):
        """Test authentication with non-existent user"""
        user = authenticate_user("nonexistent", "password123")
        assert user is None
    
    def test_authenticate_user_empty_password(self):
        """Test authentication with empty password"""
        register_user("testuser", "password123")
        
        user = authenticate_user("testuser", "")
        assert user is None
    
    def test_full_workflow(self):
        """Test complete registration and authentication workflow"""
        username = "workflowtest"
        password = "testpass456"
        
        # 1. Register user
        user = register_user(username, password)
        assert user is not None
        
        # 2. Authenticate with correct credentials
        authenticated_user = authenticate_user(username, password)
        assert authenticated_user is not None
        assert authenticated_user.username == username
        
        # 3. Verify wrong password fails
        wrong_auth = authenticate_user(username, "wrongpass")
        assert wrong_auth is None


class TestIntegrationPatterns:
    """Test common integration patterns"""
    
    def setup_method(self):
        clear_test_database()
        register_user("integrationuser", "integrationpass")
    
    def test_login_handler_pattern(self):
        """Test typical login handler usage"""
        def handle_login(username, password):
            user = authenticate_user(username, password)
            if user:
                return {"success": True, "user_id": user.id}
            else:
                return {"success": False, "error": "Invalid credentials"}
        
        # Test successful login
        result = handle_login("integrationuser", "integrationpass")
        assert result["success"] is True
        assert "user_id" in result
        
        # Test failed login
        result = handle_login("integrationuser", "wrongpass")
        assert result["success"] is False
        assert result["error"] == "Invalid credentials"
    
    def test_middleware_pattern(self):
        """Test middleware-style authentication"""
        def require_auth(username, password):
            user = authenticate_user(username, password)
            if not user:
                raise ValueError("Authentication failed")
            return user
        
        # Should succeed with valid credentials
        user = require_auth("integrationuser", "integrationpass")
        assert user is not None
        
        # Should raise exception with invalid credentials
        with pytest.raises(ValueError, match="Authentication failed"):
            require_auth("integrationuser", "wrongpass")


def clear_test_database():
    """Helper function to clear test database"""
    # Implementation depends on your database setup
    pass