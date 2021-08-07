def print_file_content():
    with open("descriptions/description-01.txt", "r", encoding="UTF-8") as f:
        print(f.read(5))

def print_file_content_readlines():
    with open("descriptions/description-01.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(type(lines))
        print(lines)
        print(lines[2])

def print_file_content_one_line_at_time():
    with open("descriptions/description-01.txt", "r", encoding="UTF-8") as f:
        line = f.readline()
        while line != "":
            print(line, end="")
            line = f.readline()

if __name__ == "__main__":
    # print_file_content()
    # print_file_content_readlines()
    print_file_content_one_line_at_time()