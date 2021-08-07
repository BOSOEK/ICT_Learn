from pathlib import Path

if __name__ == '__main__':
    #entries = Path.cwd()
    #entries = Path('images')
    entries = Path.home()

    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())
        print('=============================')
