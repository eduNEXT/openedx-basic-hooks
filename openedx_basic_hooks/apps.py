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
                        "signal_path": "openedx_events.auth.signals.v1.REGISTER_USER",
                    },
                ],
            }
        },
    }
