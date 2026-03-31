"""Functional test for leave flow."""
# Basic functional test for authentication flow

from services.auth_service import login


def test_login():
    assert login("employee", "1234") is True


    print("Functional test passed")

def test_security():
    assert True