"""
Filters that can be used with the pre_register filter.
"""

from datetime import datetime

from django.utils.translation import ugettext as _
from openedx_filters.exceptions import (  # pylint: disable=no-name-in-module,import-error
    HookFilterException,
)


def check_year_of_birth(data, *args, **kwargs):  # pylint: disable=unused-argument
    """
    Check if the user year of birth was at least 21 years ago.
    """
    year_of_birth = data["year_of_birth"]
    current_year = datetime.today().year

    try:
        if current_year - int(year_of_birth) < 21:
            raise HookFilterException(
                _("Your year of birth must be {} or before. The filter implemented at a plugins says so.").format(current_year - 21),
                status_code=400,
            )
    except ValueError as err:
        raise HookFilterException(
            _("ValueError when looking at the year_of_birth. Error raised at the plugin."),
            status_code=400,
        ) from err
