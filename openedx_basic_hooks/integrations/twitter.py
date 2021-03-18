"""
Module with Twitter integration.
"""

import tweepy
from django.conf import settings


def _get_twitter_api():
    """
    Get twitter api library from the django settings.
    """
    # .. setting_name: TWITTER_CONSUMER_KEY
    # .. setting_default: ''
    # .. setting_description: The consumer key of the Twitter application.
    consumer_key = getattr(settings, "TWITTER_CONSUMER_KEY", "")
    # .. setting_name: TWITTER_CONSUMER_SECRET
    # .. setting_default: ''
    # .. setting_description: The consumer secret of the Twitter application.
    consumer_secret = getattr(settings, "TWITTER_CONSUMER_SECRET", "")
    # .. setting_name: TWITTER_ACCESS_TOKEN
    # .. setting_default: ''
    # .. setting_description: The access token key associated with the
    #  user that will publish the tweets.
    access_token = getattr(settings, "TWITTER_ACCESS_TOKEN", "")
    # .. setting_name: TWITTER_ACCESS_TOKEN_SECRET
    # .. setting_default: ''
    # .. setting_description: The access token secret associated with
    #  the user that will publish the tweets.
    access_token_secret = getattr(settings, "TWITTER_ACCESS_TOKEN_SECRET", "")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def publish_in_twitter(msg):
    """
    Publish a given message in twitter.
    """
    api = _get_twitter_api()
    api.update_status(msg)
