import hashlib
from datetime import datetime, timedelta

class User:
    """
    A class for handling user authentication, password management,
    and session tracking.
    """
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self._password_hash = None
        self._login_attempts = 0
        self._locked_until = None
        self._session_token = None
        self._last_active = None

    def set_password(self, password: str) -> None:
        """Hash and store the password"""
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        """Verify password and handle login attempts"""
        if self._locked_until and datetime.now() < self._locked_until:
            raise ValueError("Account is temporarily locked")

        is_correct = self._password_hash == hashlib.sha256(password.encode()).hexdigest()
        
        if not is_correct:
            self._login_attempts += 1
            if self._login_attempts >= 3:
                self._locked_until = datetime.now() + timedelta(minutes=15)
                raise ValueError("Too many failed attempts. Account locked for 15 minutes")
        else:
            self._login_attempts = 0
            self._create_session()
        
        return is_correct

    def _create_session(self) -> None:
        """Create a new session token"""
        self._session_token = hashlib.sha256(
            f"{self.username}{datetime.now()}".encode()
        ).hexdigest()
        self._last_active = datetime.now()

    def check_session_valid(self) -> bool:
        """Check if current session is valid (not expired)"""
        if not self._session_token or not self._last_active:
            return False
            
        session_duration = datetime.now() - self._last_active
        return session_duration.total_seconds() < 3600  # 1 hour session

    def logout(self) -> None:
        """End the current session"""
        self._session_token = None
        self._last_active = None

# Usage example:
user = User("john_doe", "john@example.com")
user.set_password("secure123!")

# Login attempt
try:
    if user.check_password("wrong_password"):
        print("Login successful")
    else:
        print("Login failed")
except ValueError as e:
    print(f"Error: {e}")

# Check session
if user.check_session_valid():
    print("Session is active")
else:
    print("Session expired")