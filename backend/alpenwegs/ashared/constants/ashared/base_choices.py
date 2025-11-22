# Django import:
from django.db.models import IntegerChoices
from django.db.models import TextChoices



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


# Base integer to dictionary choices class:
class BaseIntegerToDictChoicesOld(
    BaseIntegerChoices,
):
    """
    Extension of Django's IntegerChoices to support:
      - int <-> str conversions
      - metadata dictionaries via Meta.metadata
    """

    pass

    # # Metadata helpers:
    # @classmethod
    # def dict_from_int(cls, int_to_search):
    #     """
    #     Return metadata dict for an int choice.
    #     If no metadata defined, return label (string).
    #     """

    #     # Check for metadata definition in Meta subclass:
    #     if hasattr(cls, 'Meta') and hasattr(cls.Meta, 'metadata'):
    #         # Return metadata dict from integer if defined:
    #         return cls.Meta.metadata.get(
    #             int_to_search,
    #             {
    #                 'value': int_to_search,
    #                 'label': cls.value_from_int(int_to_search)
    #             },
    #         )

    #     # If not found in metadata, return default structure:
    #     return {
    #         'value': int_to_search,
    #         'label': cls.value_from_int(int_to_search)
    #     }

    # @classmethod
    # def dict_from_str(cls, str_to_search):
    #     """
    #     Return metadata dict for a label (string).
    #     If not found, return False.
    #     """

    #     # Get integer value from string:
    #     int_value = cls.value_from_str(str_to_search)

    #     # If not found, return False.
    #     if not int_value:
    #         return False

    #     # If found, return metadata dict:
    #     return cls.dict_from_int(int_value)

    # # API-friendly export:
    # @classmethod
    # def as_metadata_list(cls):
    #     """
    #     Return all choices as a list of metadata dicts.
    #     Useful for serializers or API responses.
    #     """

    #     # Define result list:
    #     result = []

    #     # Iterate through all choices:
    #     for int_val, str_val in cls.choices:
    #         # Retrieve metadata dict for each choice:
    #         result.append(cls.dict_from_int(int_val))

    #     # Return the result list:
    #     return result


class BaseIntegerToDictChoices(BaseIntegerChoices):
    """
    IntegerChoices with metadata lookup support.
    Metadata should be defined as MODULE_METADATA dict
    in the same module as the Enum.
    """

    @classmethod
    def _load_metadata(cls):
        """
        Load metadata dict from same module.
        Expected name: {CLASSNAME}_METADATA
        Example: CountryChoices -> COUNTRY_METADATA
        """
        meta_var_name = cls.__name__.replace("Choices", "").upper() + "_METADATA"
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
