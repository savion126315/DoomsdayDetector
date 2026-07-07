import logging


class _Utils:
    """Tiny shim so existing test bodies can keep calling ``utils.get_logger``.

    The legacy ``vhi.utils`` module is gone in the direct-comms package; this
    keeps the call sites working with stdlib logging until they're rewritten.
    """

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("[%(name)s] %(message)s"))
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False
        return logger


utils = _Utils()