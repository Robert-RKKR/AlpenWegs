def retag_auth_endpoints(result, generator, request, public):
    """
    Retag all /api/auth/* endpoints in the schema so they appear under
    'Profiles - Authentication and Verification' in Swagger/Redoc.
    """
    for path, path_item in result["paths"].items():
        if path.startswith("/api/auth/"):
            for method, operation in path_item.items():
                operation["tags"] = ["Profiles - Authentication and Verification"]
    return result
