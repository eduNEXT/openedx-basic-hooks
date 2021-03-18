"""
Common Django settings for openedx-basic-hooks project.
"""


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open edX platform.
    More info: https://github.com/edx/edx-django-utils/blob/master/edx_django_utils/plugins/README.rst
    """
    settings.TWITTER_CONSUMER_KEY = ""
    settings.TWITTER_CONSUMER_SECRET = ""
    settings.TWITTER_ACCESS_TOKEN = ""
    settings.TWITTER_ACCESS_TOKEN_SECRET = ""
