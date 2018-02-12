import logging

import requests
from structlog import wrap_logger

from response_operations_ui import app
from response_operations_ui.exceptions.exceptions import ApiError

logger = wrap_logger(logging.getLogger(__name__))


def get_reporting_unit(ru_ref):
    logger.debug('Retrieving reporting unit', ru_ref=ru_ref)
    url = f'{app.config["BACKSTAGE_API_URL"]}/v1/reporting-unit/{ru_ref}'
    response = requests.get(url)
    if response.status_code != 200:
        raise ApiError(response)

    logger.debug('Successfully retrieved reporting unit', ru_ref=ru_ref)
    return response.json()


def search_reporting_units(query):
    logger.debug('Retrieving reporting units by search query', query=query)
    url = f'{app.config["BACKSTAGE_API_URL"]}/v1/reporting-unit/search'
    response = requests.get(url, params={'query': query})

    if response.status_code != 200:
        raise ApiError(response)

    logger.debug('Successfully retrieved reporting units by search', query=query)

    return response.json()