# study_logging_002.py

import logging
#import datetime
# logging.basicConfig(
#     format = "%(process)d - %(levelname)s - %(message)s"
# )
# logging.warning("에러가 발생했습니다")

# 반복문이 실행된 시간

# start_time = datetime.datetime.now()
# for i in range(50000):
#     pass

# end_time = datetime.datetime.now()

# print(start_time)
# print(end_time)

logging.basicConfig(
    format = "%(asctime)s - %(message)s",
    datefmt = "%d-%b-%y %H:%M:%S",
    level = logging.INFO
)
logging.warning("누군가가 로그인 했습니다.")