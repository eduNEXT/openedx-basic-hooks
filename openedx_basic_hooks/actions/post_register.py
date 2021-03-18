from openedx_basic_hooks.integrations.twitter import publish_in_twitter
from django.utils.translation import ugettext as _


def post_register_tweet(user, registration, *args, **kwargs):
    """
    Publish a tweet with a welcome the platform to an User on registration.
    """
    msg = _("{user_full_name}, welcome to the platform!").format(
        user_full_name=user.profile.name
    )

    publish_in_twitter(msg)
