# AlpenWeg import:
from alpenwegs.ashared.constants.ashared.base_choices import BaseIntegerToDictChoices


# Choices class:
class SeverityChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    CRITICAL = 1, 'Critical'
    ERROR = 2, 'Error'
    WARNING = 3, 'Warning'
    INFO = 4, 'Info'
    DEBUG = 5, 'Debug'

# Module-level metadata dictionary:
SEVERITY_TYPE_METADATA = {
    1: {
        'icon': '🟥',
        'description': 'A critical issue requiring immediate attention.',
        'depend': None,
    },
    2: {
        'icon': '🔴',
        'description': 'An error that caused an operation to fail.',
        'depend': None,
    },
    3: {
        'icon': '🟡',
        'description': 'A warning indicating a potential problem.',
        'depend': None,
    },
    4: {
        'icon': '🔵',
        'description': 'Informational message about normal operations.',
        'depend': None,
    },
    5: {
        'icon': '⚪️',
        'description': 'Debug-level details for diagnostics.',
        'depend': None,
    },
}


class ExclusionInclusionChoices(
    BaseIntegerToDictChoices,
):

    # Choices values:
    NONE = 0, 'None'
    EXCLUDE = 1, 'Exclude'
    INCLUDE = 2, 'Include'

# Module-level metadata dictionary:
EXCLUSION_INCLUSION_METADATA = {
    0: {
        'icon': '⚪️',
        'description': 'No inclusion or exclusion specified.',
        'depend': None,
    },
    1: {
        'icon': '⛔',
        'description': 'Item is excluded from processing.',
        'depend': None,
    },
    2: {
        'icon': '✔️',
        'description': 'Item is included for processing.',
        'depend': None,
    },
}


class ApplicationChoices(
    BaseIntegerToDictChoices,
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

# Module-level metadata dictionary:
APPLICATION_TYPE_METADATA = {
    0: {
        'icon': '⚪️',
        'description': 'No application specified.',
        'depend': None,
    },
    1: {
        'icon': '🌐',
        'description': 'HTTP connection logic and communication layer.',
        'depend': None,
    },
    2: {
        'icon': '⚙️',
        'description': 'Task runner responsible for executing scheduled or async tasks.',
        'depend': None,
    },
    3: {
        'icon': '🦫',
        'description': 'Capybara automation framework and related tooling.',
        'depend': None,
    },
    4: {
        'icon': '🧪',
        'description': 'Testing environment or test execution.',
        'depend': None,
    },
    5: {
        'icon': '📊',
        'description': 'Reporting engine for generating structured reports.',
        'depend': None,
    },
    6: {
        'icon': '🔍',
        'description': 'API testing utilities or inspection tools.',
        'depend': None,
    },
    7: {
        'icon': '📧',
        'description': 'Mailer application handling email sending and templates.',
        'depend': None,
    },
    8: {
        'icon': '🛠️',
        'description': 'General API processing or utility functions.',
        'depend': None,
    },
}
