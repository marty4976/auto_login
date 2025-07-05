import logging

class Logger:
    def __init__(self, *, name: str = 'Chatwork_Logger', level: int = logging.INFO, log_file: str = 'chatwork.log') -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(stream_handler)
            self.logger.addHandler(file_handler)

    def info(self, message: str) -> None:
        self.logger.info(message)
    def error(self, message: str) -> None:
        self.logger.error(message)
    def exception(self, message: str) -> None:
        self.logger.exception(message)  # 追加

def get_logger() -> Logger:
    return Logger()