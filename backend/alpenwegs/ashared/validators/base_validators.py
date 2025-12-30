# Django import:
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.template import TemplateSyntaxError
from django.template import Template

# Python import:
import re


# Name validator:
@deconstructible
class NameValueValidator(RegexValidator):
    """
    Validate if specified value is a valid name field.
    """

    regex = r"^[0-9A-Za-z_-’.]{3,128}$"
    message = _('The object name must contain 3 to 128 digits, '\
        'letters and special characters -, _, . or spaces.')
    flags = 0


# Description validator:
@deconstructible
class SnippetValueValidator(RegexValidator):
    """
    Validate if specified value is a valid snippet field.
    """

    regex = r"^[0-9A-Za-z_-’.]{8,512}$"
    message = _('Snippet must contain 8 to 512 digits, letters '\
        'and special characters -, _, . or spaces.')
    flags = 0


# Code validator:
@deconstructible
class CodeValueValidator(RegexValidator):
    """
    Validate if specified value is a valid code field.
    """

    regex = r'^[A-Z,a-z]{2,8}$'
    message = _('The object code must contain 2 to 8 letters.')
    flags = 0


@deconstructible
class StandardUrlValidator(RegexValidator):
    """
    Validate if the given value is a standard URL (without the HTTP/S, host, and 
    without any query parameters).
    """

    regex = r'^[.a-zA-Z0-9_\/]+\/?$'
    message = _('Provide a valid URL without HTTP/S, host, or query parameters.')
    flags = 0


@deconstructible
class DynamicUrlValidator(RegexValidator):
    """
    Validate if the given value is a URL with at least one template variable
    {{variable}} where variable is a string without special characters.
    """

    regex = r'^[.a-zA-Z0-9_\/]*\{\{[a-zA-Z_][a-zA-Z0-9_]+\}\}[a-zA-Z0-9_\/]*\/?$'
    message = _('Provide a valid URL containing at least one template '
                'variable like {{value}}, with standard python '
                'characters for the variable name.')
    flags = 0


@deconstructible
class StandardCommandValidator(RegexValidator):
    """
    Validate if the given value is a standard command.
    Assumes standard CLI commands are alphanumeric with optional underscores 
    or slashes.
    """

    regex = r'^[a-zA-Z0-9_\/\s]+$'
    message = _('Provide a valid standard CLI command.')
    flags = 0


@deconstructible
class DynamicCommandValidator(RegexValidator):
    """
    Validate if the given value is a command containing at least one template 
    variable {{variable}} where variable is a string without special characters.
    """

    regex = r'^[a-zA-Z0-9_\/\s]*\{\{[a-zA-Z_][a-zA-Z0-9_]+\}\}[a-zA-Z0-9_\/\s]*$'
    message = _('Provide a valid CLI command containing at least one template '
                'variable like {{value}}, with no special characters '
                'in the variable name.')
    flags = 0

# Regex validator:
def regex_validator(value):
    """
    Validate if specified value is a valid regex expression.
    """

    pattern = rf'{value}'
    try: # Try to compile given value to regex:
        re.compile(pattern)
    except Exception as exception:
        raise ValidationError(
            _(f'Regex validation error: {exception}'))

def html_template_validator(value):
    try: # Create a Template object from the rendered template string:
        Template(value)
    except TemplateSyntaxError:
        raise ValidationError('Invalid template syntax in HTML template.')
