import os
from pathlib import Path
import shutil

def delete_file_os(target_file):
    os.remove(target_file)
    # os.unlink("backup_articles/article_02.txt")

def delete_file_pathlib(target_file):
    file = Path(target_file)
    file.unlink()

def delete_directory_os(target_directory):
    os.rmdir(target_directory)    

def delete_directory_pathlib(target_directory):
    directory = Path(target_directory)
    directory.rmdir()

def delete_directory_including_subdir(target_directory):
    shutil.rmtree(target_directory)    

if __name__ == "__main__":
    # delete_file_os("backup_articles/article03.txt")
    # delete_file_pathlib("data_article/article_01.txt")
    # delete_directory_pathlib("data_article")
    delete_directory_including_subdir("descriptions")