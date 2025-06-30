"""
This module mocks an interaction with an OAuth2 Authorization Server.
You should not need to change anything in this module,
but if you do please note it in the README
"""

import werkzeug


def get_auth_token(request):
    auth_header = request.headers.get('authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        #return redirect('/') 
        raise werkzeug.exceptions.Unauthorized(f"Missing or invalid Access Token, {auth_header}")
       
    access_token = auth_header[len("Bearer ") :]
    token_info = introspect_token(access_token)
    user_info = token_info["user_info"]
    username = user_info["username"]
    return [token_info, user_info, username]

def introspect_token(access_token):
    """
    Uses hard-coded tokens to map to hard-coded user information
    """
    token_mapping = {
        "31cd894de101a0e31ec4aa46503e59c8": {
            "token_is_valid": True,
            "user_info": {
                "user_id": "8bde3e84-a964-479c-9c7b-4d7991717a1b",
                "username": "challengeuser1",
            },
        },
        "97778661dab9584190ecec11bf77593e": {
            "token_is_valid": True,
            "user_info": {
                "user_id": "45e3c49a-c699-405b-a8b2-f5407bb1a133",
                "username": "challengeuser2",
            },
        },
    }

    invalid_response = {"token_is_valid": False, "user_info": None}

    return token_mapping.get(access_token, invalid_response)
