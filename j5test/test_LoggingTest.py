from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from j5test import Utils
try:
    from j5test import LoggingTest
except ImportError:
    LoggingTest = None
import logging

@Utils.if_check(lambda: LoggingTest is not None, "Missing dependencies of LoggingTest")
def test_logging_test():
    with LoggingTest.LoggingTest() as log:
        logging.warning("Warning")
        logging.error("Error")
        logging.critical("Critical")

        assert "Warning" in log.getLogLevel(logging.WARNING)
        assert "Error" in log.getLogLevel(logging.ERROR)
        assert "Critical" in log.getLogLevel(logging.CRITICAL)
