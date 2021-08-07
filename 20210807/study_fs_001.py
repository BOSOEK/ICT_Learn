import os


def display_cwd():
    # 현재 내가 위치한 디렉토리의 경로를 파악하기
    cwd = os.getcwd()
    print('현재 위치한 디렉토리 : ', cwd)


def up_one_directory_level():
    # 내가 위치한 현재의 상위 디렉토리로 이동
    os.chdir('../')  # change directory


def display_entries_in_directory(directory):
    # 내가 지정한 디렉토리에 무슨 파일이 있는지 확인
    # os.listdir() : 내가 위치한 디렉터리에 존재하는 디렉터리 or 파일을 리스트화

    # with os.scandir() as entries:
    #    for entry in entries:
    #        print(entry.name)

    # for entry in os.scandir():
    #    print(entry.name)
    print(os.listdir(directory))


if __name__ == '__main__':  # entry point(프로그램의 시작 지점)
    #print('파이썬 프로그램이 시작되었다.')
    display_cwd()
    # up_one_directory_level()
    # display_cwd()
    display_entries_in_directory('images/')
