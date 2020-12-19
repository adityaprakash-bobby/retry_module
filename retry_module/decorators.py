import sys
import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def retry(exception, max_retires=5, delay=0.5):
    """
    Decorator which retries a function in case of an exception.

    When a max_retries is not mention, the function is retiried maximum 5
    times, after which the exception is re-raised.

    When a delay is not mentioned a default delay of 0.5 seconds is used for
    times between the next retry. Delay between each execution is delay times
    the retry number.

    Parameters
    ----------
    exception :
        The exception upon which the function needs to be retried.

    max_retries : int, optional
        The number of times a function is to be retried before re-raising the
        exception.

    delay : float, optional
        The time delay for first retry in case of an exception. Internally the
        delay between each retry is delay times the retry number.

    """

    def retry_function(fn):
        @wraps(fn)
        def retry_wrapper(*args, **kwargs):
            _tries = 0
            _sleep_time = delay

            while _tries < max_retires:
                _tries += 1
                try:
                    return fn(*args, **kwargs)
                except exception as e:
                    if _tries == max_retires:
                        logger.info(
                            f"{fn.__name__} still has some exception as {str(e)}. Stopping retry."
                        )
                        raise

                    logger.warning(
                        f"{fn.__name__} has some exception as {str(e)}. Retrying in {_sleep_time} seconds."
                    )

                time.sleep(_sleep_time)
                _sleep_time = (_tries + 1) * delay

        return retry_wrapper

    return retry_function
