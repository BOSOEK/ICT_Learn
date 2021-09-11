# study_logging_001.py

# basicConfig(**kwargs) 메소드 : logger를 설정할 때 사용
# 기본적인 파라미터 (parameter)
# 1) level : logging의 레벨
# 2) filename : 어디에 저장할지
# 3) filemode : 파일에 write or append
# 4) format : 로그 메시지의 형식

import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("디버그 모드입니다.")

logging.basicConfig(
    filename = "app.log",
    filemode = "a",
    format = "%(name)s - %(levelname)s - %(message)s",
    encoding = "UTF-8"
)
logging.warning("이번에는 파일에 저장합니다.")