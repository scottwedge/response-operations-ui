import os
from distutils.util import strtobool

FDI_LIST = {'AOFDI', 'AIFDI', 'QIFDI', 'QOFDI'}


class Config(object):

    DEBUG = os.getenv('DEBUG', False)
    TESTING = False
    PORT = os.getenv('PORT', 8085)
    GOOGLE_TAG_MANAGER = os.getenv('GOOGLE_TAG_MANAGER', None)
    GOOGLE_TAG_MANAGER_PROP = os.getenv('GOOGLE_TAG_MANAGER_PROP', None)
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
    RESPONSE_OPERATIONS_UI_SECRET = os.getenv('RESPONSE_OPERATIONS_UI_SECRET', "secret")
    SESSION_TYPE = "redis"
    PERMANENT_SESSION_LIFETIME = os.getenv('PERMANENT_SESSION_LIFETIME', 43200)
    REDIS_SERVICE = os.getenv('REDIS_SERVICE')
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_DB = os.getenv('REDIS_DB', 0)
    SECURE_COOKIES = strtobool(os.getenv('SECURE_COOKIES', 'True'))
    USE_SESSION_FOR_NEXT = True

    SECURITY_USER_NAME = os.getenv('SECURITY_USER_NAME')
    SECURITY_USER_PASSWORD = os.getenv('SECURITY_USER_PASSWORD')

    RESPONSE_OPERATIONS_UI_HOST = os.getenv('RESPONSE_OPERATIONS_UI_HOST', "http://localhost")
    RESPONSE_OPERATIONS_UI_PORT = os.getenv('RESPONSE_OPERATIONS_UI_PORT', "8085")
    RESPONSE_OPERATIONS_UI_URL = os.getenv('RESPONSE_OPERATIONS_UI_URL', f'{RESPONSE_OPERATIONS_UI_HOST}:{RESPONSE_OPERATIONS_UI_PORT}')

    # Zipkin
    ZIPKIN_DISABLE = bool(strtobool(os.getenv("ZIPKIN_DISABLE", "False")))
    ZIPKIN_DSN = os.getenv("ZIPKIN_DSN", None)
    ZIPKIN_SAMPLE_RATE = int(os.getenv("ZIPKIN_SAMPLE_RATE", 0))

    # Service Configs
    CASE_URL = os.getenv('CASE_URL')
    CASE_USERNAME = os.getenv('CASE_USERNAME')
    CASE_PASSWORD = os.getenv('CASE_PASSWORD')
    CASE_AUTH = (CASE_USERNAME, CASE_PASSWORD)
    MAX_CASES_RETRIEVED_PER_SURVEY = os.getenv('MAX_CASES_RETRIEVED_PER_SURVEY', 12)

    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL')
    COLLECTION_EXERCISE_USERNAME = os.getenv('COLLECTION_EXERCISE_USERNAME')
    COLLECTION_EXERCISE_PASSWORD = os.getenv('COLLECTION_EXERCISE_PASSWORD')
    COLLECTION_EXERCISE_AUTH = (COLLECTION_EXERCISE_USERNAME, COLLECTION_EXERCISE_PASSWORD)

    COLLECTION_INSTRUMENT_URL = os.getenv('COLLECTION_INSTRUMENT_URL')
    COLLECTION_INSTRUMENT_USERNAME = os.getenv('COLLECTION_INSTRUMENT_USERNAME')
    COLLECTION_INSTRUMENT_PASSWORD = os.getenv('COLLECTION_INSTRUMENT_PASSWORD')
    COLLECTION_INSTRUMENT_AUTH = (COLLECTION_INSTRUMENT_USERNAME, COLLECTION_INSTRUMENT_PASSWORD)

    IAC_URL = os.getenv('IAC_URL')
    IAC_USERNAME = os.getenv('IAC_USERNAME')
    IAC_PASSWORD = os.getenv('IAC_PASSWORD')
    IAC_AUTH = (IAC_USERNAME, IAC_PASSWORD)

    SECURE_MESSAGE_URL = os.getenv('SECURE_MESSAGE_URL')
    SECURE_MESSAGE_JWT_SECRET = os.getenv('SECURE_MESSAGE_JWT_SECRET')

    PARTY_URL = os.getenv('PARTY_URL')
    PARTY_USERNAME = os.getenv('PARTY_USERNAME')
    PARTY_PASSWORD = os.getenv('PARTY_PASSWORD')
    PARTY_AUTH = (PARTY_USERNAME, PARTY_PASSWORD)
    PARTY_RESPONDENTS_PER_PAGE = os.getenv('PARTY_RESPONDENTS_PER_PAGE', 25)
    PARTY_BUSINESS_RESULTS_PER_PAGE = os.getenv('PARTY_BUSINESS_RESULTS_PER_PAGE', 25)

    NOTIFY_SERVICE_URL = os.getenv('NOTIFY_SERVICE_URL', 'http://notify-gateway-service/emails/')
    NOTIFY_REQUEST_PASSWORD_CHANGE_TEMPLATE = os.getenv('NOTIFY_REQUEST_PASSWORD_CHANGE_TEMPLATE',
                                                            'request_password_change_id')
    NOTIFY_CONFIRM_PASSWORD_CHANGE_TEMPLATE = os.getenv('NOTIFY_CONFIRM_PASSWORD_CHANGE_TEMPLATE',
                                                            'confirm_password_change_id')
    NOTIFY_REQUEST_CREATE_ACCOUNT_TEMPLATE = os.getenv('NOTIFY_REQUEST_CREATE_ACCOUNT_TEMPLATE',
                                                            'request_create_account_id')
    NOTIFY_CONFIRM_CREATE_ACCOUNT_TEMPLATE = os.getenv('NOTIFY_CONFIRM_CREATE_ACCOUNT_TEMPLATE',
                                                            'confirm_create_account_id')
    SEND_EMAIL_TO_GOV_NOTIFY = os.getenv('SEND_EMAIL_TO_GOV_NOTIFY', False)

    REPORT_URL = os.getenv('REPORT_URL')

    SAMPLE_URL = os.getenv('SAMPLE_URL')
    SAMPLE_USERNAME = os.getenv('SAMPLE_USERNAME')
    SAMPLE_PASSWORD = os.getenv('SAMPLE_PASSWORD')
    SAMPLE_AUTH = (SAMPLE_USERNAME, SAMPLE_PASSWORD)

    SURVEY_URL = os.getenv('SURVEY_URL')
    SURVEY_USERNAME = os.getenv('SURVEY_USERNAME')
    SURVEY_PASSWORD = os.getenv('SURVEY_PASSWORD')
    SURVEY_AUTH = (SURVEY_USERNAME, SURVEY_PASSWORD)

    UAA_SERVICE_URL = os.getenv('UAA_SERVICE_URL')
    UAA_CLIENT_ID = os.getenv('UAA_CLIENT_ID')
    UAA_CLIENT_SECRET = os.getenv('UAA_CLIENT_SECRET')

    EMAIL_TOKEN_SALT = os.getenv('EMAIL_TOKEN_SALT', 'aardvark')
    # 24 hours in seconds
    EMAIL_TOKEN_EXPIRY = int(os.getenv('EMAIL_TOKEN_EXPIRY', '86400'))
    # 72 hours in seconds
    CREATE_ACCOUNT_EMAIL_TOKEN_EXPIRY = int(os.getenv('CREATE_ACCOUNT_EMAIL_TOKEN_EXPIRY', '259200'))
    CREATE_ACCOUNT_ADMIN_PASSWORD = os.getenv('CREATE_ACCOUNT_ADMIN_PASSWORD')



class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', True)
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
    REDIS_HOST = os.getenv('REDIS_HOST', "localhost")
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DB = os.getenv('REDIS_DB', 0)
    SECURE_COOKIES = strtobool(os.getenv('SECURE_COOKIES', 'False'))

    # Service Config
    CASE_URL = os.getenv('CASE_URL', 'http://localhost:8171')
    CASE_USERNAME = os.getenv('CASE_USERNAME', 'admin')
    CASE_PASSWORD = os.getenv('CASE_PASSWORD', 'secret')
    CASE_AUTH = (CASE_USERNAME, CASE_PASSWORD)

    COLLECTION_EXERCISE_URL = os.getenv('COLLECTION_EXERCISE_URL', 'http://localhost:8145')
    COLLECTION_EXERCISE_USERNAME = os.getenv('COLLECTION_EXERCISE_USERNAME', 'admin')
    COLLECTION_EXERCISE_PASSWORD = os.getenv('COLLECTION_EXERCISE_PASSWORD', 'secret')
    COLLECTION_EXERCISE_AUTH = (COLLECTION_EXERCISE_USERNAME, COLLECTION_EXERCISE_PASSWORD)

    COLLECTION_INSTRUMENT_URL = os.getenv('COLLECTION_INSTRUMENT_URL', 'http://localhost:8002')
    COLLECTION_INSTRUMENT_USERNAME = os.getenv('COLLECTION_INSTRUMENT_USERNAME', 'admin')
    COLLECTION_INSTRUMENT_PASSWORD = os.getenv('COLLECTION_INSTRUMENT_PASSWORD', 'secret')
    COLLECTION_INSTRUMENT_AUTH = (COLLECTION_INSTRUMENT_USERNAME, COLLECTION_INSTRUMENT_PASSWORD)

    IAC_URL = os.getenv('IAC_URL', 'http://localhost:8121')
    IAC_USERNAME = os.getenv('IAC_USERNAME', 'admin')
    IAC_PASSWORD = os.getenv('IAC_PASSWORD', 'secret')
    IAC_AUTH = (IAC_USERNAME, IAC_PASSWORD)

    SECURE_MESSAGE_URL = os.getenv('SECURE_MESSAGE_URL', 'http://localhost:5050')
    SECURE_MESSAGE_JWT_SECRET = os.getenv('SECURE_MESSAGE_JWT_SECRET', 'testsecret')

    REPORT_URL = os.getenv('REPORT_URL', 'http://localhost:8084')

    PARTY_URL = os.getenv('PARTY_URL', 'http://localhost:8081')
    PARTY_USERNAME = os.getenv('PARTY_USERNAME', 'admin')
    PARTY_PASSWORD = os.getenv('PARTY_PASSWORD', 'secret')
    PARTY_AUTH = (PARTY_USERNAME, PARTY_PASSWORD)

    SAMPLE_URL = os.getenv('SAMPLE_URL', 'http://localhost:8125')
    SAMPLE_USERNAME = os.getenv('SAMPLE_USERNAME', 'admin')
    SAMPLE_PASSWORD = os.getenv('SAMPLE_PASSWORD', 'secret')
    SAMPLE_AUTH = (SAMPLE_USERNAME, SAMPLE_PASSWORD)

    SURVEY_URL = os.getenv('SURVEY_URL', 'http://localhost:8080')
    SURVEY_USERNAME = os.getenv('SURVEY_USERNAME', 'admin')
    SURVEY_PASSWORD = os.getenv('SURVEY_PASSWORD', 'secret')
    SURVEY_AUTH = (SURVEY_USERNAME, SURVEY_PASSWORD)

    UAA_SERVICE_URL = os.getenv('UAA_SERVICE_URL', 'http://localhost:9080')
    UAA_CLIENT_ID = os.getenv('UAA_CLIENT_ID', 'response_operations')
    UAA_CLIENT_SECRET = os.getenv('UAA_CLIENT_SECRET', 'password')

    EMAIL_TOKEN_SALT = os.getenv('EMAIL_TOKEN_SALT', 'aardvark')
    # 24 hours in seconds
    EMAIL_TOKEN_EXPIRY = int(os.getenv('EMAIL_TOKEN_EXPIRY', '86400'))
    # 72 hours in seconds
    CREATE_ACCOUNT_EMAIL_TOKEN_EXPIRY = int(os.getenv('CREATE_ACCOUNT_EMAIL_TOKEN_EXPIRY', '259200'))
    CREATE_ACCOUNT_ADMIN_PASSWORD = os.getenv('CREATE_ACCOUNT_ADMIN_PASSWORD', 'secret')


class TestingConfig(DevelopmentConfig):
    """Configuration used for testing.  The uaa public and private keys in this block are used ONLY for
    the unit tests when testing the jwt and aren't used at all for anything else.
    """
    DEBUG = False
    TESTING = True
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SEND_EMAIL_TO_GOV_NOTIFY = True
    UAA_PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MFswDQYJKoZIhvcNAQEBBQADSgAwRwJAeeLysb2I2n86Ya+W3vqCxUM1j5sRdlFN
U9yf2b38ppt3rf2xHJYTfjSvezXOMEJusFbhH9LeH4V8kr4k4ZmdewIDAQAB
-----END PUBLIC KEY-----'''
    UAA_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIBOQIBAAJAeeLysb2I2n86Ya+W3vqCxUM1j5sRdlFNU9yf2b38ppt3rf2xHJYT
fjSvezXOMEJusFbhH9LeH4V8kr4k4ZmdewIDAQABAkBmg8QeTEybgWDIIpghaM+u
PC4DX6hbPFxuiWSFDe8+7N/dWO6xV3zDjzM6L8lXb5J2woEZ0JUVeS/BQB1xykOh
AiEAvdS9ocmimlGUTHaH+t0N92ZJBuGc5RdrQjdVMc5bZ0sCIQCkX0qHKjzxBC8S
IYBrirWvgd/bEXbV/81BprpF6p7UkQIhAJ0mNu5urAuwqWI7ZgrJYTyEEsR9lZMZ
thOVFxQqTwTNAiAFBhCODwFr0Ffr8vAs2UFySsLfvCnoonfQgNsClggisQIgIGEJ
Z5VVFymXN2n+A6UeWAnuO8/E1inhk99dBzKEGdw=
-----END RSA PRIVATE KEY-----'''
    SECRET_KEY = 'sekrit!'
    SECURITY_USER_NAME = 'admin'
    SECURITY_USER_PASSWORD = 'secret'
    CREATE_ACCOUNT_ADMIN_PASSWORD = 'secret'
