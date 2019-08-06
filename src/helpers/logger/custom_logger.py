import logging
import os
from pathlib import Path


class CustomLogger:
    """

        This class overwrite the Class Logging to create a custom log.
    """
    def __init__(self, name_handler, file_name):
        """

        :param string name_handler: Logs handler name.
        :param string file_name: Logs file name.
        """

        self.name_handler = name_handler
        self.logdir = str(Path(__file__).parent.resolve().parent)
        self.file_name = file_name
        self.logger = logging.getLogger(self.name_handler)
        self.set_logger()

    def set_logger(self):
        """

        Function to set all the params for the Class Logging.

        :return: Custom Logger object.
        :rtype: Logger object.
        """

        format_str = '{"date": "%(asctime)s.%(msecs)03d", "name": "%(name)s", "level": "%(levelname)s", '\
                     '"content": %(message)s}'

        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(format_str, date_format)

        file_handler = logging.FileHandler(os.path.join(self.logdir, self.file_name))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

        return self.logger
