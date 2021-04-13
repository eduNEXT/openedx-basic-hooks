"""
Receivers for the openedx-events signals.
"""

from openedx_basic_hooks.actions.post_register import post_register_tweet


def registration_receiver(user, registration, *args, **kwargs):
    """
    Registration receiver.
    """
    post_register_tweet(user, registration, *args, **kwargs)
