import pytest

from hw_tracker.email_alert import email_send


def test_email_send():
    email_send("test", "test", "tannedstone@gmail.com")
