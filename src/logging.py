import os
import sys
import logging

def setup_logging():
    """Configures the root logger for the application"""

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, 'app.log')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Handler for the console
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(stdout_handler)

    # Handler for the 'logs/app.log' file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)

    logging.info("Logging configured successfully.")