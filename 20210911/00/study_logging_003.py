import logging

# name = "서버 B"
# logging.error(f"{name}에서 에러가 또 발생했습니다")


logging.basicConfig(
    filename = "app.log",
    filemode = "a",
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding = "UTF-8"
)

a = 5
b = 0

try:
    c = a / b
    print(c)
except Exception as e:
    logging.error("발생한 에러", exc_info = True)
    # logging.exception(e)