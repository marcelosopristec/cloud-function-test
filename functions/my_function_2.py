import os

def hello_world_2(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`.
    """

    print("Value", os.getenv("TOKEN_1", ""))

    return "Hello, World! (2)"