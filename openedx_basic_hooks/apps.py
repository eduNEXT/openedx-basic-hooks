"""
App configuration for openedx_basic_hooks.
"""

from django.apps import AppConfig


class OpenEdxBasicHooksPluginConfig(AppConfig):
    """
    Open edX Hooks Demo configuration.
    """

    name = "openedx_basic_hooks"
    verbose_name = "Open edX Hooks Demo"

    plugin_app = {
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
        },
        "signals_config": {
            "lms.djangoapp": {
                "relative_path": "receivers",
                "receivers": [
                    {
                        "receiver_func_name": "registration_receiver",
                        "signal_path": "openedx_events.learning.signals.STUDENT_REGISTRATION_COMPLETED",
                    },
                    {
                        "receiver_func_name": "login_receiver",
                        "signal_path": "openedx_events.learning.signals.SESSION_LOGIN_COMPLETED",
                    },
                    {
                        "receiver_func_name": "enrollment_receiver",
                        "signal_path": "openedx_events.learning.signals.COURSE_ENROLLMENT_CREATED",
                    },
                ],
            }
        },
    }
