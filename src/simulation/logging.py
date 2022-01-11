import logging
import sys


def setup_console_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


def setup_file_logging(log_path):
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%d-%m-%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


def setup_logging(log_path):
    logging.root.setLevel(logging.DEBUG)
    setup_console_logging()
    if log_path:
        setup_file_logging(log_path)