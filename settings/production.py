from .base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "your_admin_credentials"

INSTALLED_APPS += (
    # other apps for production site
)
