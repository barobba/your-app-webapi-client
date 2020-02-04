
from requests import Response


def prepare_headers():

    return {'Accept': 'application/json'}


def validate_response(response: Response):

    if 200 <= response.status_code < 300:
        pass  # Passes validation
    else:
        raise RuntimeError(response.status_code, response.text)
