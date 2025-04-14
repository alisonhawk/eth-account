"""Mock getpass module for testing."""

class MockGetPass:
    """A mock getpass that returns predefined passwords for testing."""
    
    def __init__(self, test_password="test_password"):
        self.test_password = test_password

    def getpass(self, prompt=None):
        """Return the test password regardless of prompt."""
        return self.test_password

# Default instance with default test password
mock_getpass = MockGetPass()

def patch_getpass(test_password="test_password"):
    """Create a new mock getpass instance with specified password."""
    return MockGetPass(test_password) 