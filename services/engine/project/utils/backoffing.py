import backoff
import requests


def retry_timeout():
    return backoff.on_exception(
        wait_gen=backoff.expo,
        exception=(
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.exceptions.RequestException
        ),
        max_tries=10,
    )
