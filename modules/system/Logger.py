import logging
from logging.handlers import SysLogHandler

class Logger:
  def __init__(self, formatString = '%(message)s', logLevel = logging.INFO):
    self.logger = logging.getLogger()
    self.logger.setLevel(logLevel)
    self.handler = SysLogHandler(facility=SysLogHandler.LOG_DAEMON, address='/dev/log')
    self.handler.setFormatter(logging.Formatter(formatString))
    self.logger.addHandler(self.handler)


  def write(self, message = ''):
    """ Запис логів різних результатів та дій """
    print(self.logger)
    self.logger.info(message)
