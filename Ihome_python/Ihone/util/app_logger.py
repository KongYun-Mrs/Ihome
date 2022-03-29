import os
import logging
from logging.handlers import TimedRotatingFileHandler


def init_log(app):
    request_formatter = logging.Formatter(
        "[%(asctime)s %(levelname)s %(pathname)s/%(filename)s:%(lineno)d %(module)s %(funcName)s] %(message)s")
    logging.basicConfig(level=logging.DEBUG)

    if not os.path.exists("./logs"):
        os.mkdir("./logs")

    file_logger = TimedRotatingFileHandler("logs/Ihome.log", when='midnight', backupCount=7, encoding="UTF-8")
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(request_formatter)
    app.logger.addHandler(file_logger)
