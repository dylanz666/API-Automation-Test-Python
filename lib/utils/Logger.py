# Created by Dylan
import time, os, logging

logger = logging.getLogger()
logging.basicConfig(filename=os.getcwd() + '/lib/log/log.log', level=logging.DEBUG,
                    format='%(asctime)s [INFO] %(message)s', datefmt='[%Y-%m-%d %H:%M:%S]')


class Logger:
    def __int__(self):
        print("logger")

    @staticmethod
    def info(*info):
        info_list = list(info)
        for i in range(0, len(info_list)):
            info_list[i] = str(info_list[i])
        log_info = ''.join(info_list)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "[INFO]", log_info)
        logger.info(log_info)

    @staticmethod
    def warning(*info):
        info_list = list(info)
        for i in range(0, len(info_list)):
            info_list[i] = str(info_list[i])
        log_info = ''.join(info_list)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "[WARN]", log_info)
        logger.warning(log_info)

    @staticmethod
    def error(*info):
        info_list = list(info)
        for i in range(0, len(info_list)):
            info_list[i] = str(info_list[i])
        log_info = ''.join(info_list)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "[ERROR]", log_info)
        logger.error(log_info)

    @staticmethod
    def debug(*info):
        info_list = list(info)
        for i in range(0, len(info_list)):
            info_list[i] = str(info_list[i])
        log_info = ''.join(info_list)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "[DEBUG]", log_info)
        logger.debug(log_info)

    @staticmethod
    def critical(*info):
        logger.basicConfig(filename='../../lib/log/log.log', level=logging.DEBUG,
                           format='%(asctime)s [CRITICAL] %(message)s', datefmt='[%Y-%m-%d %H:%M:%S]')
        info_list = list(info)
        for i in range(0, len(info_list)):
            info_list[i] = str(info_list[i])
        log_info = ''.join(info_list)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), "[CRITICAL]", log_info)
        logger.critical(log_info)
