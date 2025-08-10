# AlpenWeg import:
from alpenwegs.ashared.constants.base_choices import BaseIntegerChoices

# Django translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class SeverityChoices(
    BaseIntegerChoices
):

    # Choices values:
    CRITICAL = 1, _('Critical')
    ERROR = 2, _('Error')
    WARNING = 3, _('Warning')
    INFO = 4, _('Info')
    DEBUG = 5, _('Debug')


class ExclusionInclusionChoices(
    BaseIntegerChoices
):


    # Choices values:
    NONE = 0, _('None')
    EXCLUDE = 1, _('Exclude')
    INCLUDE = 2, _('Include')


class ApplicationChoices(
    BaseIntegerChoices
):

    # Choices values:
    NONE = 0, _('None')
    HTTP_CONNECTION = 1, _('HTTP Connection')
    TASK_RUNNER = 2, _('Task Runner')
    CAPYBARA = 3, _('Capybara')
    TEST = 4, _('Test')
    REPORT = 5, _('Report')
    API_TEST = 6, _('API Test')
    MAILER = 7, _('Mailer')
    API = 8, _('API')
