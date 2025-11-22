# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerChoices


# Choices class:
class SeverityChoices(
    BaseIntegerChoices,
):

    # Choices values:
    CRITICAL = 1, 'Critical'
    ERROR = 2, 'Error'
    WARNING = 3, 'Warning'
    INFO = 4, 'Info'
    DEBUG = 5, 'Debug'


class ExclusionInclusionChoices(
    BaseIntegerChoices,
):

    # Choices values:
    NONE = 0, 'None'
    EXCLUDE = 1, 'Exclude'
    INCLUDE = 2, 'Include'


class ApplicationChoices(
    BaseIntegerChoices,
):

    # Choices values:
    NONE = 0, 'None'
    HTTP_CONNECTION = 1, 'HTTP Connection'
    TASK_RUNNER = 2, 'Task Runner'
    CAPYBARA = 3, 'Capybara'
    TEST = 4, 'Test'
    REPORT = 5, 'Report'
    API_TEST = 6, 'API Test'
    MAILER = 7, 'Mailer'
    API = 8, 'API'
