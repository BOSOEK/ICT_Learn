# study_logging_004.py
# 나만의 logger를 만들어 보기

import logging

# 파이썬 기본 logger
#logging.warning("이번에는 경고를 알립니다.")

# 나만의 logger
# logger = logging.getLogger("my_logger")
# logger.warning("이번에는 경고를 알립니다.")

logger = logging.getLogger("my_logger")

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("my_logger.log", encoding="UTF-8")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("my_logger 경고")
logger.error("my_logger 에러")