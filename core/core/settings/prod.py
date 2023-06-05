from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "=rdvl%n=pqr6j(@0ki6*&bf&qbv!b0!s6@u+!g@^6=u%(1k4cb"

# Add your site's domain name(s) here.
ALLOWED_HOSTS = ["www.example.com"]

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/4.1/ref/settings/#email-backend
# EMAIL_BACKEND = "django_sendmail_backend.backends.EmailBackend"

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = "My Company Inc. <info@example.com>"

# A list of people who get error notifications.
ADMINS = [
    ("Administrator", "admin@example.com"),
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),  # noqa
        "KEY_PREFIX": "coderedcms",
        "TIMEOUT": 14400,  # in seconds
    }
}
