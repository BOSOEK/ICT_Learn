def print_content():
    with open("descriptions/description-03.txt", "r") as f:
        contents = f.read()
        print(contents)

def write_new_content():
    #with open("descriptions/description-01.txt", "w") as f:
    with open("descriptions/description-03.txt", "a") as f:   # a => append
        f.write("대한민국! 배구 화이팅!\n")

if __name__ == "__main__":
    write_new_content()
    print_content()


