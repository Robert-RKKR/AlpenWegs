def dict_to_filter_params(
    dictionary: dict,
    prefix: str = '',
) -> dict:
    """
    Translate a dictionary of attributes to a nested set of parameters
    suitable for QuerySet filtering.
    
    Args:
        dictionary (dict):
            The dictionary of attributes.
        prefix (str):
            The prefix to prepend to each parameter key (default: '').

    Returns (dict):
        The nested set of parameters suitable for QuerySet filtering.
    """

    # Initialize the filter parameters:
    params = {}

    # Iterate over the dictionary items:
    for key, val in dictionary.items():
        k = prefix + key
        if isinstance(val, dict):
            params.update(dict_to_filter_params(val, k + '__'))
        else:
            params[k] = val

    # Return the constructed filter parameters:
    return params
