import logging
import sys


def add_action_loglevel(log_actions):
    ACTION = 15 if log_actions else 0
    logging.addLevelName(ACTION, "ACTION")

    def root_action(self, creature, message, *args, **kwargs):
        message = "Creature: {id} - ".format(id=id(creature)) + message
        if self.isEnabledFor(ACTION):
            self._log(ACTION, message, args, **kwargs)

    def logging_action(creature, msg, *args, **kwargs):
        if len(logging.root.handlers) == 0:
            logging.basicConfig()
        logging.root.action(creature, msg, *args, **kwargs)

    logging.Logger.action = root_action
    logging.action = logging_action


def setup_console_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


def setup_file_logging(log_path):
    handler = logging.FileHandler(log_path)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%d-%m-%Y %H:%M:%S")
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)


def setup_logging(log_path, log_actions):
    add_action_loglevel(log_actions)
    logging.root.setLevel(logging.DEBUG)
    setup_console_logging()
    if log_path:
        setup_file_logging(log_path)
