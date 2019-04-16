import logging

import jwt
from structlog import wrap_logger

from response_operations_ui.common.uaa import get_uaa_public_key


logger = wrap_logger(logging.getLogger(__name__))


def decode_access_token(access_token):
    """Decodes the access token provided by uaa.  It's important to note that this JWT is
    using RS256 as it's what uaa uses whereas other parts of the application use HS256.
    """
    uaa_public_key = get_uaa_public_key()
    decoded_jwt = jwt.decode(
        access_token,
        key=uaa_public_key,
        algorithms=['RS256'],
        audience='response_operations',
        leeway=10
    )
    return decoded_jwt
