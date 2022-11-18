import logging
import sys

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('dali2iot')

console = logging.StreamHandler(sys.stdout)
file = logging.FileHandler('dali2iot.log')

console.setLevel(logging.DEBUG)
file.setLevel(logging.INFO)

console.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(console)
#logger.addHandler(file)
