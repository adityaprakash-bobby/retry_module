import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def retry(exception, max_retries=5, delay=0):
    """
    Decorator which retries a function in case of an exception.

    When a max_retries is not specified, the function is retried a maximum 5
    times, after which the exception is re-raised.

    When a delay is not specified a default delay of 0.5 seconds is used for
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

            if max_retries == 0:
                return fn(*args, **kwargs)
            elif max_retries < 0:
                raise ValueError('max_retries must be >= 0')

            while _tries < max_retries:
                _tries += 1
                try:
                    return fn(*args, **kwargs)
                except exception as e:
                    if _tries == max_retries:
                        logger.info(
                            "{} still has some exception as {}. Stopping retry.".
                            format(fn.__name__, str(e))
                        )
                        raise

                    logger.warning(
                        "{} has some exception as {}. Retrying in {} seconds.".
                        format(fn.__name__, str(e), _sleep_time)
                    )

                time.sleep(_sleep_time)
                _sleep_time = (_tries + 1) * delay

        return retry_wrapper
    return retry_function
