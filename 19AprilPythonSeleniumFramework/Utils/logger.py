# utils/logger.py

import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True) 
        handler = logging.FileHandler(f"{log_dir}/test_log.log")

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
