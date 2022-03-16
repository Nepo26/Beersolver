from logging import basicConfig,getLogger, INFO

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)


def log_general(msg: str, level: int = INFO) -> None:
    """
    Wrapper for logging.
    :param msg: message to be issued
    :param level: what level it is being issued to
    """
    logger.log(level, msg)
