def retag_auth_endpoints(
        result,
        generator,
        request,
        public,
    ):
    """
    Retag all authentication endpoints in the schema so they appear under
    'Profiles - Authentication and Verification' in Swagger/Redoc.
    """

    # Iterating over all Swagger paths:
    for path, path_item in result['paths'].items():
        # Checking if the path is an authentication endpoint:
        if path.startswith('/api/auth/'):
            # Iterating over all HTTP methods for the path:
            for method, operation in path_item.items():
                # Apply the tag to each of the operation:
                operation['tags'] = ['Profiles - Authentication and Verification']

    # Return the modified result:
    return result
