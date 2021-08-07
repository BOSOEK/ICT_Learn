import os


def top_down_walk():
    for dirpath, dirnames, files in os.walk('images/'):
        print('디렉터리 : ', dirpath)
        print('포함된 디렉터리들')
        for dirname in dirnames:
            print(dirname)
        print('포함된 파일들')
        for filename in files:
            print(filename)
        print()


def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('images/', topdown=False):
        print('디렉터리 : ', dirpath)
        print('포함된 디렉터리들')
        for dirname in dirnames:
            print(dirname)
        print('포함된 파일들')
        for filename in files:
            print(filename)
        print()


if __name__ == '__main__':
    bottom_up_walk()
