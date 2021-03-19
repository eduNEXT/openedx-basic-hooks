"""
Actions that can be triggered with the post_register trigger.
"""
from django.utils.translation import ugettext as _

from openedx_basic_hooks.integrations.twitter import publish_in_twitter


def post_enrollment_tweet(
    enrollment, *args, **kwargs
):  # pylint: disable=unused-argument
    """
    Publish a tweet with a welcome the platform to an User on registration.
    """
    msg = _("{user_full_name}, welcome to the {course} course!").format(
        user_full_name=enrollment.user.profile.name,
        course=enrollment.course.display_name,
    )

    publish_in_twitter(msg)
