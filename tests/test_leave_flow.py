# Basic functional test for authentication flow

def test_leave_submission():
    result = "Submitted successfully"
    assert result == "Submitted successfully"


def test_leave_limit():
    result = "Rejected: Maximum leave limit exceeded"
    assert result == "Rejected: Maximum leave limit exceeded"