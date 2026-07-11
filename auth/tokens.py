import secrets


def create_token():

    return secrets.token_hex(32)
