# Django import:
from django.db.models import IntegerChoices
from django.db.models import TextChoices

# Python import:
import re


# Base integer choices class:
class BaseIntegerChoices(
    IntegerChoices,
):

    @classmethod
    def value_from_int(cls, int_to_search):
        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[0] == int_to_search:
                return choice[1]
        # If not found return False value:
        return False

    @classmethod
    def value_from_str(cls, str_to_search):
        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[1] == str_to_search:
                return choice[0]
        # If not found return False value:
        return False


# Base string choices class:
class BaseStringChoices(
    TextChoices,
):

    @classmethod
    def value_from_str(cls, str_to_search):
        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[0] == str_to_search:
                return choice[1]
        # If not found return False value:
        return False

    @classmethod
    def value_from_int(cls, int_to_search):
        # Iterate thru all chaises:
        for choice in cls.choices:
            if choice[1] == int_to_search:
                return choice[0]
        # If not found return False value:
        return False


class BaseIntegerToDictChoices(BaseIntegerChoices):
    """
    IntegerChoices with metadata lookup support.
    Metadata should be defined as MODULE_METADATA dict
    in the same module as the Enum.
    """

    @classmethod
    def _class_to_metadata_var(cls):
        """
        Convert class name like SportCategoryDifficultyChoices ->
        SPORT_CATEGORY_DIFFICULTY_METADATA
        """

        # 1. Remove the suffix "Choices"
        base = cls.__name__.replace("Choices", "")

        # 2. CamelCase → snake_case
        snake = re.sub(r'(?<!^)(?=[A-Z])', '_', base).lower()

        # 3. snake_case → UPPER_CASE_METADATA
        return snake.upper() + "_METADATA"

    @classmethod
    def _load_metadata(cls):
        """
        Load metadata dict from same module.
        Expected name: {CLASSNAME}_METADATA
        Example: CountryChoices -> COUNTRY_METADATA
        """

        meta_var_name = cls._class_to_metadata_var()
        module = __import__(cls.__module__, fromlist=[meta_var_name])
        return getattr(module, meta_var_name, {})

    @classmethod
    def dict_from_int(cls, int_value):
        label = cls.value_from_int(int_value)
        if label is None:
            return None

        metadata = cls._load_metadata()
        extra = metadata.get(int_value, {})

        return {
            "value": int_value,
            "label": label,
            **extra
        }

    @classmethod
    def as_metadata_list(cls):
        """
        Returns a list of dicts with metadata for ALL choices.
        Example for API responses.
        """
        return [cls.dict_from_int(value) for value, _ in cls.choices]
