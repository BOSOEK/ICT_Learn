# logger_load_file.py

import logging
import logging.config

logging.config.fileConfig(fname="file.conf")

logger = logging.getLogger("configLogger")
logger.debug("디버그 모드입니다")