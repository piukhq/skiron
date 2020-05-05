import typing as t
import contextlib

import kombu.simple

import settings


@contextlib.contextmanager
def mastercard_auth() -> t.Generator[kombu.simple.SimpleQueue, None, None]:
    with kombu.Connection(settings.RABBITMQ_DSN, connect_timeout=3) as conn:
        conn.ensure_connection(timeout=5)
        with conn.SimpleQueue("mastercard-auth") as queue:
            yield queue
