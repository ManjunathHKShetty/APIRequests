import os
import logging


class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "tests", "Logs")

        # Ensure the directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up logging configuration
        logging.basicConfig(
            filename=os.path.join(log_dir, 'auto.log'),
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m%d%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
