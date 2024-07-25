import logging
from pathlib import Path
from datetime import datetime

LOG_PATH = Path.cwd() / 'logs'

LOG_PATH.mkdir(exist_ok=True, parents=True)

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOG_FILE_PATH = LOG_PATH / LOG_FILE

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('Logging has started')
