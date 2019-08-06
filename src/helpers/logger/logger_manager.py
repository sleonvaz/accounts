import json
import sys
from cerberus import Validator
from helpers.logger.custom_logger import CustomLogger


class LoggerManager(object):

    def __init__(self, logname, logevent, schema=None, session=None):
        """
        :param logname: Logs handler name.
        :type logname: str.
        :param logevent: Logs file name.
        :type logevent: str.
        :param schema: Data schema to validate with. Default value is None.
        :type schema: dict.
        :param session: Dictionary with the data session. Default value is None.
        :type session: Dict.
        :raise IOError: Error handeling the file.
        """
        if session is not None:

            self.ip = session["ip"]
            self.request_uuid = session["request_uuid"]
        else:

            self.ip = None
            self.request_uuid = None
        self.schema = schema
        self.log_event = logevent
        self.log = CustomLogger(logevent, logname)

    def _add_session(self, data):
        """

        Function to add data sessions to  data dictionary.

        :param data: Data dictionary to write on logger
        :type data: dict
        :return: Dictionary result of the join
        :rtype: Dict
        """
        session = {
            "ip": self.ip,
            "request_uuid": self.request_uuid,
        }

        final_data = {**session, **data}

        return final_data

    def _validate_data(self, data):
        """
        Function to validate and normalize data.

        :param data:  Dictionary with the info to write on log.
        :type data: dict
        :return: Dictionary with the nomalized data.
        :rtype: dict
        """
        if self.schema is not None:

            val = Validator(self.schema, purge_unknown=True)
            val.validate(data)
            val.normalized(data)

            return json.dumps(val.document)

        else:

            return data

    def write_info(self, data):
        """
        Function to write a log info.

        :param data: Dictionary with the info to write on log.
        :type data: dict.

        """
        final_data = data
        if self.ip is not None:
            final_data = self._add_session(data)

        if self.schema is not None:
            self.log.logger.info(self._validate_data(final_data))
        else:
            self.log.logger.info(final_data)

    def write_error(self, data):
        """

        Function to write a log error.

        :param data: Dictionary with the error to write on log.
        :type data: dict.

        """

        final_data = data
        if self.ip is not None:
            final_data = self._add_session(data)

        if self.schema is not None:
            self.log.logger.error(self._validate_data(final_data))
        else:
            self.log.logger.error(final_data)

    def write_exception(self, exc):
        """
        Function to write a log excepción.

        :param exc: Exception to write on log.
        :type exc: Exception Object.
        """

        _, exc_obj, exc_tb = sys.exc_info()
        name = exc_tb.tb_frame.f_code.co_filename

        exception_data = {
            "exception_type": str(exc.__class__).replace("'", ''),
            "exception_msg": str(exc),
            "module": name,
            "line": exc_tb.tb_lineno
        }

        if self.ip is not None:
            full_data = self._add_session(exception_data)
            self.log.logger.error(json.dumps(full_data))
        else:
            self.log.logger.error(json.dumps(exception_data))
