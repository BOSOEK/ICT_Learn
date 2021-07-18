# QR 코드 리더기

from pyzbar.pyzbar import decode
from PIL import Image  # pillow OpenCV보다 강력하지는 않지만 간단하게 파이썬에서 이미지를 다룰 수 있다.

print("QR 코드 리더기")
qrcode_image = Image.open("my_qrcode.png")
decoded_qrcode = decode(qrcode_image)
print("QR 코드에 담긴 내용 : ", decoded_qrcode[0].data.decode())

