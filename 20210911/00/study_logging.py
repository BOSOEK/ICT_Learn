# study_logging.py
# 개발이나 운영시 어떤 결과나 변수값을 확인할 때, print를 사용
# print를 사용하다보면 나중에 그 상황이 언제 발생했는지 모른다.
# 기록이 남지 않는다. 파일로...
# 자바의 경우 log4j와 같은 라이브러리를 사용.
# 파이썬은 logging이라는 기본 라이브러리를 사용
# 로그의 레벨
# DEBUG-> INFO -> WARNING -> ERROR -> CRITICAL : 점점 심각도가 높아지는 레벨

import logging

logging.debug("Debug 모드입니다.")
logging.info("info 모드입니다.")
logging.warning("warning 모드입니다.")
logging.error("error 모드입니다.")
logging.critical("critical 모드입니다.")

# 실행 결과에서 알 수 있는 것!
# WARNING:root:warning 모드입니다.
# ERROR:root:error 모드입니다.      
# CRITICAL:root:critical 모드입니다.

# 1) root : 기본 logger의 이름이다!
# 2) 기본 logger의 레벨은 warning이상이다!

