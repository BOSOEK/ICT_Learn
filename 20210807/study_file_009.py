import shutil

def copy_file(original_file, target_location):
    shutil.copy(original_file, target_location)

def copy_file_with_metadata(original_file, target_location):
    shutil.copy(original_file, target_location) # 파일의 메타정보까지 복사

def copy_directory(origianl_location, target_location):
    shutil.copytree(origianl_location, target_location)

if __name__ == "__main__":
    # copy_file("articles/article_01.txt", "data_article")
    # copy_file_with_metadata("articles/article_01.txt", "data_article") 
    copy_directory("articles/", "backup_articles/")