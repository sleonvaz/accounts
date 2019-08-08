import os
from django.test import TestCase
from testfixtures import log_capture
from helpers.logger import LoggerManager


class TestLoggerManager(TestCase):

    dirpath = str(os.path.abspath(__file__)).replace('\\', '\\\\')

    def setUp(self):

        self.logfile = 'test'
        self.schema = {
            "amount": {"type": "string", "default": "sin asignar"},
            "currency": {"type": "string", "default": "sin asignar"},
            "iban": {"type": "string", "default": "sin asignar"},

        }
        self.session_schema = {
            "ip": {"type": "string", "default": "sin asignar"},
            "request_uuid": {"type": "string", "default": "sin asignar"},
        }
        self.full_schema = {**self.session_schema, **self.schema}

        self.data = {
            "amount": "14.50",
            "currency": "EUR",
        }
        self.session = {
            "ip": "192.168.1.1",
            "request_uuid": "AS678234876834GSFA",
        }

    def test_add_session(self):

        test_log2 = LoggerManager(self.logfile, "Test Event", session=self.session)
        response = test_log2._add_session(self.data)
        final_data = {**self.session, **self.data}
        self.assertEqual(response, final_data)

    @log_capture()
    def test_write_error_no_session(self, capture):
        test_log6 = LoggerManager(self.logfile, "test_write_error_no_session", schema=self.schema)
        test_log6.write_error(self.data)

        capture.check(("test_write_error_no_session", "ERROR",
                       '{"amount": "14.50", "currency": "EUR", "iban": "sin asignar"}'))

    @log_capture()
    def test_write_info(self, capture):

        test_log3 = LoggerManager(self.logfile, "test_write_info", self.full_schema, self.session)
        test_log3.write_info(self.data)

        capture.check(("test_write_info", "INFO",
                       '{"ip": "192.168.1.1", "request_uuid": "AS678234876834GSFA", "amount": '
                       '"14.50", "currency": "EUR", "iban": "sin asignar"}'))

    @log_capture()
    def test_write_info_no_session(self, capture):
        test_log4 = LoggerManager(self.logfile, "test_write_info_no_session", self.schema)
        test_log4.write_info(self.data)

        capture.check(("test_write_info_no_session", "INFO",
                       '{"amount": "14.50", "currency": "EUR", "iban": "sin asignar"}'))

    @log_capture()
    def test_write_error(self, capture):
        test_log5 = LoggerManager(self.logfile, "test_write_error", self.full_schema, self.session)
        test_log5.write_error(self.data)

        capture.check(("test_write_error", "ERROR",
                       '{"ip": "192.168.1.1", "request_uuid": "AS678234876834GSFA", "amount": '
                       '"14.50", "currency": "EUR", "iban": "sin asignar"}'))

    @log_capture()
    def test_write_exception_no_session(self, capture):
        test_log7 = LoggerManager(self.logfile, "test_write_exception_no_session")
        try:
            raise Exception("Mock Exception")
        except Exception as err:
            test_log7.write_exception(err)

        capture.check(('test_write_exception_no_session',
                       'ERROR',
                       '{"exception_type": "<class Exception>", "exception_msg": "Mock Exception", "module": "'
                       + "{}".format(self.dirpath)
                       + '", "line": 81}'))

    @log_capture()
    def test_write_exception(self, capture):

        test_log8 = LoggerManager(self.logfile, "test_write_exception", session=self.session)
        try:
            raise Exception("Mock Exception")
        except Exception as err:
            test_log8.write_exception(err)

        capture.check(('test_write_exception',
                       'ERROR',
                       '{"ip": "192.168.1.1", "request_uuid": "AS678234876834GSFA", "exception_type":'
                       ' "<class Exception>", "exception_msg": "Mock Exception", "module": "'
                       + "{}".format(self.dirpath)
                       + '", "line": 96}'))
