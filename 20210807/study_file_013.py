from pathlib import Path

if __name__ == "__main__":
    file_types= [".png", ".svg"]
    for path in Path("images/movies/monsters").iterdir():
        if path.is_file and path.suffix in file_types:
            print(f"파일이름 : {path.stem}")
            new_path = Path("images/movies/monsters" + "_new_" + path.stem + path.suffix)
            path.rename(new_path)