# Basic functional test for authentication flow

from services.auth_service import login


def test_invalid_login():
    assert login("", "") is False