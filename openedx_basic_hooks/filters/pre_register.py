from datetime import datetime

from django.utils.translation import ugettext as _

from edx_django_utils.hooks.exceptions import HookException


def check_year_of_birth(data, *args, **kwargs):
    """
    Check if the user year of birth was at least 21 years ago.
    """
    year_of_birth = data["year_of_birth"]
    current_year = datetime.today().year

    try:
        if current_year - int(year_of_birth) < 21:
            raise HookException(
                _("Your year of birth must be {} or before.").format(current_year - 21),
                status_code=400,
            )
    except ValueError:
        raise HookException(
            _("Invalid year of birth."),
            status_code=400,
        )
