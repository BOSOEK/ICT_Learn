import os
import zipfile
from pathlib import Path

if __name__ == "__main__":

    file_list = []

    for path in Path("images/movies/monsters").iterdir():
        file_list.append("images/movies/monsters/" + path.stem + path.suffix)
    
    print(file_list)
    with zipfile.ZipFile("test_archive.zip", "w") as  archive:
        for file in file_list:
            archive.write(file)
