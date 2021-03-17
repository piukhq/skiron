import typing as t
import os

import sentry_sdk
from sentry_sdk.integrations.falcon import FalconIntegration


class ConfigVarRequiredError(Exception):
    pass


def getenv(key: str, default: str = None, conv: t.Callable = str, required: bool = True) -> t.Any:
    """If `default` is None, then the var is non-optional."""
    var = os.getenv(key, default)
    if var is None and required is True:
        raise ConfigVarRequiredError(f"Configuration variable '{key}' is required but was not provided.")
    elif var is not None:
        return conv(var)
    else:
        return None


# Connection details for RabbitMQ.
RABBITMQ_USER = getenv("RABBITMQ_USER")
RABBITMQ_PASS = getenv("RABBITMQ_PASS")
RABBITMQ_HOST = getenv("RABBITMQ_HOST")
RABBITMQ_PORT = getenv("RABBITMQ_PORT", conv=int)
RABBITMQ_DSN = getenv("AMQP_DSN", f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//")


# Sentry project data source name.
# https://docs.sentry.io/quickstart/#about-the-dsn
SENTRY_DSN = getenv("TXM_SENTRY_DSN", required=False)

# Environment identifier to file issues under in Sentry.
SENTRY_ENV = getenv("TXM_SENTRY_ENV", default="unset").lower()

if SENTRY_DSN is not None:
    sentry_sdk.init(dsn=SENTRY_DSN, environment=SENTRY_ENV, integrations=[FalconIntegration()])


# API key for service authentication.
SERVICE_API_KEY = "F616CE5C88744DD52DB628FAD8B3D"
