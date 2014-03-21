import datetime, time, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.propagate = False

handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

while True:
  logger.info('Hello')
  time.sleep(1)
  logger.info('python') 
  time.sleep(1)

