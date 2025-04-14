"""Tests for password handling in Account class."""

import pytest
from unittest.mock import patch

from eth_account import Account
from eth_keys import keys
from hexbytes import HexBytes

EXPECTED_ADDRESS = '5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

def test_basic_account_encrypt():
    """Test basic Account.encrypt functionality with direct password."""
    test_key = 0xb25c7db31feed9122727bf0939dc769a96564b2de4c4726d035b36ecf1e5b364
    test_password = "test_password"
    
    # Test direct password usage (as in doctests)
    encrypted = Account.encrypt(test_key, test_password)
    assert encrypted['address'] == EXPECTED_ADDRESS
    
    # Verify we can decrypt it back
    decrypted_key = Account.decrypt(encrypted, test_password)
    assert decrypted_key.hex() == hex(test_key)[2:]

def test_account_encrypt_with_getpass():
    """Test Account.encrypt with mocked getpass."""
    test_key = 0xb25c7db31feed9122727bf0939dc769a96564b2de4c4726d035b36ecf1e5b364
    test_password = "test_password"
    
    # Mock getpass to return our test password
    with patch('getpass.getpass', return_value=test_password):
        encrypted = Account.encrypt(test_key, test_password)
        assert encrypted['address'] == EXPECTED_ADDRESS
        
        # Verify we can decrypt it back
        decrypted_key = Account.decrypt(encrypted, test_password)
        assert decrypted_key.hex() == hex(test_key)[2:]

def test_account_encrypt_with_mock_getpass():
    """Test Account.encrypt with mocked getpass."""
    test_key = "0xb25c7db31feed9122727bf0939dc769a96564b2de4c4726d035b36ecf1e5b364"
    test_password = "test_password"
    
    # Mock getpass to return our test password
    mock_getpass = lambda prompt: test_password
    with patch('getpass.getpass', mock_getpass):
        encrypted = Account.encrypt(test_key, test_password)
        assert encrypted['address'] == EXPECTED_ADDRESS
        
        # Verify we can decrypt it back
        decrypted_key = Account.decrypt(encrypted, test_password)
        assert decrypted_key.hex() == test_key.replace('0x', '')

def test_account_encrypt_with_direct_password():
    """Test Account.encrypt with direct password (for doctests)."""
    test_key = "0xb25c7db31feed9122727bf0939dc769a96564b2de4c4726d035b36ecf1e5b364"
    test_password = "test_password"
    
    # Test direct password usage (as in doctests)
    encrypted = Account.encrypt(test_key, test_password)
    assert encrypted['address'] == EXPECTED_ADDRESS
    
    # Verify we can decrypt it back
    decrypted_key = Account.decrypt(encrypted, test_password)
    assert decrypted_key.hex() == test_key.replace('0x', '') 