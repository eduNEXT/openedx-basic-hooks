"""
Filters that can be used with the pre_register filter.
"""
from openedx_filters.learning.enrollment import PreEnrollmentFilter


def avoid_enrollment(course_key, user, mode, **kwargs):
    "Method that raises exception used to avoid enrollments."
    raise PreEnrollmentFilter.PreventEnrollment
