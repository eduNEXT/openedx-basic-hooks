"""
Actions that can be triggered with the post_register trigger.
"""
from django.utils.translation import ugettext as _

from openedx_basic_hooks.integrations.twitter import publish_in_twitter


def post_register_tweet(
    user, registration, *args, **kwargs
):  # pylint: disable=unused-argument
    """
    Publish a tweet with a welcome the platform to an User on registration.
    """
    msg = _("{user_full_name}, welcome to the platform!").format(
        user_full_name=user.profile.name
    )

    publish_in_twitter(msg)
