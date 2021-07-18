# QR 코드 생성기

import pyqrcode

qrcode = pyqrcode.create(input('QR 코드로 변환할 메시지를 입력해 주세요 : '))
qrcode.png('my_qrcode.png', scale=7)
print('QR 코드가 생성되었습니다.')