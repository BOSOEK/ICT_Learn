import os
from datetime import datetime


def format_datatime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    date = utc_timestamp.strftime('%d / %b / %Y %H:%M:%S')
    return date


def display_entries_in_directory(directory):
    # 내가 지정한 디렉토리에 무슨 파일이 있는지 확인

    with os.scandir() as entries:
        for entry in entries:
            print('이름 : ', entry.name)
            info = entry.stat()
            print('생성시간 : ', format_datatime(info.st_ctime))
            print('최종 수정시간 : ', format_datatime(info.st_atime))
            print('파일 크기 : ', info.st_size)


def display_directories(directory):
    # 디렉토리만 보고 싶을때
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_dir():
                print('디렉터리 이름 : ', entry.name)


def display_files(directory):
    # 파일만 보고 싶을때
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file():
                print('파일 이름 : ', entry.name)


if __name__ == '__main__':  # entry point(프로그램의 시작 지점)
    #print('파이썬 프로그램이 시작되었다.')

    display_entries_in_directory('./')
